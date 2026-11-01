#!/usr/bin/env python3
"""Incident memory search — generic prototype.
Usage: python3 incident-memory.py "search terms"
Searches notes/*.md for matching terms and prints the best matches.
"""
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 incident-memory.py "search terms"')
        return 1
    query = " ".join(sys.argv[1:]).lower()
    terms = query.split()
    notes_dir = Path(__file__).parent / "notes"
    results = []
    for f in sorted(notes_dir.glob("*.md")):
        text = f.read_text()
        score = sum(text.lower().count(t) for t in terms)
        if score:
            results.append((score, f.name, text))
    results.sort(reverse=True)
    if not results:
        print("No past incident matched. Log this one once it is fixed, so the next person finds it.")
        return 0
    for score, name, text in results:
        print(f"--- {name} (score {score}) ---")
        print(text[:1200])
        print()
    return 0

if __name__ == "__main__":
    sys.exit(main())
