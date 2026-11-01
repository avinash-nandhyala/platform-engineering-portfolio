# Cluster Audit & Decommission Scripts — Generic Recreation

## Why this exists
Before a cluster is retired, you need a trustworthy answer to: what is still running here, who owns it, and what will break if we turn it off? Guessing from memory is how migrations stall.

These scripts answer that from the cluster itself, with `oc` output you can save and share.

## Scripts

```bash
# List apps/pods per namespace, with a CSV you can hand to owners
./audit-apps-pods.sh <cluster-context-label> > audit.csv

# Surface pods with high CPU/memory requests, especially single-agent pods
./one-agent-resources.sh <namespace>
```

Both are read-only. They do not delete, scale, or migrate anything.

## Output you can act on
- A namespace-by-namespace list of workloads still present
- A shortlist of resource-heavy pods to review before migration
- A file you can send to owners asking: migrated, still in use, or safe to retire?

## What this is not
It is not a migration tool, and it contains no real cluster, app, or owner data. Run it against your own lab or authorised cluster, with your own namespaces.
