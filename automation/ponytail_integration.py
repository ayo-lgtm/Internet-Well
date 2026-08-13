#!/usr/bin/env python3
"""Governed Ponytail integration for Internet-Well."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

SOURCE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HOME = Path(os.environ.get("INTERNET_WELL_HOME", Path.home() / ".internet-well"))


class PonytailError(RuntimeError):
    pass


def resolve_manifest() -> Path:
    candidates: list[Path] = []
    configured_root = os.environ.get("INTERNET_WELL_ROOT")
    if configured_root:
        candidates.append(Path(configured_root).expanduser().resolve() / "integrations" / "vibe" / "ponytail.json")
    candidates.extend([
        SOURCE_ROOT / "integrations" / "vibe" / "ponytail.json",
        Path(sys.prefix) / "integrations" / "vibe" / "ponytail.json",
        Path(sys.base_prefix) / "integrations" / "vibe" / "ponytail.json",
    ])
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise PonytailError("Ponytail manifest not found. Set INTERNET_WELL_ROOT to an Internet-Well checkout.")


def load_manifest() -> dict[str, Any]:
    data = json.loads(resolve_manifest().read_text(encoding="utf-8"))
    if data.get("id") != "ponytail":
        raise PonytailError("Invalid Ponytail manifest.")
    return data


def validate_ref(ref: str) -> str:
    if not ref or any(ch.isspace() for ch in ref):
        raise PonytailError("An exact release tag or commit is required.")
    if ref.lower() in {"latest", "main", "master", "head", "*"}:
        raise PonytailError("Floating refs are not accepted. Use an exact release or commit.")
    return ref


def plan(ref: str, destination: Path | None = None) -> dict[str, Any]:
    item = load_manifest()
    ref = validate_ref(ref)
    dest = (destination or (DEFAULT_HOME / "sources" / "ponytail")).expanduser().resolve()
    return {
        "integration": item,
        "approved": False,
        "execution": "not-performed",
        "destination": str(dest),
        "planned_clone": ["git", "clone", "--filter=blob:none", "--no-checkout", item["source"], str(dest)],
        "planned_checkout": ["git", "-C", str(dest), "checkout", "--detach", ref],
        "adoption_rule": "Inspect and selectively adopt only approved skills or AGENTS.md rules; do not vendor the whole repository by default.",
        "required_review": item["quality_gates"],
        "restrictions": item["restrictions"],
    }


def run(command: list[str]) -> dict[str, Any]:
    proc = subprocess.run(command, text=True, capture_output=True, check=False, timeout=300)
    return {"command": command, "returncode": proc.returncode, "stdout": proc.stdout[-8000:], "stderr": proc.stderr[-8000:]}


def install(ref: str, destination: Path | None, approve: bool) -> dict[str, Any]:
    if not approve:
        raise PonytailError("Installation requires --approve after reviewing the plan.")
    if shutil.which("git") is None:
        raise PonytailError("git is required.")
    p = plan(ref, destination)
    dest = Path(p["destination"])
    if dest.exists():
        raise PonytailError(f"Destination already exists: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    clone = run(p["planned_clone"])
    if clone["returncode"] != 0:
        raise PonytailError(json.dumps(clone, indent=2))
    checkout = run(p["planned_checkout"])
    if checkout["returncode"] != 0:
        shutil.rmtree(dest, ignore_errors=True)
        raise PonytailError(json.dumps(checkout, indent=2))
    return {
        "integration": load_manifest(),
        "approved": True,
        "execution": "source-pinned",
        "destination": str(dest),
        "clone": clone,
        "checkout": checkout,
        "next_step": "Review the selected Ponytail skills and generated agent rules before copying them into any project.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-ponytail")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show")
    for name in ("plan", "install"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--ref", required=True, help="Exact release tag or commit.")
        cmd.add_argument("--destination", type=Path)
        if name == "install":
            cmd.add_argument("--approve", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "show":
            payload = load_manifest()
        elif args.command == "plan":
            payload = plan(args.ref, args.destination)
        else:
            payload = install(args.ref, args.destination, args.approve)
        print(json.dumps(payload, indent=2))
        return 0
    except (PonytailError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
