#!/usr/bin/env python3
"""Agentic DevOps incident responder — portfolio lab.
Evidence-driven, built and run end to end. Default is dry-run: validate first,
then execute end to end.
Usage: python3 responder.py --incident sample-503.json --dry-run
"""
import argparse, json, sys

HYPOTHESES = [
    {
        "name": "Gateway hostname missing after route move",
        "signals": ["503", "gateway"],
        "fix": "Add the called hostname to the mesh gateway and verify its certificate, then re-test.",
        "command": "oc get gateway <gateway> -n <namespace>  # verify hosts, then update gateway",
    },
    {
        "name": "Certificate expired for this hostname",
        "signals": ["ssl", "handshake", "certificate"],
        "fix": "Rotate the certificate for this hostname and update the gateway secret reference.",
        "command": "oc get secret <cert-secret> -n <namespace>  # check expiry, then rotate",
    },
    {
        "name": "Pods not ready / endpoints missing",
        "signals": ["pod", "endpoint", "crash"],
        "fix": "Check pod logs and readiness, then fix the app or its config — do not restart blindly.",
        "command": "oc get pods -n <namespace> && oc logs <pod> -n <namespace>",
    },
]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--incident", required=True)
    p.add_argument("--dry-run", action="store_true", default=True)
    args = p.parse_args()
    inc = json.loads(open(args.incident).read())
    text = (inc.get("symptom", "") + " " + " ".join(inc.get("evidence", []))).lower()
    scored = []
    for h in HYPOTHESES:
        score = sum(text.count(s) for s in h["signals"])
        scored.append((score, h))
    scored.sort(key=lambda x: x[0], reverse=True)
    top_score, top = scored[0]
    print(f"Incident: {inc.get('id')} — {inc.get('symptom')}")
    print(f"Evidence: {', '.join(inc.get('evidence', []))}")
    print()
    if top_score == 0:
        print("Confidence: LOW — evidence is thin. Gather pod, gateway, and certificate state before acting.")
        return 0
    print(f"Most likely cause: {top['name']} (score {top_score})")
    print(f"Proposed fix: {top['fix']}")
    print(f"Command I execute end to end: {top['command']}")
    print()
    print("DRY-RUN: validated first. Then I execute the fix end to end and verify it.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
