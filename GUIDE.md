# Bootcamp Guide — One Script Per Day

This guide ties the three sessions together. Each day (session) ships a single
runnable script, `run.sh`, that checks prerequisites, installs dependencies, and
runs that day's exercises in order. Use this file as your map; each session's own
`README.md` explains the underlying scripts line by line.

---

## One-Time Setup

```bash
# 1. Clone and enter the repo
git clone https://github.com/Here2ServeU/agentic_ai_3_sessions.git
cd agentic_ai_3_sessions

# 2. (Recommended) create a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# 3. Install Python dependencies for all sessions
pip install -r requirements.txt

# 4. Choose your AI backend
export OPENAI_API_KEY=sk-...     # use OpenAI (default)
# --- or ---
export AGENT_BACKEND=ollama      # use a local Ollama model instead
```

Every `run.sh` honours the `AGENT_BACKEND` variable, so you can switch between
OpenAI and Ollama at any time without editing code.

---

## Day 1 — Setup + Log Troubleshooting

Run your first AI agent and a Linux log-troubleshooting agent.

```bash
cd session1
./run.sh
```

What it does:
1. Installs dependencies.
2. Runs `agent_unified.py` → generates a Kubernetes Deployment YAML.
3. Runs `agent_log_troubleshooter.py` → collects this host's logs and asks the AI to diagnose issues.

| Requirement | Why |
|-------------|-----|
| `python3`   | runs the agents |
| `OPENAI_API_KEY` *or* `AGENT_BACKEND=ollama` | talks to the model |

---

## Day 2 — DevSecOps & FinOps

Summarize container vulnerabilities and find AWS cost savings with AI.

```bash
cd session2
./run.sh
```

What it does:
1. Installs dependencies.
2. **DevSecOps:** if `trivy_nginx.json` is missing, it runs a Trivy scan (when `trivy` is installed), then `agent_devsecops_trivy.py` prioritizes the findings and fixes.
3. **FinOps:** if working AWS credentials are detected, `agent_finops_aws.py` reads Cost Explorer data and proposes savings.

| Requirement | Why |
|-------------|-----|
| `python3`, `OPENAI_API_KEY`/Ollama | runs the agents |
| `trivy` *(optional)* | generates the vulnerability report |
| AWS credentials *(optional)* | Cost Explorer access for FinOps |

Steps with missing optional tools are skipped with a clear message, so the
script never fails just because Trivy or AWS isn't configured.

---

## Day 3 — Kubernetes SRE: Incident Triage

Deploy a deliberately broken workload, then let the AI triage it.

```bash
cd session3
./run.sh            # deploy bad-deploy.yaml + run AI triage
./run.sh --cleanup  # remove the broken workload when finished
```

What it does:
1. Installs dependencies.
2. Applies `bad-deploy.yaml` (an invalid image tag → `ImagePullBackOff`).
3. Runs `agent_k8s_triage.py` → snapshots the cluster and returns impact, root cause, and safe fixes.

| Requirement | Why |
|-------------|-----|
| `python3`, `OPENAI_API_KEY`/Ollama | runs the agent |
| `kubectl` + a reachable cluster | deploys and inspects the workload |

> **Remember to clean up** with `./run.sh --cleanup` so the broken pod doesn't linger.

---

## Troubleshooting

- **`OPENAI_API_KEY is not set`** — export the key, or switch to Ollama with `export AGENT_BACKEND=ollama`.
- **`no reachable Kubernetes cluster`** (Day 3) — check `kubectl cluster-info` and your kubeconfig.
- **FinOps step skipped** (Day 2) — run `aws configure` and ensure the IAM user has Cost Explorer permissions.
- **Dependency errors** — re-run `pip install -r requirements.txt` inside your virtual environment.

---

[LinkedIn](https://linkedin.com/in/ready2assist) | [GitHub](https://github.com/Here2ServeU)
