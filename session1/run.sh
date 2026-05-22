#!/usr/bin/env bash
#
# Day 1 runner — Setup + Log Troubleshooting
# Runs both Session 1 agents in order. Safe to re-run.
#
# Usage:
#   export OPENAI_API_KEY=sk-...        # or: export AGENT_BACKEND=ollama
#   ./run.sh
#
set -euo pipefail
cd "$(dirname "$0")"

BACKEND="${AGENT_BACKEND:-openai}"

echo "=================================================="
echo " Day 1 — Your first AI agent + log troubleshooting"
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

# --- Exercise 1: generate Kubernetes YAML --------------------------------
echo
echo "[2/3] Running agent_unified.py (generate a Kubernetes Deployment)..."
python3 agent_unified.py

# --- Exercise 2: troubleshoot system logs --------------------------------
echo
echo "[3/3] Running agent_log_troubleshooter.py (analyze this host's logs)..."
python3 agent_log_troubleshooter.py

echo
echo "Day 1 complete. See session1/README.md for line-by-line explanations."
