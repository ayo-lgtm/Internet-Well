#!/usr/bin/env python3
"""Report deep-research catalog coverage by validated registry records.

This script is intentionally dependency-free. It does not promote resources or
change evidence. It produces a machine-readable view of which catalog entries
have a registry record and which remain candidate-only.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "curated-repositories.json"
REGISTRY = ROOT / "registry"
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    result: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def registry_by_repo() -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in sorted(REGISTRY.rglob("*.md")):
        data = parse_front_matter(path)
        repo = data.get("canonical_repo", "")
        if not repo.startswith("https://github.com/"):
            continue
        slug = repo.removeprefix("https://github.com/").rstrip("/")
        records[slug.lower()] = {
            "path": str(path.relative_to(ROOT)),
            "status": data.get("status", "unknown"),
            "tier": data.get("tier", "unknown"),
            "tested": data.get("tested", "unknown"),
            "last_verified": data.get("last_verified", "unknown"),
            "pinned_version": data.get("pinned_version", "unknown"),
            "human_reviewed": data.get("human_reviewed", "unknown"),
        }
    return records


def build_report() -> dict[str, Any]:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    candidates = catalog.get("repositories", [])
    registry = registry_by_repo()
    entries: list[dict[str, Any]] = []

    for candidate in candidates:
        slug = str(candidate.get("slug", "")).strip()
        record = registry.get(slug.lower())
        if record:
            disposition = "registry-record"
            if record["status"] == "rejected":
                disposition = "rejected"
            elif record["status"] == "experimental":
                disposition = "experimental"
            elif record["status"] in {"approved", "approved-with-restrictions"}:
                disposition = "promoted"
        else:
            disposition = "candidate-only"

        entries.append(
            {
                "slug": slug,
                "name": candidate.get("name"),
                "role": candidate.get("role"),
                "catalog_readiness": candidate.get("readiness"),
                "catalog_risk": candidate.get("risk"),
                "disposition": disposition,
                "registry": record,
            }
        )

    counts: dict[str, int] = {}
    for entry in entries:
        counts[entry["disposition"]] = counts.get(entry["disposition"], 0) + 1

    return {
        "catalog_generated_at": catalog.get("generated_at"),
        "catalog_count": len(entries),
        "counts": dict(sorted(counts.items())),
        "entries": entries,
    }


def validate(report: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for entry in report["entries"]:
        slug = entry["slug"].lower()
        if not slug or "/" not in slug:
            errors.append(f"invalid catalog slug: {entry['slug']!r}")
        if slug in seen:
            errors.append(f"duplicate catalog slug: {entry['slug']}")
        seen.add(slug)
        record = entry.get("registry")
        if record and record.get("status") in {"approved", "approved-with-restrictions"}:
            if record.get("pinned_version") in {"", "unknown", None}:
                errors.append(f"promoted record lacks pin: {entry['slug']}")
            if record.get("last_verified") in {"", "unknown", None}:
                errors.append(f"promoted record lacks verification date: {entry['slug']}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    report = build_report()
    errors = validate(report)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")

    if args.check and errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
