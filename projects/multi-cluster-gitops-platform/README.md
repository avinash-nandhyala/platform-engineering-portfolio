# Multi-Cluster GitOps Platform — Advanced

## Architecture
```
Git repo (desired state)
  └─ environments/ dev → staging → prod (promotion gates)
       └─ ArgoCD ApplicationSet (one app per cluster, templated)
            └─ Clusters: cluster-a, cluster-b, cluster-c (placeholders)
                 └─ Policy check: no privileged pods, resource limits required
                      └─ Drift report: ./drift-report.py
```

## Why this is senior-level, not a demo
- **Templating, not copy-paste:** ApplicationSet generates one Application per cluster from a single template. Adding a cluster is adding a list entry, not a new YAML file.
- **Promotion with gates:** prod is not auto-synced from main. A promotion PR moves a version forward, so a bad dev change cannot silently reach prod.
- **Policy as a gate:** workloads without resource limits or with privileged containers fail the check in `policy-check.py` before they are applied.
- **Drift visibility:** `drift-report.py` compares desired vs. actual (from a supplied inventory file in this lab) and lists out-of-sync apps — the report a platform lead actually reads on Monday morning.

## Files
- `argocd/applicationset.yaml` — ApplicationSet template (placeholders for repo URL and clusters)
- `environments/` — dev / staging / prod value overlays
- `policy-check.py` — fails on privileged containers or missing limits; includes a self-test
- `drift-report.py` — reads `sample-inventory.json` and reports drift

## Run the checks (no cluster needed)
```bash
python3 policy-check.py --test
python3 drift-report.py
```

All cluster names, repo URLs, and inventory data here are placeholders / samples.
