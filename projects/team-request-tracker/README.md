# Team Request Tracker — Generic Recreation

## Problem
Work that arrives in a shared team mailbox is invisible unless someone logs it. Leadership then asks "what has the team been doing?" and the answer is anecdote, not evidence.

## Solution pattern
Log every request once, with intake date, requester (role, not personal data in this sample), summary, owner, status, and close date. Then generate a weekly summary from that log — no manual recounting.

This project is a clean recreation of that pattern. The sample data below is invented for demonstration only; no real requests, people, or internal content are included.

## Run it

```bash
python3 tracker.py --report
# Reads requests.csv (sample data included), prints open / closed counts and a weekly summary.
```

## Sample data
`requests.csv` contains a handful of clearly-labelled sample rows, e.g. "SAMPLE: route certificate check" — replace them with your own team's log.

## Why recruiters / platform leads care
This is the tracker pattern: make invisible team work visible, measurable, and reportable, without building app-team self-service that bypasses the platform team. It is team-internal tooling, for the team that runs the platform.
