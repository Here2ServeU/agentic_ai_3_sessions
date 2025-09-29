#!/usr/bin/env python3
import os, subprocess
from openai import OpenAI

BACKEND=os.getenv("AGENT_BACKEND","openai").lower()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY","").strip()

def ask_llm(prompt):
    if BACKEND=="ollama":
        return subprocess.run(["ollama","run","llama2", prompt], capture_output=True, text=True).stdout.strip()
    client=OpenAI(api_key=OPENAI_API_KEY or None)
    r=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"DevSecOps triage. Give prioritized issues and fixes."},
                  {"role":"user","content": prompt}],temperature=0.1)
    return r.choices[0].message.content

if __name__=="__main__":
    with open("trivy_nginx.json") as f: report=f.read()
    print(ask_llm("Summarize and fix these Trivy findings:\n"+report[:15000]))
