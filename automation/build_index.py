#!/usr/bin/env python3
"""Generate registry/INDEX.md from record front matter.

  python3 automation/build_index.py          # rewrite INDEX.md
  python3 automation/build_index.py --check  # exit 1 if INDEX.md differs

The index is fully generated — never hand-edit it. This removes the
count-drift bug class the linter once caught in a hand-maintained index.
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_registry import parse_front_matter, REGISTRY, CATEGORIES  # noqa: E402

STATUS_ICON = {"approved": "✅", "approved-with-restrictions": "⚠️",
               "experimental": "🧪"}


def load_records():
    records = []
    for path in sorted(REGISTRY.glob("*/*.md")):
        rel = path.relative_to(REGISTRY).as_posix()
        fields, _ = parse_front_matter(path.read_text(encoding="utf-8"), rel)
        if fields:
            fields["_rel"] = rel
            records.append(fields)
    return records


def row(f):
    tested = {"true": "✅", "false": "–"}.get(f.get("tested"), "n/a")
    score = f.get("score", "")
    score = "n/a" if score in ("null", "", None) else score
    pin = f.get("pinned_version", "")
    pin = (pin[:38] + "…") if len(pin) > 39 else pin
    return (f"| [{f['name']}]({f['_rel']}) | {f['category']} | "
            f"{f['tier']} | {f.get('subcategory', '')} | {f['license']} | "
            f"{pin} | {score} | {tested} |")


def build():
    records = load_records()
    by_status = {}
    for f in records:
        by_status.setdefault(f["status"], []).append(f)
    tiers = {}
    for f in records:
        tiers[f["tier"]] = tiers.get(f["tier"], 0) + 1
    tested_count = sum(1 for f in records if f.get("tested") == "true")
    reviewed = sum(1 for f in records if f.get("human_reviewed") == "true")

    header = ["# Registry Index", "",
              "**GENERATED FILE — do not hand-edit.** Rebuild with "
              "`python3 automation/build_index.py`.", "",
              f"{len(records)} records as of "
              f"{dt.date.today().isoformat()} — "
              + ", ".join(f"{len(v)} {k}" for k, v in sorted(
                  by_status.items()))
              + f". Tiers: " + ", ".join(
                  f"{v}×{k}" for k, v in sorted(tiers.items()))
              + f". Execution-tested: {tested_count}. "
              f"Human-reviewed: {reviewed} (tier A requires human review — "
              "see METHODOLOGY §5a).", "",
              "Rejected candidates (tier D) are preserved with evidence in "
              "[rejected/README.md](../rejected/README.md); open "
              "verification debts in "
              "[evidence/RECHECK.md](../evidence/RECHECK.md); execution-"
              "test transcript in "
              "[evaluations/README.md](../evaluations/README.md).", ""]

    cols = ("| Name | Category | Tier | Function | License | Pinned | "
            "Score | Tested |\n|---|---|---|---|---|---|---|---|")
    body = []
    for status in ("approved", "approved-with-restrictions", "experimental"):
        if status not in by_status:
            continue
        body.append(f"## {STATUS_ICON[status]} {status} "
                    f"({len(by_status[status])})")
        body.append("")
        body.append(cols)
        for f in sorted(by_status[status],
                        key=lambda x: (x["category"], x["name"].lower())):
            body.append(row(f))
        body.append("")

    coverage = ["## Coverage", "",
                "| Category | Records |", "|---|---|"]
    counts = {}
    for f in records:
        counts[f["category"]] = counts.get(f["category"], 0) + 1
    for cat in sorted(CATEGORIES):
        coverage.append(f"| {cat} | {counts.get(cat, 0)} |")
    coverage += ["",
                 "Known thin spots, held open honestly (see "
                 "[PHASES.md](../PHASES.md)): PRD templates with real "
                 "provenance, customer-success playbooks, keyword/rank "
                 "tooling, forecasting beyond hledger budgets + Metabase.",
                 ""]

    return "\n".join(header + body + coverage)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    out = REGISTRY / "INDEX.md"
    content = build()
    if args.check:
        if out.read_text(encoding="utf-8") != content:
            print("INDEX.md is out of date — run automation/build_index.py")
            sys.exit(1)
        print("INDEX.md up to date")
        return
    out.write_text(content, encoding="utf-8")
    print(f"wrote {out} ({len(content.splitlines())} lines)")


if __name__ == "__main__":
    main()
