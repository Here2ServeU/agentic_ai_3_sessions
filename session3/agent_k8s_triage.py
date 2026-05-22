#!/usr/bin/env python3
"""
A Kubernetes detective AI helper.

What it does: it takes a snapshot of your cluster (which pods are broken, recent
events, etc.) and asks the AI for the impact, the root cause, and safe fixes.

How to run it:
    export OPENAI_API_KEY=sk-...   # or: export AGENT_BACKEND=ollama
    python3 agent_k8s_triage.py
"""

import os, subprocess, json
from openai import OpenAI

# Which AI brain to use, and your secret key (see GUIDE.md for setup).
BACKEND = os.getenv("AGENT_BACKEND", "openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()


def sh(c):
    """Run one shell command and give back its text output."""
    return subprocess.run(c, shell=True, text=True, capture_output=True).stdout.strip()


def snapshot():
    """Collect the clues from the cluster and bundle them as JSON text."""
    return json.dumps({
        "pods": sh("kubectl get pods -A -o wide"),                                  # all pods + status
        "events": sh("kubectl get events -A --sort-by=.lastTimestamp | tail -n 100"),  # what just happened
        "bad_pods": sh("kubectl get pods -A | egrep 'CrashLoopBackOff|ImagePullBackOff|Error' || true"),  # broken ones
    }, indent=2)


def ask_llm(prompt):
    """Send the clues to the AI and return its triage report."""
    if BACKEND == "ollama":
        return sh(f"ollama run llama2 {prompt!r}")
    client = OpenAI(api_key=OPENAI_API_KEY or None)
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "K8s SRE agent. Provide root cause + safe fixes."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return r.choices[0].message.content


if __name__ == "__main__":
    # Take the snapshot, hand it to the AI, and print the triage report.
    print(ask_llm("Analyze cluster:\n" + snapshot()))
