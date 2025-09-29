# Session 2 — Agentic DevSecOps & FinOps

## Overview
In this session, you’ll:
- Scan an image with Trivy
- Use AI (`agent_devsecops_trivy.py`) to summarize vulnerabilities and fixes
- Use AI (`agent_finops_aws.py`) to analyze AWS costs and suggest savings

---

## Script 1: `agent_devsecops_trivy.py`

This script reads a Trivy scan and asks AI to prioritize vulnerabilities and suggest fixes.

### Explanation
- Import libraries.
- Define `ask_llm()` to query OpenAI or Ollama.
- Open saved `trivy_nginx.json` report.
- Send to AI for summary and remediation steps.

---

## Script 2: `agent_finops_aws.py`

This script gets AWS cost data and asks AI for savings recommendations.

### Explanation
- Import `boto3` to use AWS Cost Explorer.
- Function `ce_last_7d()` fetches costs for last 7 days by service.
- Send data to AI.
- AI outputs FinOps plan (rightsizing, Spot, Savings Plans).
