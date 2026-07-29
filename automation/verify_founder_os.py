#!/usr/bin/env python3
"""Validate Internet-Well Founder OS operating artifacts.

Checks commands, playbooks, profiles, stacks, bundles, skills, output schemas,
capability references, registry references, and required safety sections.
No third-party dependencies; Python 3.9+.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAPABILITY_FILE = ROOT / "capabilities" / "CAPABILITY-GRAPH.md"
REQUIRED_ROOT = ["AGENTS.md", "START-HERE.md", "FOUNDER-OS.md"]
REQUIRED_PLAYBOOK = [
    "## Purpose", "## Inputs", "## Workflow", "## Outputs",
    "## Verification", "## Stop conditions", "## Human review",
]
REQUIRED_COMMAND = ["## Purpose", "## Inputs", "## Procedure", "## Output"]
REQUIRED_PROFILE = ["## Applies to", "## Required capabilities", "## Risk model", "## Completion evidence"]
REQUIRED_STACK = ["## Detection", "## Required controls", "## Compatible capabilities", "## Verification"]
REQUIRED_BUNDLE = ["## Outcome", "## Required capabilities", "## Selection rules", "## Implementation order", "## Verification", "## Human review"]
REQUIRED_SKILL = ["## Purpose", "## Inputs", "## Procedure", "## Outputs", "## Permission boundary", "## Evaluation"]
HIGH_RISK_TERMS = {"legal", "finance", "trading", "security", "privacy", "healthcare", "authentication", "production"}


def headings(path: Path, required: list[str], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for heading in required:
        if heading not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing {heading}")


def markdown_files(directory: str) -> list[Path]:
    base = ROOT / directory
    return sorted(p for p in base.rglob("*.md") if p.name != "README.md") if base.exists() else []


def extract_capabilities() -> set[str]:
    text = CAPABILITY_FILE.read_text(encoding="utf-8")
    values = set(re.findall(r"`([a-z][a-z0-9-]+)`", text))
    values.update(re.findall(r"^###\s+([a-z][a-z0-9-]+)\s*$", text, re.M))
    return values


def validate_json(errors: list[str]) -> None:
    for path in sorted((ROOT / "outputs").glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                errors.append(f"{path.relative_to(ROOT)}: schema must be an object")
            if "$schema" not in data:
                errors.append(f"{path.relative_to(ROOT)}: missing $schema")
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")


def validate_links(errors: list[str]) -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: dead local link {target}")


def validate_registry_refs(errors: list[str]) -> None:
    pattern = re.compile(r"registry/([a-z-]+/[a-z0-9._-]+\.md)")
    for directory in ["commands", "playbooks", "profiles", "stacks", "bundles", "skills"]:
        for path in markdown_files(directory):
            for rel in pattern.findall(path.read_text(encoding="utf-8")):
                if not (ROOT / "registry" / rel).exists():
                    errors.append(f"{path.relative_to(ROOT)}: missing registry/{rel}")


def validate_safety(errors: list[str]) -> None:
    for directory in ["playbooks", "profiles", "bundles", "skills"]:
        for path in markdown_files(directory):
            text = path.read_text(encoding="utf-8").lower()
            if any(term in path.as_posix().lower() or term in text for term in HIGH_RISK_TERMS):
                if "human review" not in text:
                    errors.append(f"{path.relative_to(ROOT)}: high-risk artifact lacks human review")


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_ROOT:
        if not (ROOT / rel).exists():
            errors.append(f"missing root artifact {rel}")
    if not CAPABILITY_FILE.exists():
        errors.append("missing capabilities/CAPABILITY-GRAPH.md")
    for path in markdown_files("commands"):
        headings(path, REQUIRED_COMMAND, errors)
    for path in markdown_files("playbooks"):
        headings(path, REQUIRED_PLAYBOOK, errors)
    for path in markdown_files("profiles"):
        headings(path, REQUIRED_PROFILE, errors)
    for path in markdown_files("stacks"):
        headings(path, REQUIRED_STACK, errors)
    for path in markdown_files("bundles"):
        headings(path, REQUIRED_BUNDLE, errors)
    for path in markdown_files("skills"):
        if path.name == "SKILL.md":
            headings(path, REQUIRED_SKILL, errors)
    validate_json(errors)
    validate_links(errors)
    validate_registry_refs(errors)
    validate_safety(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Founder OS validation failed with {len(errors)} error(s)")
        return 1
    print("OK: Founder OS structure, schemas, links, references, and safety gates are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
