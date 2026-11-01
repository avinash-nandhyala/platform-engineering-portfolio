#!/usr/bin/env bash
# Generic, read-only service mesh gateway check.
# Usage: ./check-gateway.sh <namespace> <gateway-name>
# Requires: oc (OpenShift CLI), logged in to your own cluster.
set -euo pipefail
NS="${1:-}"
GW="${2:-}"
if [ -z "$NS" ] || [ -z "$GW" ]; then
  echo "Usage: $0 <namespace> <gateway-name>" >&2
  exit 1
fi
echo "== Pods in $NS =="
oc get pods -n "$NS" || true
echo
echo "== Routes in $NS =="
oc get route -n "$NS" || true
echo
echo "== Gateway $GW =="
oc get gateway "$GW" -n "$NS" -o yaml 2>/dev/null | grep -E "hosts:|credentialName:|name:" || oc get gateway -n "$NS" || true
echo
echo "Compare gateway hosts above with route hosts. A hostname in the route but missing from the gateway is a likely 503 / SSL cause."
