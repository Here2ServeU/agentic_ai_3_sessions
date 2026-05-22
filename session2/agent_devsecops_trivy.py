#!/usr/bin/env python3
"""
A security AI helper (DevSecOps).

What it does: it reads a Trivy scan file (a list of security weak spots found in
a container image) and asks the AI which ones to fix FIRST, and how.

How to run it:
    export OPENAI_API_KEY=sk-...   # or: export AGENT_BACKEND=ollama
    python3 agent_devsecops_trivy.py
"""

import os, subprocess
from openai import OpenAI

# Which AI brain to use, and your secret key (see GUIDE.md for setup).
BACKEND = os.getenv("AGENT_BACKEND", "openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()


def ask_llm(prompt):
    """Send a question to the AI (OpenAI or Ollama) and return its answer."""
    if BACKEND == "ollama":
        return subprocess.run(["ollama", "run", "llama2", prompt], capture_output=True, text=True).stdout.strip()
    client = OpenAI(api_key=OPENAI_API_KEY or None)
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "DevSecOps triage. Give prioritized issues and fixes."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,  # Very steady answers — good for security advice.
    )
    return r.choices[0].message.content


if __name__ == "__main__":
    # Open the saved scan file. (Make one with: trivy image --format json ...)
    with open("trivy_nginx.json") as f:
        report = f.read()
    # Send the first chunk of the report to the AI for a summary and fixes.
    print(ask_llm("Summarize and fix these Trivy findings:\n" + report[:15000]))
