# Incident Memory CLI — Generic Prototype

## Idea
When a teammate hits a symptom or error, they should be able to ask "have we seen this before?" and get the previous fix — not start from zero every time.

This is a tiny prototype of that idea: incident notes live as Markdown files in `notes/`, and a CLI searches them by keyword.

## Run it

```bash
python3 incident-memory.py "503 gateway"
python3 incident-memory.py "certificate"
```

## Notes included
Only generic, sample incidents are included — for example, a gateway hostname mismatch causing 503s, and a certificate expiry causing handshake errors. No real company incidents, tickets, app names, or internal data are included. Replace `notes/` with your own team's (sanitised) write-ups in a real deployment.

## Why this matters for SRE / platform roles
Incident memory is how a team gets faster without hiring more people: the second time an issue happens, the fix is already written down and searchable. This prototype shows the pattern in under 100 lines, so a team can adopt it without a new platform.
