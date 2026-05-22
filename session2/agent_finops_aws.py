#!/usr/bin/env python3
"""
A cloud-cost AI helper (FinOps).

What it does: it reads your AWS spending for the last 7 days, then asks the AI
for smart ways to spend less money.

Needs working AWS login info (run `aws configure` first).

How to run it:
    export OPENAI_API_KEY=sk-...   # or: export AGENT_BACKEND=ollama
    python3 agent_finops_aws.py
"""

import os, datetime, boto3
from openai import OpenAI

# Which AWS region and AI brain to use, plus your secret key.
REGION = os.getenv("AWS_REGION", "us-east-1")
BACKEND = os.getenv("AGENT_BACKEND", "openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()


def ce_last_7d():
    """Ask AWS Cost Explorer how much was spent in the last 7 days, by service."""
    ce = boto3.client("ce", region_name=REGION)
    end = datetime.date.today()
    start = end - datetime.timedelta(days=7)
    r = ce.get_cost_and_usage(
        TimePeriod={"Start": start.isoformat(), "End": end.isoformat()},
        Granularity="DAILY",
        Metrics=["UnblendedCost"],
        GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}],
    )
    # Pull out (service name, cost amount) for each result.
    return [(g["Keys"][0], g["Metrics"]["UnblendedCost"]["Amount"]) for d in r["ResultsByTime"] for g in d.get("Groups", [])]


def ask_llm(prompt):
    """Send the cost numbers to the AI and return its savings plan."""
    if BACKEND == "ollama":
        import subprocess
        return subprocess.run(["ollama", "run", "llama2", prompt], capture_output=True, text=True).stdout.strip()
    client = OpenAI(api_key=OPENAI_API_KEY or None)
    rr = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "FinOps coach. Provide savings plan and commands."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return rr.choices[0].message.content


if __name__ == "__main__":
    # Grab the costs and ask the AI for a savings plan.
    print(ask_llm(f"Create FinOps plan: {ce_last_7d()[:10]}"))
