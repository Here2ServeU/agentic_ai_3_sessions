#!/usr/bin/env bash
#
# Day 3 runner — Kubernetes SRE: Incident Triage
# Deploys a broken workload, then runs the AI triage agent.
#
# Usage:
#   export OPENAI_API_KEY=sk-...        # or: export AGENT_BACKEND=ollama
#   ./run.sh            # deploy bad-deploy.yaml + run triage
#   ./run.sh --cleanup  # remove the broken workload
#
set -euo pipefail
cd "$(dirname "$0")"

BACKEND="${AGENT_BACKEND:-openai}"

# --- Optional cleanup mode ----------------------------------------------
if [ "${1:-}" = "--cleanup" ]; then
  echo "Removing the broken workload (bad-deploy.yaml)..."
  kubectl delete -f bad-deploy.yaml --ignore-not-found
  echo "Cleanup complete."
  exit 0
fi

echo "=================================================="
echo " Day 3 — Kubernetes SRE incident triage"
echo " Backend: ${BACKEND}"
echo "=================================================="

# --- Prerequisite checks -------------------------------------------------
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 is not installed."; exit 1; }
command -v kubectl >/dev/null 2>&1 || { echo "ERROR: kubectl is not installed."; exit 1; }
kubectl cluster-info >/dev/null 2>&1 || { echo "ERROR: no reachable Kubernetes cluster (check your kubeconfig)."; exit 1; }

if [ "${BACKEND}" = "openai" ] && [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "ERROR: OPENAI_API_KEY is not set."
  echo "Set it with:  export OPENAI_API_KEY=sk-...   (or use: export AGENT_BACKEND=ollama)"
  exit 1
fi

# --- Install Python dependencies ----------------------------------------
echo "[1/3] Installing Python dependencies..."
python3 -m pip install -q -r ../requirements.txt

# --- Deploy the broken workload ------------------------------------------
echo
echo "[2/3] Deploying the broken workload (expect ImagePullBackOff)..."
kubectl apply -f bad-deploy.yaml
echo "  Waiting 15s for the failure to surface..."
sleep 15
kubectl get pods -l app=bad-api -o wide || true

# --- Run the triage agent ------------------------------------------------
echo
echo "[3/3] Running agent_k8s_triage.py (AI root-cause + safe fixes)..."
python3 agent_k8s_triage.py

echo
echo "Day 3 complete. Clean up the broken workload with:  ./run.sh --cleanup"
echo "See session3/README.md for line-by-line explanations."
