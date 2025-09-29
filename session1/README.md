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

---

## About Me  

DevOps, Cloud, and SRE Engineer with AI integration expertise.  
Currently pursuing a PhD in Computer Science (AI & ML in Healthcare, Cloud, and DevOps).  

---

## Skills & Certifications  

![AWS](https://img.shields.io/badge/AWS-orange?logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-blue?logo=microsoft-azure&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=white)
![OpenAI](https://img.shields.io/badge/AI-OpenAI-412991?logo=openai&logoColor=white)

![AWS Solutions Architect](https://img.shields.io/badge/Cert-AWS%20SA-orange?logo=amazon-aws&logoColor=white)
![Azure Solutions Architect Expert](https://img.shields.io/badge/Cert-Azure%20SA%20Expert-blue?logo=microsoft-azure&logoColor=white)
![Terraform Associate](https://img.shields.io/badge/Cert-Terraform%20Assoc-844FBA?logo=terraform&logoColor=white)
![CKA](https://img.shields.io/badge/Cert-CKA-326ce5?logo=kubernetes&logoColor=white)
![PhD-CS](https://img.shields.io/badge/PhD-CS%20(In%20Progress)-lightgrey)

---

[LinkedIn](https://linkedin.com/in/ready2assist) | [GitHub](https://github.com/Here2ServeU)

---
