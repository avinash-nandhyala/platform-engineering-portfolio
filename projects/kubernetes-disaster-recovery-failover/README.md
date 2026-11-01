# Multi-Region Kubernetes Disaster Recovery & Failover Platform ★

A production-grade disaster recovery platform for Kubernetes, built end to end:
backup, restore drills, failover decisions, and runbooks — designed, built,
tested, and operated end to end.

This is a portfolio build / lab. Sample data is labelled as sample. No
company-confidential code, cluster names, app names, internal tickets, or internal
data are included.

## Why this is strong

Most portfolios show how to deploy an app. This shows how to *save* one when a
whole region goes down — the question senior SRE and platform engineers are
actually hired to answer:

- Can we restore? How fast? How much data do we lose?
- Who decides to fail over, and what evidence do they need?
- How do we prove it works, before a real outage forces us to find out?

## Architecture, in one paragraph

Two regions, one active, one standby. Velero backs up cluster state and persistent
volumes on a schedule. A drill restores to an isolated namespace and validates
the app, so a backup is never trusted on faith. A failover engine scores region
health, data lag, and error budget, and proposes FAILOVER, HOLD, or PARTIAL —
I run the engine, I decide, I execute the runbook,
traffic shifts, and the drill is recorded — end to end.

## Recovery tiers

| Tier | RTO | RPO | Example |
|------|-----|-----|---------|
| Critical | 15 minutes | 5 minutes | Checkout, payments, auth |
| Standard | 1 hour | 1 hour | Internal tools, reporting |
| Best effort | 24 hours | 24 hours | Batch jobs, archives |

RTO = how fast you are back. RPO = how much data you can afford to lose.
A 5-minute RPO means, at worst, the last 5 minutes of writes are lost.

## Files

- `velero/schedule.yaml` — daily backup schedule, with critical namespaces first
- `velero/backup-storage-location.yaml` — sample backup storage location
- `failover.py` — failover decision engine I built and run end to end, with `--test`
- `rto.py` — RTO / RPO calculator: given restore time and data lag, does it meet the tier?
- `sample-status.json` — sample region status, labelled as sample
- `runbooks/restore-drill.md` — monthly restore drill, step by step
- `runbooks/failover.md` — failover runbook, with rollback
- `runbooks/rollback.md` — how to fail back when the primary region recovers

## Run it

```bash
# Check a failover decision from sample status (dry-run, no change applied)
python3 failover.py --status sample-status.json --dry-run

# Check whether a restore meets the Critical tier
python3 rto.py --restore-minutes 12 --data-lag-minutes 4 --tier critical

# Run the built-in tests
python3 failover.py --test
python3 rto.py --test
```

Expected sample output: the sample region is unhealthy, data lag is 3 minutes,
so the engine proposes FAILOVER for Critical tier, but applies nothing in
dry-run mode. The RTO check passes: 12 minutes restore + 4 minutes lag is
inside Critical (15 / 5).

## End-to-end ownership — the key design choice

I own failover end to end, from evidence to verification — no step is left
to an unchecked automation:

1. I gather evidence: region health, data lag, error budget, backup age
2. I decide, using the engine I built, with reasons in plain language
3. I execute the traffic shift, following the failover runbook
4. I verify the standby: health, data, error rate, and user-facing checks
5. If the primary recovers, I fail back following the rollback runbook

## What a recruiter can verify

- `failover.py --test` passes, and the decision logic is readable, not magic
- `rto.py --test` passes, and the tier math is explicit
- The Velero manifests are real, apply-ready shapes, not screenshots
- The runbooks cover drill, failover, and rollback — the three things that
  actually go wrong in a real disaster
