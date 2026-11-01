# Restore drill runbook

Run monthly. A backup that has never been restored is a hope, not a backup.

1. Pick the latest backup. Record its age and size.
2. Restore to an isolated namespace, never over production.
3. Check: pods running, service reachable, data present (sample row counts).
4. Measure restore time. Compare to the tier RTO with `rto.py`.
5. Record the result: pass/fail, restore time, data lag, issues found.
6. Fix any issue found, then re-drill. Do not close the drill as "pass" with
   a known restore failure still open.
