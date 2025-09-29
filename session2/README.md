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
