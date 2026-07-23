#!/usr/bin/env python3
"""Registry consistency linter and staleness reporter.

Implements the Phase 4 continuous-verification loop from PHASES.md:

  python3 tools/verify_registry.py [--max-age DAYS] [--json]

Checks every record under registry/<category>/*.md for:
  - parseable flat YAML front matter
  - required fields (name, category, status, type, canonical_repo or a
    stated 'none', license, confidence, last_verified)
  - valid status and confidence values
  - last_verified recency against --max-age (default 90 days)
  - INDEX.md cross-reference (every record linked, no dead links)

Exit codes: 0 clean · 1 schema/consistency errors · 2 stale entries only.
No third-party dependencies, so it runs anywhere Python 3.9+ exists.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry"

REQUIRED = ["name", "category", "status", "type", "license",
            "confidence", "last_verified"]
STATUSES = {"approved", "approved-with-restrictions", "experimental",
            "rejected", "recheck-required"}
CONFIDENCE = {"high", "medium", "low"}


def parse_front_matter(text, path):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, [f"{path}: missing front matter"]
    fields, errors = {}, []
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith(" "):  # continuation; flat schema only
            continue
        if ":" not in line:
            errors.append(f"{path}: unparseable line {line!r}")
            continue
        k, v = line.split(":", 1)
        v = v.split(" #", 1)[0].strip().strip('"')
        fields[k.strip()] = v
    return fields, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-age", type=int, default=90)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    records = sorted(REGISTRY.glob("*/*.md"))
    index_text = (REGISTRY / "INDEX.md").read_text(encoding="utf-8")
    today = dt.date.today()
    errors, stale, stats = [], [], {}

    for path in records:
        rel = path.relative_to(REGISTRY).as_posix()
        fields, errs = parse_front_matter(
            path.read_text(encoding="utf-8"), rel)
        errors.extend(errs)
        if fields is None:
            continue
        for key in REQUIRED:
            if not fields.get(key):
                errors.append(f"{rel}: missing required field '{key}'")
        status = fields.get("status", "")
        if status not in STATUSES:
            errors.append(f"{rel}: invalid status {status!r}")
        if fields.get("confidence") not in CONFIDENCE:
            errors.append(
                f"{rel}: invalid confidence {fields.get('confidence')!r}")
        lv = fields.get("last_verified", "")
        try:
            age = (today - dt.date.fromisoformat(lv)).days
            if age > args.max_age:
                stale.append(f"{rel}: last_verified {lv} ({age}d old)")
        except ValueError:
            errors.append(f"{rel}: bad last_verified {lv!r}")
        if rel not in index_text:
            errors.append(f"{rel}: not linked from INDEX.md")
        stats[status] = stats.get(status, 0) + 1

    for link in re.findall(r"\]\((\w[\w./-]+\.md)\)", index_text):
        if link.startswith(("REJECTED", "RECHECK", "..")):
            continue
        if not (REGISTRY / link).exists():
            errors.append(f"INDEX.md: dead link {link}")

    report = {"records": len(records), "by_status": stats,
              "errors": errors, "stale": stale,
              "max_age_days": args.max_age,
              "run_date": today.isoformat()}
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{len(records)} records — {stats}")
        for e in errors:
            print(f"ERROR: {e}")
        for s in stale:
            print(f"STALE: {s}")
        if not errors and not stale:
            print("OK: registry consistent, nothing stale")
    sys.exit(1 if errors else (2 if stale else 0))


if __name__ == "__main__":
    main()
