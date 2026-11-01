#!/usr/bin/env python3
"""Generic team request tracker: read requests.csv, print a summary.
Sample data only. No real team data is included.
Usage: python3 tracker.py --report
"""
import argparse, csv, collections, sys
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--report", action="store_true")
    p.add_argument("--file", default=str(Path(__file__).parent / "requests.csv"))
    args = p.parse_args()
    rows = list(csv.DictReader(open(args.file)))
    by_status = collections.Counter(r.get("status", "") for r in rows)
    by_owner = collections.Counter(r.get("owner", "") for r in rows)
    print(f"Total requests: {len(rows)}")
    print("By status:")
    for k, v in by_status.items():
        print(f"  {k}: {v}")
    print("By owner:")
    for k, v in by_owner.items():
        print(f"  {k}: {v}")
    print("\nOpen requests:")
    for r in rows:
        if r.get("status") != "Closed":
            print(f"  - {r.get('id')} | {r.get('summary')} | owner: {r.get('owner')}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
