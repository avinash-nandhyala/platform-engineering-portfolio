#!/usr/bin/env python3
"""RTO / RPO calculator.

RTO = maximum time to restore. RPO = maximum data loss, in minutes.
Given a measured restore time and data lag, does it meet the tier?
"""
import argparse
import sys

TIERS = {
    "critical": (15, 5),
    "standard": (60, 60),
    "best-effort": (1440, 1440),
}


def meets_tier(restore_minutes, data_lag_minutes, tier):
    rto, rpo = TIERS[tier]
    return restore_minutes <= rto and data_lag_minutes <= rpo


def main():
    parser = argparse.ArgumentParser(description="RTO / RPO calculator")
    parser.add_argument("--restore-minutes", type=float, default=0)
    parser.add_argument("--data-lag-minutes", type=float, default=0)
    parser.add_argument("--tier", default="critical", choices=TIERS)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        assert meets_tier(12, 4, "critical") is True
        assert meets_tier(20, 4, "critical") is False  # RTO breached
        assert meets_tier(12, 10, "critical") is False  # RPO breached
        assert meets_tier(50, 50, "standard") is True
        print("rto tests: PASS (4/4)")
        return 0

    ok = meets_tier(args.restore_minutes, args.data_lag_minutes, args.tier)
    rto, rpo = TIERS[args.tier]
    print(f"Tier {args.tier}: RTO {rto}m, RPO {rpo}m")
    print(f"Measured: restore {args.restore_minutes}m, "
          f"data lag {args.data_lag_minutes}m")
    print(f"Result: {'MEETS tier' if ok else 'BREACHES tier'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
