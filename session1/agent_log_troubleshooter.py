#!/usr/bin/env python3
"""
A log-reading AI helper. 

What it does: it gathers facts about THIS computer (disk, memory, errors, etc.),
then asks the AI "what looks wrong, and how do I fix it?" — like a doctor reading
your symptoms.

How to run it:
    export OPENAI_API_KEY=sk-...   # or: export AGENT_BACKEND=ollama
    python3 agent_log_troubleshooter.py
"""

import os, subprocess
from openai import OpenAI

# Which AI brain to use, and your secret key (see GUIDE.md for setup).
BACKEND = os.getenv("AGENT_BACKEND", "openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()


def sh(c):
    """Run one shell command and give back its text output."""
    return subprocess.run(c, shell=True, text=True, capture_output=True).stdout.strip()


def gather():
    """Collect clues about this computer's health and bundle them into one report."""
    cmds = [
        ("UNAME", "uname -a"),                                                  # what system is this
        ("UPTIME", "uptime"),                                                   # how long it's been on
        ("DISK", "df -h"),                                                      # how full the disk is
        ("MEM", "free -m || true"),                                             # how much memory is used
        ("FAILED_UNITS", "systemctl --failed || true"),                         # services that crashed
        ("DMESG", "dmesg --ctime --level=err,warn | tail -n 120 || true"),      # recent errors/warnings
        ("SYSLOG", "tail -n 200 /var/log/syslog || tail -n 200 /var/log/messages || true"),  # system log
    ]
    return "\n\n".join([f"## {l}\n{sh(c)}" for l, c in cmds])


def ask_llm(prompt):
    """Send the clues to the AI and return its diagnosis."""
    if BACKEND == "ollama":
        return sh(f"ollama run llama2 {prompt!r}")
    client = OpenAI(api_key=OPENAI_API_KEY or None)
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Linux SRE agent. Output: Summary, Top Findings, Exact Commands."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return r.choices[0].message.content


if __name__ == "__main__":
    # Gather the clues, hand them to the AI, and print the diagnosis.
    print(ask_llm("Analyze logs:\n" + gather()))
