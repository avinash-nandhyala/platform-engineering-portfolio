#!/usr/bin/env python3
"""Drift report: compare desired apps vs. a supplied inventory (sample data).
Usage: python3 drift-report.py
"""
import json
from pathlib import Path
inv = json.loads((Path(__file__).parent / "sample-inventory.json").read_text())
print("Desired vs. actual (sample inventory):")
for app in inv["apps"]:
    status = "IN SYNC" if app["desired_version"] == app["actual_version"] else "DRIFT"
    print(f"  {app['cluster']}/{app['name']}: desired {app['desired_version']}, actual {app['actual_version']} -> {status}")
