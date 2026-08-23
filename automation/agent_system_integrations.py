#!/usr/bin/env python3
"""Governed adapters for autonomous agent-system repositories."""
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
RESTRICTED = {"qwen38-uncensored"}


class IntegrationError(RuntimeError):
    pass


def resolve_manifest() -> Path:
    roots = []
    configured = os.environ.get("INTERNET_WELL_ROOT")
    if configured:
        roots.append(Path(configured).expanduser().resolve())
    roots.extend([SOURCE_ROOT, Path(sys.prefix), Path(sys.base_prefix)])
    for root in roots:
        candidate = root / "integrations" / "agent-systems" / "wassim-agent-systems.json"
        if candidate.is_file():
            return candidate
    raise IntegrationError("Unable to locate integrations/agent-systems/wassim-agent-systems.json")


def load_manifest() -> dict[str, Any]:
    data = json.loads(resolve_manifest().read_text(encoding="utf-8"))
    items = data.get("integrations")
    if not isinstance(items, list) or not items:
        raise IntegrationError("Agent-system integration manifest is empty or invalid.")
    return data


def find(integration_id: str) -> dict[str, Any]:
    for item in load_manifest()["integrations"]:
        if item["id"] == integration_id:
            return item
    raise IntegrationError(f"Unknown integration: {integration_id}")


def exact_pin(item: dict[str, Any], requested: str | None) -> str:
    ref = requested or item.get("pin")
    if not ref or ref.lower() in {"latest", "main", "master", "head", "*"} or any(c.isspace() for c in ref):
        raise IntegrationError("An immutable commit or exact release pin is required.")
    return ref


def summary(item: dict[str, Any]) -> dict[str, Any]:
    return {k: item.get(k) for k in ("id", "kind", "source", "pin", "license", "risk", "install_mode", "recommended_for", "capabilities")}


def plan(item: dict[str, Any], ref: str | None, destination: Path | None) -> dict[str, Any]:
    pin = exact_pin(item, ref)
    restricted = item["id"] in RESTRICTED or item.get("install_mode") == "reference-only"
    payload: dict[str, Any] = {
        "integration": summary(item),
        "pin": pin,
        "execution": "not-performed",
        "restricted": restricted,
        "required_review": [
            "verify upstream source and immutable pin",
            "review license, scripts, dependencies, hooks, network behavior, and permissions",
            "test in an isolated fixture",
            "define rollback and stop conditions",
            "compare against a no-integration baseline",
        ],
    }
    if restricted:
        payload["decision"] = "reference-only"
        payload["restriction"] = "Internet-Well does not install or execute this resource. Authorized adversarial/safety evaluation only."
        return payload
    dest = (destination or (DEFAULT_HOME / "sources" / item["id"])).expanduser().resolve()
    payload["planned_clone"] = ["git", "clone", "--filter=blob:none", "--no-checkout", item["source"], str(dest)]
    payload["planned_checkout"] = ["git", "-C", str(dest), "checkout", "--detach", pin]
    payload["destination"] = str(dest)
    return payload


def run(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, text=True, capture_output=True, timeout=300, check=False)
    return {"command": cmd, "returncode": proc.returncode, "stdout": proc.stdout[-6000:], "stderr": proc.stderr[-6000:]}


def install(item: dict[str, Any], ref: str | None, destination: Path | None, approve: bool) -> dict[str, Any]:
    if item["id"] in RESTRICTED or item.get("install_mode") == "reference-only":
        raise IntegrationError("Restricted adversarial resources are reference-only and cannot be installed by Internet-Well.")
    if not approve:
        raise IntegrationError("Installation requires --approve after reviewing the plan.")
    if shutil.which("git") is None:
        raise IntegrationError("git is required.")
    pin = exact_pin(item, ref)
    dest = (destination or (DEFAULT_HOME / "sources" / item["id"])).expanduser().resolve()
    if dest.exists():
        raise IntegrationError(f"Destination already exists: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    clone = run(["git", "clone", "--filter=blob:none", "--no-checkout", item["source"], str(dest)])
    if clone["returncode"] != 0:
        raise IntegrationError(json.dumps(clone, indent=2))
    checkout = run(["git", "-C", str(dest), "checkout", "--detach", pin])
    if checkout["returncode"] != 0:
        shutil.rmtree(dest, ignore_errors=True)
        raise IntegrationError(json.dumps(checkout, indent=2))
    return {
        "integration": summary(item),
        "execution": "source-pinned",
        "destination": str(dest),
        "clone": clone,
        "checkout": checkout,
        "next_step": "Inspect and selectively wire the approved capability. Do not grant production credentials or live-trading authority by default.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-agent-systems")
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("list")
    show = subs.add_parser("show")
    show.add_argument("integration_id")
    for name in ("plan", "install"):
        p = subs.add_parser(name)
        p.add_argument("integration_id")
        p.add_argument("--ref")
        p.add_argument("--destination", type=Path)
        if name == "install":
            p.add_argument("--approve", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "list":
            payload: Any = [summary(x) for x in load_manifest()["integrations"]]
        else:
            item = find(args.integration_id)
            if args.command == "show":
                payload = item
            elif args.command == "plan":
                payload = plan(item, args.ref, args.destination)
            else:
                payload = install(item, args.ref, args.destination, args.approve)
        print(json.dumps(payload, indent=2))
        return 0
    except (IntegrationError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
