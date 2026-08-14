#!/usr/bin/env python3
"""Governed adapter for the verified Apple Design Skills family."""
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
DEFAULT_REF = "8a3fbea8b561405e5719d682ebd1d14c952aecd7"


class IntegrationError(RuntimeError):
    pass


def resolve_manifest() -> Path:
    configured_root = os.environ.get("INTERNET_WELL_ROOT")
    candidates: list[Path] = []
    if configured_root:
        candidates.append(Path(configured_root).expanduser().resolve() / "integrations" / "vibe" / "apple-design-skills.json")
    candidates.extend([
        SOURCE_ROOT / "integrations" / "vibe" / "apple-design-skills.json",
        Path(sys.prefix) / "integrations" / "vibe" / "apple-design-skills.json",
        Path(sys.base_prefix) / "integrations" / "vibe" / "apple-design-skills.json",
    ])
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise IntegrationError("Unable to locate integrations/vibe/apple-design-skills.json. Set INTERNET_WELL_ROOT to a verified checkout.")


def load_manifest() -> dict[str, Any]:
    data = json.loads(resolve_manifest().read_text(encoding="utf-8"))
    if data.get("integration", {}).get("id") != "apple-design-skills":
        raise IntegrationError("Apple Design Skills manifest is invalid.")
    return data


def validate_ref(ref: str) -> str:
    if not ref or any(ch.isspace() for ch in ref):
        raise IntegrationError("A non-empty exact tag or commit pin is required.")
    if ref.lower() in {"latest", "main", "master", "head", "*"}:
        raise IntegrationError("Floating refs are prohibited. Use an exact commit or immutable tag.")
    return ref


def run(command: list[str]) -> dict[str, Any]:
    proc = subprocess.run(command, text=True, capture_output=True, check=False, timeout=300)
    return {
        "command": command,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-8000:],
        "stderr": proc.stderr[-8000:],
    }


def source_dir(destination: Path | None = None) -> Path:
    return (destination or (DEFAULT_HOME / "sources" / "apple-design-skills")).expanduser().resolve()


def plan(ref: str, destination: Path | None = None) -> dict[str, Any]:
    data = load_manifest()
    ref = validate_ref(ref)
    dest = source_dir(destination)
    return {
        "integration": data["integration"],
        "source": data["source"],
        "approved": False,
        "execution": "not-performed",
        "planned_clone": ["git", "clone", "--filter=blob:none", "--no-checkout", data["source"]["url"], str(dest)],
        "planned_checkout": ["git", "-C", str(dest), "checkout", "--detach", ref],
        "destination": str(dest),
        "required_review": [
            "confirm source repository identity and MIT license",
            "confirm exact immutable ref",
            "inspect install.sh and install.ps1 before any use",
            "inspect each intended SKILL.md and references",
            "compare claims against current official Apple HIG/platform documentation",
            "review accessibility, reduced-motion, performance, and brand-distinctiveness impact",
            "keep Apple trademarks and copyrighted media out of product assets unless separately authorized",
            "compare product output with and without the skill family",
        ],
        "note": "Planning never runs upstream installers or modifies agent skill directories.",
    }


def install_source(ref: str, destination: Path | None, approve: bool) -> dict[str, Any]:
    if not approve:
        raise IntegrationError("Source installation requires --approve after reviewing the plan.")
    data = load_manifest()
    ref = validate_ref(ref)
    dest = source_dir(destination)
    if shutil.which("git") is None:
        raise IntegrationError("git is required.")
    if dest.exists():
        raise IntegrationError(f"Destination already exists: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    clone = run(["git", "clone", "--filter=blob:none", "--no-checkout", data["source"]["url"], str(dest)])
    if clone["returncode"] != 0:
        raise IntegrationError(json.dumps(clone, indent=2))
    checkout = run(["git", "-C", str(dest), "checkout", "--detach", ref])
    if checkout["returncode"] != 0:
        shutil.rmtree(dest, ignore_errors=True)
        raise IntegrationError(json.dumps(checkout, indent=2))
    return {
        "approved": True,
        "execution": "source-pinned",
        "destination": str(dest),
        "ref": ref,
        "clone": clone,
        "checkout": checkout,
        "next_step": "Inspect the selected skill directory before adoption. Do not run upstream install scripts automatically.",
    }


def target_root(target: str, custom: Path | None = None) -> Path:
    if custom is not None:
        return custom.expanduser().resolve()
    if target == "claude-code":
        return (Path.home() / ".claude" / "skills").resolve()
    if target == "codex":
        return (Path.home() / ".agents" / "skills").resolve()
    raise IntegrationError("Target must be claude-code or codex unless --target-dir is supplied.")


def adopt(skill: str, source: Path, target: str, target_dir: Path | None, approve: bool) -> dict[str, Any]:
    if not approve:
        raise IntegrationError("Skill adoption requires --approve after source inspection.")
    data = load_manifest()
    allowed = set(data["integration"]["skills"])
    if skill not in allowed:
        raise IntegrationError(f"Unknown Apple design skill: {skill}")
    src = source.expanduser().resolve() / "skills" / skill
    if not src.is_dir() or not (src / "SKILL.md").is_file():
        raise IntegrationError(f"Reviewed skill directory is missing or incomplete: {src}")
    root = target_root(target, target_dir)
    dst = root / skill
    if dst.exists():
        raise IntegrationError(f"Refusing to overwrite existing skill: {dst}")
    root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)
    return {
        "approved": True,
        "execution": "skill-adopted",
        "skill": skill,
        "source": str(src),
        "target": str(dst),
        "post_adoption_gates": data["governance"]["quality_gates"],
        "authority_rule": data["governance"]["authority_rule"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-apple-design")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show")
    sub.add_parser("list-skills")

    p = sub.add_parser("plan")
    p.add_argument("--ref", default=DEFAULT_REF)
    p.add_argument("--destination", type=Path)

    p = sub.add_parser("install")
    p.add_argument("--ref", default=DEFAULT_REF)
    p.add_argument("--destination", type=Path)
    p.add_argument("--approve", action="store_true")

    p = sub.add_parser("adopt")
    p.add_argument("skill")
    p.add_argument("--source", type=Path, default=source_dir())
    p.add_argument("--target", choices=["claude-code", "codex"], required=True)
    p.add_argument("--target-dir", type=Path)
    p.add_argument("--approve", action="store_true")

    args = parser.parse_args()
    try:
        data = load_manifest()
        if args.command == "show":
            payload: Any = data
        elif args.command == "list-skills":
            payload = data["integration"]["skills"]
        elif args.command == "plan":
            payload = plan(args.ref, args.destination)
        elif args.command == "install":
            payload = install_source(args.ref, args.destination, args.approve)
        else:
            payload = adopt(args.skill, args.source, args.target, args.target_dir, args.approve)
        print(json.dumps(payload, indent=2))
        return 0
    except (IntegrationError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
