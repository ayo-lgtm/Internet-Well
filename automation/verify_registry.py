#!/usr/bin/env python3
"""Registry consistency linter, tier-rule enforcer, and staleness reporter.

Implements the continuous-verification loop from PHASES.md:

  python3 automation/verify_registry.py [--max-age DAYS] [--json]

Checks every record under registry/<category>/*.md for:
  - parseable flat YAML front matter (contract: schemas/record-schema.md)
  - required fields
  - valid status, confidence, tier values; category matches directory
  - tier rules:
      * A requires status=approved, tested=true, confidence=high,
        human_reviewed=true — always
      * records in SENSITIVE categories (security, legal-compliance,
        finance) can never be A without human_reviewed=true (subsumed by
        the rule above; kept explicit so future rule relaxations cannot
        silently drop it)
      * experimental status must be tier C
      * tier D never appears under registry/ (rejections live in
        rejected/README.md)
  - last_verified recency against --max-age (default 90 days)
  - INDEX.md cross-reference (every record linked, no dead links)

Exit codes: 0 clean · 1 schema/consistency errors · 2 stale entries only.
No third-party dependencies (Python 3.9+).
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry"

REQUIRED = ["name", "category", "status", "tier", "human_reviewed", "type",
            "license", "confidence", "last_verified"]
STATUSES = {"approved", "approved-with-restrictions", "experimental",
            "rejected", "recheck-required"}
CONFIDENCE = {"high", "medium", "low"}
TIERS = {"A", "B", "C"}  # D lives only in rejected/README.md
CATEGORIES = {"engineering", "security", "product", "design",
              "legal-compliance", "marketing", "finance", "operations",
              "launch-maintenance"}
SENSITIVE = {"security", "legal-compliance", "finance"}


def parse_front_matter(text, path):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, [f"{path}: missing front matter"]
    fields, errors = {}, []
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith("#") or line.startswith(" "):
            continue
        if ":" not in line:
            errors.append(f"{path}: unparseable line {line!r}")
            continue
        k, v = line.split(":", 1)
        v = v.split(" #", 1)[0].strip().strip('"')
        fields[k.strip()] = v
    return fields, errors


def check_tier(rel, f, errors):
    tier = f.get("tier", "")
    if tier not in TIERS:
        errors.append(f"{rel}: invalid tier {tier!r} (A/B/C in registry/)")
        return
    status = f.get("status")
    reviewed = f.get("human_reviewed") == "true"
    if tier == "A":
        if not (status == "approved" and f.get("tested") == "true"
                and f.get("confidence") == "high" and reviewed):
            errors.append(
                f"{rel}: tier A requires approved + tested + high "
                f"confidence + human_reviewed=true")
        if f.get("category") in SENSITIVE and not reviewed:
            errors.append(
                f"{rel}: sensitive category cannot be tier A without "
                f"human review")
    if status == "experimental" and tier != "C":
        errors.append(f"{rel}: experimental records must be tier C")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-age", type=int, default=90)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    records = sorted(REGISTRY.glob("*/*.md"))
    index_text = (REGISTRY / "INDEX.md").read_text(encoding="utf-8")
    today = dt.date.today()
    errors, stale = [], []
    stats, tiers = {}, {}

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
        if fields.get("status") not in STATUSES:
            errors.append(f"{rel}: invalid status {fields.get('status')!r}")
        if fields.get("confidence") not in CONFIDENCE:
            errors.append(
                f"{rel}: invalid confidence {fields.get('confidence')!r}")
        if fields.get("category") != path.parent.name:
            errors.append(
                f"{rel}: category {fields.get('category')!r} != directory "
                f"{path.parent.name!r}")
        if path.parent.name not in CATEGORIES:
            errors.append(f"{rel}: unknown category dir {path.parent.name}")
        check_tier(rel, fields, errors)
        lv = fields.get("last_verified", "")
        try:
            age = (today - dt.date.fromisoformat(lv)).days
            if age > args.max_age:
                stale.append(f"{rel}: last_verified {lv} ({age}d old)")
        except ValueError:
            errors.append(f"{rel}: bad last_verified {lv!r}")
        if rel not in index_text:
            errors.append(f"{rel}: not linked from INDEX.md")
        stats[fields.get("status")] = stats.get(fields.get("status"), 0) + 1
        tiers[fields.get("tier")] = tiers.get(fields.get("tier"), 0) + 1

    for link in re.findall(r"\]\((\w[\w./-]+\.md)\)", index_text):
        if link.startswith(".."):
            continue
        if not (REGISTRY / link).exists():
            errors.append(f"INDEX.md: dead link {link}")

    report = {"records": len(records), "by_status": stats,
              "by_tier": tiers, "errors": errors, "stale": stale,
              "max_age_days": args.max_age, "run_date": today.isoformat()}
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{len(records)} records — {stats} — tiers {tiers}")
        for e in errors:
            print(f"ERROR: {e}")
        for s in stale:
            print(f"STALE: {s}")
        if not errors and not stale:
            print("OK: registry consistent, tier rules hold, nothing stale")
    sys.exit(1 if errors else (2 if stale else 0))


if __name__ == "__main__":
    main()
