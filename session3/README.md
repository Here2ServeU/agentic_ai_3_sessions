# Session 3 — Kubernetes SRE: Incident Triage

## Overview
In this session, you’ll:
- Deploy a broken workload (`bad-deploy.yaml`)
- Use `agent_k8s_triage.py` to snapshot the cluster
- Get an AI-generated triage report with fixes

---

## Script 1: `bad-deploy.yaml`

This file creates a Deployment with an invalid image tag.

### Explanation
- `nginx:0.0` does not exist.
- Kubernetes will fail to pull the image → `ImagePullBackOff` error.
- Perfect for testing incident triage.

---

## Script 2: `agent_k8s_triage.py`

This script collects cluster state and asks AI for triage.

### Explanation
- Import libraries (`os`, `subprocess`, `json`, `OpenAI`).
- Define helper `sh()` to run commands.
- Define `snapshot()` to collect:
  - Pod status
  - Events
  - Bad pods
- Send snapshot to AI using `ask_llm()`.
- AI responds with:
  - Impact
  - Root cause
  - Suggested fixes (`kubectl set image`, rollback, etc.).
