# Failover runbook

Human approval required. Automation proposes, a human decides.

1. Run `failover.py --status <status.json> --dry-run` and read the reasons.
2. Confirm: primary really down, standby healthy, backup age acceptable.
3. Get explicit approval, and record who approved and when.
4. Shift traffic to standby, following the traffic-shift checklist.
5. Verify standby: health, data, error rate, and user-facing checks.
6. Announce the failover, with RTO/RPO actually achieved.
7. Keep primary isolated until root cause is known — do not fail back blindly.
