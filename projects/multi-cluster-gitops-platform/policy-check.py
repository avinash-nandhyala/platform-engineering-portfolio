#!/usr/bin/env python3
"""Policy check for Kubernetes manifests: fail on privileged containers or missing limits.
Usage: python3 policy-check.py --test   (runs built-in self-test, no cluster needed)
       python3 policy-check.py <manifest.yaml>
"""
import sys, yaml

def check(doc):
    errors = []
    if not isinstance(doc, dict):
        return errors
    spec = doc.get("spec", {})
    template = spec.get("template", {}).get("spec", {}) if "template" in spec else spec
    for c in template.get("containers", []):
        name = c.get("name", "?")
        sc = c.get("securityContext", {}) or {}
        if sc.get("privileged"):
            errors.append(f"{name}: privileged container is not allowed")
        res = c.get("resources", {}) or {}
        if not res.get("limits"):
            errors.append(f"{name}: missing resource limits")
        if not res.get("requests"):
            errors.append(f"{name}: missing resource requests")
    return errors

def main():
    if "--test" in sys.argv:
        good = {"spec": {"template": {"spec": {"containers": [{"name": "app", "resources": {"limits": {"cpu": "500m"}, "requests": {"cpu": "250m"}}}]}}}}
        bad = {"spec": {"template": {"spec": {"containers": [{"name": "app", "securityContext": {"privileged": True}}]}}}}
        assert check(good) == [], check(good)
        assert len(check(bad)) >= 2, check(bad)
        print("policy-check self-test: PASS")
        return 0
    if len(sys.argv) < 2:
        print("Usage: python3 policy-check.py <manifest.yaml>  or  --test")
        return 1
    docs = list(yaml.safe_load_all(open(sys.argv[1])))
    all_errors = []
    for d in docs:
        all_errors.extend(check(d))
    if all_errors:
        print("POLICY FAIL:")
        for e in all_errors:
            print(f"  - {e}")
        return 1
    print("POLICY PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
