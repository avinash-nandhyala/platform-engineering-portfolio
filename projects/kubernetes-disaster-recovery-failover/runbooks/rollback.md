# Rollback / failback runbook

1. Confirm primary region is healthy and root cause is fixed.
2. Sync any writes made on standby back to primary, and verify counts.
3. Shift a small percentage of traffic first, watch error rate and latency.
4. If stable for the agreed window, shift the rest.
5. Record actual RTO/RPO, and run a restore drill on the new primary.
6. Post-incident review: what failed, what the drill missed, what changes next.
