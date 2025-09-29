#!/usr/bin/env python3
import os, subprocess
from openai import OpenAI

BACKEND = os.getenv("AGENT_BACKEND","openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","").strip()

def sh(c): return subprocess.run(c, shell=True, text=True, capture_output=True).stdout.strip()

def gather():
    cmds=[("UNAME","uname -a"),("UPTIME","uptime"),("DISK","df -h"),
          ("MEM","free -m || true"),("FAILED_UNITS","systemctl --failed || true"),
          ("DMESG","dmesg --ctime --level=err,warn | tail -n 120 || true"),
          ("SYSLOG","tail -n 200 /var/log/syslog || tail -n 200 /var/log/messages || true")]
    return "\n\n".join([f"## {l}\n{sh(c)}" for l,c in cmds])

def ask_llm(prompt):
    if BACKEND=="ollama": return sh(f"ollama run llama2 {prompt!r}")
    client=OpenAI(api_key=OPENAI_API_KEY or None)
    r=client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role":"system","content":"Linux SRE agent. Output: Summary, Top Findings, Exact Commands."},
                  {"role":"user","content": prompt}],temperature=0.2)
    return r.choices[0].message.content

if __name__=="__main__":
    print(ask_llm("Analyze logs:\n"+gather()))
