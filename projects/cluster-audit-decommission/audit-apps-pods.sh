#!/usr/bin/env bash
# Generic cluster audit: list pods per namespace as CSV. Read-only.
# Usage: ./audit-apps-pods.sh > audit.csv
set -euo pipefail
echo "namespace,pod,phase,node"
oc get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace},{.metadata.name},{.status.phase},{.spec.nodeName}{"\n"}{end}' 2>/dev/null || {
  echo "oc is not logged in, or no pods were returned. Log in to your own cluster and retry." >&2
  exit 1
}
