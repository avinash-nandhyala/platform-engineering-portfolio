# SLO & Observability Automation — Advanced

## Why SLOs, not just alerts
A dashboard with 200 alerts teaches a team to ignore alerts. An SLO teaches a team what "good" means, how much error budget is left, and when to stop shipping features and fix reliability instead.

This project implements that, with tests:

- **SLO definition** — e.g. 99.9% successful requests over 30 days = 43 minutes of error budget
- **Burn-rate alerts** — alert fast when you are burning budget 14x faster than sustainable, page slower when burning 2x — the standard multi-window, multi-burn-rate pattern
- **Error-budget math** — tested in `slo.py --test`, so the numbers are not hand-waved
- **Runbook linking** — every alert rule in `alerts.yaml` points to a runbook file, so the on-call engineer is not searching at 2am

## Files
- `slo.py` — error-budget calculator + burn-rate helper, with `--test`
- `alerts.yaml` — Prometheus-style alert rules (generic, sample service names)
- `runbooks/` — short runbooks for the two alert types above

## Run it
```bash
python3 slo.py --test
python3 slo.py --slo 99.9 --window-days 30
```

## What a hiring manager should take from this
I do not just "set up Prometheus". I define reliability in numbers, alert on budget burn instead of noise, and close the loop with runbooks and postmortems. That is SRE work, not monitoring theatre.
