#!/usr/bin/env python3
import os, datetime, boto3
from openai import OpenAI

REGION=os.getenv("AWS_REGION","us-east-1")
BACKEND=os.getenv("AGENT_BACKEND","openai").lower()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY","").strip()

def ce_last_7d():
    ce=boto3.client("ce",region_name=REGION)
    end=datetime.date.today()
    start=end-datetime.timedelta(days=7)
    r=ce.get_cost_and_usage(TimePeriod={"Start":start.isoformat(),"End":end.isoformat()},
                            Granularity="DAILY", Metrics=["UnblendedCost"],
                            GroupBy=[{"Type":"DIMENSION","Key":"SERVICE"}])
    return [(g["Keys"][0],g["Metrics"]["UnblendedCost"]["Amount"]) for d in r["ResultsByTime"] for g in d.get("Groups",[])]

def ask_llm(prompt):
    if BACKEND=="ollama":
        import subprocess; return subprocess.run(["ollama","run","llama2", prompt], capture_output=True, text=True).stdout.strip()
    client=OpenAI(api_key=OPENAI_API_KEY or None)
    rr=client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role":"system","content":"FinOps coach. Provide savings plan and commands."},
                  {"role":"user","content": prompt}],temperature=0.2)
    return rr.choices[0].message.content

if __name__=="__main__":
    print(ask_llm(f"Create FinOps plan: {ce_last_7d()[:10]}"))
