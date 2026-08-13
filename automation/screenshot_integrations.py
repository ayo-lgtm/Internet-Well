#!/usr/bin/env python3
"""Controlled adapters for screenshot-discovered Internet-Well resources."""
from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

SOURCE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HOME = Path(os.environ.get("INTERNET_WELL_HOME", Path.home() / ".internet-well"))


class IntegrationError(RuntimeError):
    pass


def resolve_manifest() -> Path:
    configured_root = os.environ.get("INTERNET_WELL_ROOT")
    candidates: list[Path] = []
    if configured_root:
        candidates.append(Path(configured_root).expanduser().resolve() / "integrations" / "vibe" / "screenshot-resources.json")
    candidates.extend([
        SOURCE_ROOT / "integrations" / "vibe" / "screenshot-resources.json",
        Path(sys.prefix) / "integrations" / "vibe" / "screenshot-resources.json",
        Path(sys.base_prefix) / "integrations" / "vibe" / "screenshot-resources.json",
    ])
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise IntegrationError("Unable to locate integrations/vibe/screenshot-resources.json. Set INTERNET_WELL_ROOT to a verified checkout.")


def load_manifest() -> dict[str, Any]:
    data = json.loads(resolve_manifest().read_text(encoding="utf-8"))
    integrations = data.get("integrations")
    if not isinstance(integrations, list) or not integrations:
        raise IntegrationError("Screenshot integration manifest is empty or invalid.")
    return data


def find_integration(integration_id: str) -> dict[str, Any]:
    for item in load_manifest()["integrations"]:
        if item["id"] == integration_id:
            return item
    raise IntegrationError(f"Unknown integration: {integration_id}")


def validate_ref(ref: str) -> str:
    if not ref or any(ch.isspace() for ch in ref):
        raise IntegrationError("A non-empty exact version, tag, or commit pin is required.")
    if ref.lower() in {"latest", "main", "master", "head", "*"}:
        raise IntegrationError("Floating refs are prohibited. Use an exact release or commit.")
    return ref


def summary(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item["id"],
        "name": item["name"],
        "kind": item["kind"],
        "source": item["source"],
        "install_mode": item["install_mode"],
        "pin_required": item.get("pin_required", False),
        "approval_required": item.get("approval_required", True),
        "capabilities": item.get("capabilities", []),
        "targets": item.get("targets", []),
        "notes": item.get("notes", ""),
    }


def render_command(item: dict[str, Any], ref: str) -> list[str]:
    template = item.get("command_template")
    if not template:
        raise IntegrationError(f"{item['id']} does not define a direct command adapter.")
    return [str(part).format(source=item["source"], ref=ref) for part in template]


def plan(item: dict[str, Any], ref: str, destination: Path | None = None) -> dict[str, Any]:
    ref = validate_ref(ref)
    result: dict[str, Any] = {
        "integration": summary(item),
        "approved": False,
        "execution": "not-performed",
        "required_review": [
            "confirm upstream source identity",
            "confirm exact pin",
            "review license and redistribution terms",
            "inspect scripts, hooks, binaries, dependencies, permissions, and network behavior",
            "test in an isolated fixture",
            "compare against a no-integration baseline",
            "record rollback instructions",
        ],
    }
    mode = item["install_mode"]
    if mode == "selective-copy":
        dest = destination or (DEFAULT_HOME / "sources" / item["id"])
        result["planned_clone"] = ["git", "clone", "--filter=blob:none", "--no-checkout", item["source"], str(dest)]
        result["planned_checkout"] = ["git", "-C", str(dest), "checkout", "--detach", ref]
        result["post_clone_rule"] = "Inspect selected skills and linked upstream sources; copy only individually approved directories."
        result["destination"] = str(dest)
    elif mode == "npx":
        cmd = render_command(item, ref)
        result["planned_command"] = cmd
        result["planned_command_shell"] = shlex.join(cmd)
    else:
        raise IntegrationError(f"Unsupported install mode: {mode}")
    return result


def run(command: list[str]) -> dict[str, Any]:
    proc = subprocess.run(command, text=True, capture_output=True, check=False, timeout=300)
    return {"command": command, "returncode": proc.returncode, "stdout": proc.stdout[-8000:], "stderr": proc.stderr[-8000:]}


def execute(item: dict[str, Any], ref: str, destination: Path | None, approve: bool) -> dict[str, Any]:
    if not approve:
        raise IntegrationError("Execution requires --approve after reviewing the generated plan.")
    ref = validate_ref(ref)
    mode = item["install_mode"]
    if mode == "selective-copy":
        if shutil.which("git") is None:
            raise IntegrationError("git is required.")
        dest = (destination or (DEFAULT_HOME / "sources" / item["id"])).expanduser().resolve()
        if dest.exists():
            raise IntegrationError(f"Destination already exists: {dest}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        clone = run(["git", "clone", "--filter=blob:none", "--no-checkout", item["source"], str(dest)])
        if clone["returncode"] != 0:
            raise IntegrationError(json.dumps(clone, indent=2))
        checkout = run(["git", "-C", str(dest), "checkout", "--detach", ref])
        if checkout["returncode"] != 0:
            shutil.rmtree(dest, ignore_errors=True)
            raise IntegrationError(json.dumps(checkout, indent=2))
        return {
            "integration": summary(item),
            "approved": True,
            "execution": "source-pinned",
            "destination": str(dest),
            "clone": clone,
            "checkout": checkout,
            "next_step": "Inspect each intended skill, scripts, allowed tools, dependencies, credentials, and linked upstream license before selective adoption.",
        }
    if mode == "npx":
        cmd = render_command(item, ref)
        if shutil.which(cmd[0]) is None:
            raise IntegrationError(f"Required executable is not installed: {cmd[0]}")
        result = run(cmd)
        result.update({"integration": summary(item), "approved": True, "execution": "smoke-test-performed"})
        if result["returncode"] != 0:
            raise IntegrationError(json.dumps(result, indent=2))
        return result
    raise IntegrationError(f"Unsupported install mode: {mode}")


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-screenshot-integrations")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    show = sub.add_parser("show")
    show.add_argument("integration_id")
    for name in ("plan", "install"):
        p = sub.add_parser(name)
        p.add_argument("integration_id")
        p.add_argument("--ref", required=True, help="Exact package version, release tag, or commit SHA.")
        p.add_argument("--destination", type=Path)
        if name == "install":
            p.add_argument("--approve", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "list":
            payload: Any = [summary(item) for item in load_manifest()["integrations"]]
        else:
            item = find_integration(args.integration_id)
            if args.command == "show":
                payload = item
            elif args.command == "plan":
                payload = plan(item, args.ref, args.destination)
            else:
                payload = execute(item, args.ref, args.destination, args.approve)
        print(json.dumps(payload, indent=2))
        return 0
    except (IntegrationError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
