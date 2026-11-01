#!/usr/bin/env bash
# Generic resource check: show pods and their CPU/memory requests/limits.
# Usage: ./one-agent-resources.sh <namespace>
set -euo pipefail
NS="${1:-default}"
echo "Pods and resource requests/limits in namespace: $NS"
oc get pods -n "$NS" -o custom-columns=NAME:.metadata.name,CPU_REQ:.spec.containers[*].resources.requests.cpu,MEM_REQ:.spec.containers[*].resources.requests.memory,CPU_LIM:.spec.containers[*].resources.limits.cpu,MEM_LIM:.spec.containers[*].resources.limits.memory 2>/dev/null || echo "Log in with oc and check the namespace name, then retry."
