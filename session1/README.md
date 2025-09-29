# Session 1 — Setup + Log Troubleshooting

## Overview
In this session, you’ll:
- Install Python and AI libraries
- Run your first AI agent (`agent_unified.py`) to generate Kubernetes YAML
- Build a log-troubleshooting agent (`agent_log_troubleshooter.py`) to analyze system logs

---

## Script 1: `agent_unified.py`

This script asks AI to generate a Kubernetes Deployment YAML.

### Explanation
- Import libraries (`os`, `subprocess`, `OpenAI`).
- Check if backend is `openai` or `ollama`.
- Define function `ask_llm` to talk to the AI.
- If using OpenAI, send prompt and return reply.
- If using Ollama, run local model.
- Finally, print a Deployment YAML for an Express app.

---

## Script 2: `agent_log_troubleshooter.py`

This script collects Linux system info and asks AI to diagnose problems.

### Explanation
- Import libraries.
- Define helper `sh()` to run shell commands.
- Define `gather()` to collect system data (disk, memory, uptime, logs, errors).
- Send this combined data to the AI using `ask_llm`.
- Print AI’s troubleshooting summary and commands.
