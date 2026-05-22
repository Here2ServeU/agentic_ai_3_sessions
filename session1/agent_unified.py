#!/usr/bin/env python3
"""
Your FIRST AI helper. 

What it does: it asks the AI to write a Kubernetes "Deployment" file for you
(the settings that say "keep my app running").

How to run it:
    export OPENAI_API_KEY=sk-...   # or: export AGENT_BACKEND=ollama
    python3 agent_unified.py
"""

import os, subprocess
from openai import OpenAI

# Which AI brain should we use? "openai" (default) or "ollama".
# This reads the note you left with the `export AGENT_BACKEND=...` command.
BACKEND = os.getenv("AGENT_BACKEND", "openai").lower()

# Your secret OpenAI key (only needed for the OpenAI brain).
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()


def ask_llm(prompt: str) -> str:
    """Send a question to the AI and return its answer (like a waiter taking your order)."""
    if BACKEND == "ollama":
        # Ask the free AI brain running on your own computer.
        out = subprocess.run(["ollama", "run", "llama2", prompt], capture_output=True, text=True)
        return out.stdout.strip()

    # Otherwise, ask OpenAI's brain over the internet.
    client = OpenAI(api_key=OPENAI_API_KEY or None)
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # The "system" message tells the AI what kind of helper to be.
            {"role": "system", "content": "Helpful DevOps agent. Give exact commands."},
            # The "user" message is your actual question.
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,  # Low number = steady, predictable answers.
    )
    return r.choices[0].message.content


if __name__ == "__main__":
    # Here is the question we ask the AI. Try changing it and run again!
    print(ask_llm("Generate a Kubernetes Deployment for Express app on port 3000 with 2 replicas."))
