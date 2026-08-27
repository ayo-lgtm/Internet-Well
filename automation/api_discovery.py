#!/usr/bin/env python3
"""Governed discovery adapter for public-apis/public-apis."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

SOURCE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HOME = Path(os.environ.get("INTERNET_WELL_HOME", Path.home() / ".internet-well"))


class DiscoveryError(RuntimeError):
    pass


def resolve_manifest() -> Path:
    roots = []
    configured = os.environ.get("INTERNET_WELL_ROOT")
    if configured:
        roots.append(Path(configured).expanduser().resolve())
    roots.extend([SOURCE_ROOT, Path(sys.prefix), Path(sys.base_prefix)])
    for root in roots:
        candidate = root / "integrations" / "api-discovery" / "public-apis.json"
        if candidate.is_file():
            return candidate
    raise DiscoveryError("Unable to locate integrations/api-discovery/public-apis.json")


def manifest() -> dict[str, Any]:
    data = json.loads(resolve_manifest().read_text(encoding="utf-8"))
    pin = data.get("pin", "")
    if not re.fullmatch(r"[0-9a-f]{40}", pin):
        raise DiscoveryError("Public APIs source must be pinned to an immutable 40-character commit SHA.")
    return data


def source_dir() -> Path:
    return (DEFAULT_HOME / "sources" / "public-apis").expanduser().resolve()


def run(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, text=True, capture_output=True, timeout=300, check=False)
    return {"command": cmd, "returncode": proc.returncode, "stdout": proc.stdout[-4000:], "stderr": proc.stderr[-4000:]}


def install(approve: bool, destination: Path | None) -> dict[str, Any]:
    if not approve:
        raise DiscoveryError("Source checkout requires --approve after reviewing the discovery policy.")
    if shutil.which("git") is None:
        raise DiscoveryError("git is required.")
    cfg = manifest()
    dest = (destination or source_dir()).expanduser().resolve()
    if dest.exists():
        raise DiscoveryError(f"Destination already exists: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    clone = run(["git", "clone", "--filter=blob:none", "--no-checkout", cfg["source"], str(dest)])
    if clone["returncode"] != 0:
        raise DiscoveryError(json.dumps(clone, indent=2))
    checkout = run(["git", "-C", str(dest), "checkout", "--detach", cfg["pin"]])
    if checkout["returncode"] != 0:
        shutil.rmtree(dest, ignore_errors=True)
        raise DiscoveryError(json.dumps(checkout, indent=2))
    return {"execution": "source-pinned", "destination": str(dest), "pin": cfg["pin"], "api_calls_performed": False}


def strip_md(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", value)
    return match.group(1).strip() if match else value.strip()


def url_from(value: str) -> str | None:
    match = re.search(r"\[[^\]]+\]\((https?://[^)]+)\)", value)
    return match.group(1).strip() if match else None


def parse_catalog(readme: Path) -> list[dict[str, str | None]]:
    if not readme.is_file():
        raise DiscoveryError(f"Catalog not found: {readme}")
    category = "Uncategorized"
    rows: list[dict[str, str | None]] = []
    for raw in readme.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("### "):
            category = line[4:].strip()
            continue
        if not (line.startswith("|") and line.endswith("|")):
            continue
        cells = [x.strip() for x in line.strip("|").split("|")]
        if len(cells) != 5 or cells[0] in {"API", ":---"} or set(cells[0]) <= {"-", ":"}:
            continue
        rows.append({
            "name": strip_md(cells[0]),
            "url": url_from(cells[0]),
            "description": strip_md(cells[1]),
            "auth": strip_md(cells[2]),
            "https": strip_md(cells[3]),
            "cors": strip_md(cells[4]),
            "category": category,
        })
    return rows


def discover(query: str, catalog: Path, limit: int) -> list[dict[str, Any]]:
    q = query.casefold().strip()
    if not q:
        raise DiscoveryError("A non-empty discovery query is required.")
    matches = []
    for row in parse_catalog(catalog):
        haystack = " ".join(str(row.get(k) or "") for k in ("name", "description", "category")).casefold()
        if q not in haystack:
            continue
        https = (row.get("https") or "").casefold() == "yes"
        auth = (row.get("auth") or "").casefold()
        score = (2 if https else 0) + (1 if auth in {"no", "", "none"} else 0)
        matches.append({**row, "discovery_score": score, "status": "candidate-only", "requires_provider_verification": True})
    matches.sort(key=lambda x: (-x["discovery_score"], str(x["name"]).casefold()))
    return matches[:limit]


def use_plan(name: str) -> dict[str, Any]:
    cfg = manifest()
    return {
        "candidate": name,
        "source_catalog": cfg["repository"],
        "source_pin": cfg["pin"],
        "approval": "not-granted",
        "api_call": "not-performed",
        "required_before_use": cfg["required_checks_before_use"],
        "hard_rules": [
            "Use only credentials issued to or explicitly authorized for the user/project.",
            "Never use leaked, copied, shared, or third-party credentials to avoid provider charges or quotas.",
            "A catalog listing is discovery evidence, not proof of safety, legality, availability, or free/unlimited access.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-api-discovery")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show")
    inst = sub.add_parser("install-source")
    inst.add_argument("--destination", type=Path)
    inst.add_argument("--approve", action="store_true")
    find = sub.add_parser("find")
    find.add_argument("query")
    find.add_argument("--catalog", type=Path)
    find.add_argument("--limit", type=int, default=10)
    plan = sub.add_parser("plan-use")
    plan.add_argument("name")
    args = parser.parse_args()
    try:
        if args.command == "show":
            payload: Any = manifest()
        elif args.command == "install-source":
            payload = install(args.approve, args.destination)
        elif args.command == "find":
            catalog = args.catalog or (source_dir() / manifest()["upstream_catalog"])
            payload = discover(args.query, catalog.expanduser().resolve(), max(1, min(args.limit, 100)))
        else:
            payload = use_plan(args.name)
        print(json.dumps(payload, indent=2))
        return 0
    except (DiscoveryError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
