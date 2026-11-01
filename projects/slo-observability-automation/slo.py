#!/usr/bin/env python3
"""SLO error-budget calculator with burn-rate helpers. Tested.
Usage: python3 slo.py --test
       python3 slo.py --slo 99.9 --window-days 30
       python3 slo.py --slo 99.9 --window-days 30 --burn-rate 14
"""
import argparse, sys

def error_budget_minutes(slo_percent, window_days):
    allowed_error = 1 - slo_percent / 100.0
    return allowed_error * window_days * 24 * 60

def burn_rate(error_rate_percent, slo_percent):
    allowed = 1 - slo_percent / 100.0
    if allowed == 0:
        return float("inf")
    return (error_rate_percent / 100.0) / allowed

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--test", action="store_true")
    p.add_argument("--slo", type=float, default=99.9)
    p.add_argument("--window-days", type=int, default=30)
    p.add_argument("--burn-rate", type=float, default=None)
    p.add_argument("--error-rate", type=float, default=None)
    args = p.parse_args()
    if args.test:
        # 99.9% over 30 days = 0.1% * 43200 min = 43.2 min
        assert abs(error_budget_minutes(99.9, 30) - 43.2) < 0.01
        assert abs(error_budget_minutes(99.0, 30) - 432.0) < 0.01
        assert abs(burn_rate(1.4, 99.9) - 14.0) < 0.01
        print("slo self-test: PASS")
        return 0
    budget = error_budget_minutes(args.slo, args.window_days)
    print(f"SLO {args.slo}% over {args.window_days} days -> error budget: {budget:.1f} minutes")
    if args.error_rate is not None:
        br = burn_rate(args.error_rate, args.slo)
        print(f"Current error rate {args.error_rate}% -> burn rate {br:.1f}x")
        if br >= 14:
            print("Action: PAGE — burning budget 14x faster than sustainable (fast burn).")
        elif br >= 2:
            print("Action: TICKET — burning budget 2x faster than sustainable (slow burn).")
        else:
            print("Action: none — burn rate within budget.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
