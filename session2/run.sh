#!/usr/bin/env bash
#
# Day 2 runner — Agentic DevSecOps & FinOps
# Runs the Trivy security agent and the AWS FinOps agent.
#
# Usage:
#   export OPENAI_API_KEY=sk-...        # or: export AGENT_BACKEND=ollama
#   ./run.sh
#
set -euo pipefail
cd "$(dirname "$0")"

BACKEND="${AGENT_BACKEND:-openai}"

echo "=================================================="
echo " Day 2 — DevSecOps (Trivy) + FinOps (AWS)"
echo " Backend: ${BACKEND}"
echo "=================================================="

# --- Prerequisite checks -------------------------------------------------
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 is not installed."; exit 1; }

if [ "${BACKEND}" = "openai" ] && [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "ERROR: OPENAI_API_KEY is not set."
  echo "Set it with:  export OPENAI_API_KEY=sk-...   (or use: export AGENT_BACKEND=ollama)"
  exit 1
fi

# --- Install Python dependencies ----------------------------------------
echo "[1/3] Installing Python dependencies..."
python3 -m pip install -q -r ../requirements.txt

# --- Exercise 1: DevSecOps with Trivy ------------------------------------
echo
echo "[2/3] DevSecOps — agent_devsecops_trivy.py"
if [ ! -f trivy_nginx.json ]; then
  if command -v trivy >/dev/null 2>&1; then
    echo "  No trivy_nginx.json found — scanning nginx:latest with Trivy..."
    trivy image --format json --output trivy_nginx.json nginx:latest
  else
    echo "  SKIP: trivy_nginx.json not found and 'trivy' is not installed."
    echo "  Generate a report first, e.g.:"
    echo "     trivy image --format json --output session2/trivy_nginx.json nginx:latest"
  fi
fi
if [ -f trivy_nginx.json ]; then
  python3 agent_devsecops_trivy.py
fi

# --- Exercise 2: FinOps with AWS Cost Explorer ---------------------------
echo
echo "[3/3] FinOps — agent_finops_aws.py"
echo "  Note: this needs valid AWS credentials with Cost Explorer access."
if command -v aws >/dev/null 2>&1 && aws sts get-caller-identity >/dev/null 2>&1; then
  python3 agent_finops_aws.py
else
  echo "  SKIP: no working AWS credentials detected (run 'aws configure' first)."
fi

echo
echo "Day 2 complete. See session2/README.md for line-by-line explanations."
