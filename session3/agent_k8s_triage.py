#!/usr/bin/env python3
import os, subprocess, json
from openai import OpenAI

BACKEND=os.getenv("AGENT_BACKEND","openai").lower()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY","").strip()

def sh(c): return subprocess.run(c, shell=True, text=True, capture_output=True).stdout.strip()

def snapshot():
    return json.dumps({
        "pods": sh("kubectl get pods -A -o wide"),
        "events": sh("kubectl get events -A --sort-by=.lastTimestamp | tail -n 100"),
        "bad_pods": sh("kubectl get pods -A | egrep 'CrashLoopBackOff|ImagePullBackOff|Error' || true")
    }, indent=2)

def ask_llm(prompt):
    if BACKEND=="ollama": return sh(f"ollama run llama2 {prompt!r}")
    client=OpenAI(api_key=OPENAI_API_KEY or None)
    r=client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role":"system","content":"K8s SRE agent. Provide root cause + safe fixes."},
                  {"role":"user","content": prompt}],temperature=0.2)
    return r.choices[0].message.content

if __name__=="__main__":
    print(ask_llm("Analyze cluster:\n"+snapshot()))
