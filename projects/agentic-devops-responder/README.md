# Agentic DevOps Incident Responder — Advanced

## What it is
An LLM-style incident agent with a tool loop, built as a portfolio project to show how agentic DevOps should actually work in production:

1. **Gather evidence first** — pods, mesh gateway state, and recent metrics (supplied as structured sample evidence in this lab, not live cluster access).
2. **Rank causes** — score hypotheses against the evidence, instead of jumping to the first plausible fix.
3. **Propose, don't apply** — in `--dry-run` (default) it prints the proposed fix and stops. A real change requires a human approval gate, by design.

This mirrors the AWS Agentic AI DevOps pattern: an agent that investigates and resolves operational incidents, learns from them, and shapes service architecture — but with guardrails, so it cannot make a bad incident worse.

## Run it
```bash
python3 responder.py --incident sample-503.json --dry-run
python3 responder.py --incident sample-cert.json --dry-run
```

## Sample incidents
- `sample-503.json` — 503s, pods healthy, gateway hostname missing
- `sample-cert.json` — SSL handshake errors, certificate expired for one hostname

## Guardrails (the point of the project)
- No automatic kubectl apply, no automatic restarts, no secret access
- Every proposal includes: evidence used, confidence, and the exact command a human should review
- If evidence is thin, it says so and asks for more — it does not hallucinate a root cause

## Files
- `responder.py` — the agent loop (evidence → hypotheses → proposal)
- `sample-503.json`, `sample-cert.json` — structured sample evidence, clearly labelled
