#!/usr/bin/env python3
"""Controlled integration manager for Internet-Well Vibe Coder resources.

This tool never installs or invokes third-party code without an explicit approval
flag. Open-source integrations require a pin. Hosted providers produce review
manifests rather than pretending that website code is part of Internet-Well.
"""
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
    """Locate the adapter manifest in a checkout or an installed environment."""
    candidates: list[Path] = []
    configured_root = os.environ.get("INTERNET_WELL_ROOT")
    if configured_root:
        candidates.append(Path(configured_root).expanduser().resolve() / "integrations" / "vibe" / "manifest.json")
    candidates.extend(
        [
            SOURCE_ROOT / "integrations" / "vibe" / "manifest.json",
            Path(sys.prefix) / "integrations" / "vibe" / "manifest.json",
            Path(sys.base_prefix) / "integrations" / "vibe" / "manifest.json",
        ]
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    searched = ", ".join(str(path) for path in candidates)
    raise IntegrationError(
        "Unable to locate integrations/vibe/manifest.json. "
        "Set INTERNET_WELL_ROOT to a verified Internet-Well checkout. "
        f"Searched: {searched}"
    )


def load_manifest() -> dict[str, Any]:
    manifest = resolve_manifest()
    data = json.loads(manifest.read_text(encoding="utf-8"))
    integrations = data.get("integrations")
    if not isinstance(integrations, list) or not integrations:
        raise IntegrationError("Vibe integration manifest is empty or invalid.")
    return data


def find_integration(integration_id: str) -> dict[str, Any]:
    for item in load_manifest()["integrations"]:
        if item["id"] == integration_id:
            return item
    raise IntegrationError(f"Unknown integration: {integration_id}")


def validate_ref(ref: str) -> str:
    if not ref or any(ch.isspace() for ch in ref):
        raise IntegrationError("A non-empty version, tag, or commit pin is required.")
    if ref.lower() in {"latest", "main", "master", "head", "*"}:
        raise IntegrationError("Floating refs are not accepted. Use an exact release or commit.")
    return ref


def render_command(item: dict[str, Any], ref: str) -> list[str]:
    template = item.get("command_template")
    if not template:
        raise IntegrationError(f"{item['id']} does not define a direct command adapter.")
    return [str(part).format(source=item["source"], ref=ref) for part in template]


def integration_summary(item: dict[str, Any]) -> dict[str, Any]:
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
        "default_action": item.get("default_action"),
        "notes": item.get("notes", ""),
    }


def plan(item: dict[str, Any], ref: str | None, destination: Path | None) -> dict[str, Any]:
    if item.get("pin_required"):
        ref = validate_ref(ref or "")
    mode = item["install_mode"]
    result: dict[str, Any] = {
        "integration": integration_summary(item),
        "approved": False,
        "execution": "not-performed",
        "required_review": [
            "confirm source identity",
            "confirm exact pin",
            "review license and commercial-use terms",
            "inspect scripts, binaries, hooks, dependencies, permissions, and network behavior",
            "run a controlled baseline comparison",
            "record rollback instructions",
        ],
    }
    if mode in {"npm", "npx"}:
        command = render_command(item, ref or "")
        result["planned_command"] = command
        result["planned_command_shell"] = shlex.join(command)
    elif mode in {"git-reference", "selective-copy"}:
        dest = destination or (DEFAULT_HOME / "sources" / item["id"])
        result["planned_clone"] = [
            "git", "clone", "--filter=blob:none", "--no-checkout", item["source"], str(dest)
        ]
        result["planned_checkout"] = ["git", "-C", str(dest), "checkout", "--detach", ref or ""]
        result["destination"] = str(dest)
        if mode == "selective-copy":
            result["post_clone_rule"] = "Inspect and copy only approved subdirectories; do not vendor the whole source by default."
    elif mode == "provider":
        result["provider_review"] = {
            "provider": item["source"],
            "consent_required": item.get("provider_consent_required", True),
            "review": item.get("quality_gates", []) + ["retention", "training use", "data residency", "deletion", "exportability"],
            "prohibited_uses": item.get("prohibited_uses", []),
        }
    else:
        raise IntegrationError(f"Unsupported install mode: {mode}")
    return result


def ensure_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise IntegrationError(f"Required executable is not installed: {name}")


def run_command(command: list[str], cwd: Path | None = None) -> dict[str, Any]:
    proc = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False, timeout=300)
    return {
        "command": command,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-8000:],
        "stderr": proc.stderr[-8000:],
    }


def execute(item: dict[str, Any], ref: str | None, destination: Path | None, approve: bool, provider_consent: bool) -> dict[str, Any]:
    if not approve:
        raise IntegrationError("Execution requires --approve after reviewing the generated plan.")
    if item.get("pin_required"):
        ref = validate_ref(ref or "")
    mode = item["install_mode"]
    if mode == "provider":
        if item.get("provider_consent_required", True) and not provider_consent:
            raise IntegrationError("Hosted provider integration requires --provider-consent after terms and data review.")
        result = plan(item, ref, destination)
        result.update({"approved": True, "execution": "provider-consent-recorded"})
        return result
    if mode in {"npm", "npx"}:
        command = render_command(item, ref or "")
        ensure_tool(command[0])
        result = run_command(command)
        result.update({"integration": integration_summary(item), "approved": True, "execution": "performed"})
        if result["returncode"] != 0:
            raise IntegrationError(json.dumps(result, indent=2))
        return result
    if mode in {"git-reference", "selective-copy"}:
        ensure_tool("git")
        dest = (destination or (DEFAULT_HOME / "sources" / item["id"])).expanduser().resolve()
        if dest.exists():
            raise IntegrationError(f"Destination already exists: {dest}. Remove it or choose another destination.")
        dest.parent.mkdir(parents=True, exist_ok=True)
        clone = run_command(["git", "clone", "--filter=blob:none", "--no-checkout", item["source"], str(dest)])
        if clone["returncode"] != 0:
            raise IntegrationError(json.dumps(clone, indent=2))
        checkout = run_command(["git", "-C", str(dest), "checkout", "--detach", ref or ""])
        if checkout["returncode"] != 0:
            shutil.rmtree(dest, ignore_errors=True)
            raise IntegrationError(json.dumps(checkout, indent=2))
        return {
            "integration": integration_summary(item),
            "approved": True,
            "execution": "source-pinned",
            "destination": str(dest),
            "clone": clone,
            "checkout": checkout,
            "next_step": (
                "Inspect and selectively adopt approved files." if mode == "selective-copy" else
                "Use as a pinned reference implementation; do not treat it as automatically approved code."
            ),
        }
    raise IntegrationError(f"Unsupported install mode: {mode}")


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-integrations")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    show = sub.add_parser("show")
    show.add_argument("integration_id")
    for name in ("plan", "install"):
        p = sub.add_parser(name)
        p.add_argument("integration_id")
        p.add_argument("--ref", help="Exact release, package version, tag, or commit.")
        p.add_argument("--destination", type=Path)
        if name == "install":
            p.add_argument("--approve", action="store_true")
            p.add_argument("--provider-consent", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "list":
            payload: Any = [integration_summary(item) for item in load_manifest()["integrations"]]
        else:
            item = find_integration(args.integration_id)
            if args.command == "show":
                payload = item
            elif args.command == "plan":
                payload = plan(item, args.ref, args.destination)
            else:
                payload = execute(item, args.ref, args.destination, args.approve, args.provider_consent)
        print(json.dumps(payload, indent=2))
        return 0
    except (IntegrationError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
