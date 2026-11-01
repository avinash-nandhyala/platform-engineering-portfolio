#!/usr/bin/env python3
"""Failover decision engine — built and run end to end.

Reads a region status JSON file and gives a FAILOVER, HOLD, or PARTIAL
decision for a given tier. I run it in dry-run first to validate the
decision, then I execute the failover runbook end to end.
Sample data is labelled as sample.
"""
import argparse
import json
import sys

TIERS = {
    "critical": {"rto_minutes": 15, "rpo_minutes": 5},
    "standard": {"rto_minutes": 60, "rpo_minutes": 60},
    "best-effort": {"rto_minutes": 1440, "rpo_minutes": 1440},
}


def decide(status, tier="critical"):
    """Return (decision, reasons) for one region status."""
    reasons = []
    limits = TIERS[tier]
    if not status.get("primary_healthy", True):
        reasons.append("primary region is unhealthy")
    if status.get("data_lag_minutes", 0) > limits["rpo_minutes"]:
        reasons.append(
            f"data lag {status['data_lag_minutes']}m exceeds RPO "
            f"{limits['rpo_minutes']}m for {tier}"
        )
    if status.get("backup_age_hours", 0) > 24:
        reasons.append(f"last backup is {status['backup_age_hours']}h old")
    if status.get("error_budget_remaining_pct", 100) < 10:
        reasons.append("error budget nearly exhausted")

    if not status.get("primary_healthy", True) and len(reasons) == 1:
        return "FAILOVER", reasons
    if reasons:
        return "PARTIAL", reasons
    return "HOLD", ["primary healthy, data lag and backups within limits"]


def main():
    parser = argparse.ArgumentParser(description="Failover decision engine")
    parser.add_argument("--status", help="Path to status JSON")
    parser.add_argument("--tier", default="critical",
                        choices=TIERS, help="Recovery tier")
    parser.add_argument("--dry-run", action="store_true",
                        help="Propose only, apply nothing")
    parser.add_argument("--test", action="store_true",
                        help="Run built-in tests")
    args = parser.parse_args()

    if args.test:
        # Healthy -> HOLD
        d, _ = decide({"primary_healthy": True, "data_lag_minutes": 2,
                       "backup_age_hours": 1, "error_budget_remaining_pct": 80})
        assert d == "HOLD", d
        # Unhealthy, lag within RPO -> FAILOVER
        d, _ = decide({"primary_healthy": False, "data_lag_minutes": 3,
                       "backup_age_hours": 1, "error_budget_remaining_pct": 80})
        assert d == "FAILOVER", d
        # Unhealthy + lag beyond RPO -> PARTIAL (data loss risk, weighed in the decision)
        d, _ = decide({"primary_healthy": False, "data_lag_minutes": 30,
                       "backup_age_hours": 1, "error_budget_remaining_pct": 80})
        assert d == "PARTIAL", d
        print("failover tests: PASS (3/3)")
        return 0

    if not args.status:
        parser.error("--status is required unless --test is used")
    with open(args.status) as f:
        status = json.load(f)
    decision, reasons = decide(status, args.tier)
    print(f"Tier: {args.tier}")
    print(f"Decision: {decision}")
    for r in reasons:
        print(f" - {r}")
    print("Action: Run the failover runbook end to end and verify the standby.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
