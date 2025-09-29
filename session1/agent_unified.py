import os, subprocess
from openai import OpenAI

BACKEND = os.getenv("AGENT_BACKEND","openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","").strip()

def ask_llm(prompt: str) -> str:
    if BACKEND == "ollama":
        out = subprocess.run(["ollama","run","llama2", prompt], capture_output=True, text=True)
        return out.stdout.strip()
    client = OpenAI(api_key=OPENAI_API_KEY or None)
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"Helpful DevOps agent. Give exact commands."},
                  {"role":"user","content": prompt}],
        temperature=0.2
    )
    return r.choices[0].message.content

if __name__ == "__main__":
    print(ask_llm("Generate a Kubernetes Deployment for Express app on port 3000 with 2 replicas."))
