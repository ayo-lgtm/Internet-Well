#!/usr/bin/env python3
"""Validate Internet-Well Founder OS operating artifacts.

Checks commands, playbooks, profiles, stacks, bundles, skills, output schemas,
local links, registry references, and safety gates. Python 3.9+ only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAPABILITY_FILE = ROOT / "capabilities" / "CAPABILITY-GRAPH.md"
REQUIRED_ROOT = ["AGENTS.md", "START-HERE.md", "FOUNDER-OS.md"]
CONCEPTS = {
    "commands": [
        ("purpose", ["## purpose", "## goal", "## use when"]),
        ("inputs", ["## inputs", "## required inputs"]),
        ("procedure", ["## procedure", "## workflow", "## steps"]),
        ("output", ["## output", "## required outputs", "## required result"]),
    ],
    "playbooks": [
        ("purpose", ["## purpose", "## goal"]),
        ("inputs", ["## inputs", "## required inputs"]),
        ("workflow", ["## workflow", "## procedure"]),
        ("outputs", ["## outputs", "## required outputs"]),
        ("stop conditions", ["## stop conditions"]),
    ],
    "profiles": [
        ("scope", ["## applies to", "## use this profile when", "## apply when"]),
        ("capabilities", ["## required capabilities", "## baseline capabilities"]),
        ("risk", ["## risk model", "## major risks", "## primary risks", "## launch blockers"]),
        ("evidence", ["## completion evidence", "## definition of done", "## launch blockers"]),
    ],
    "stacks": [
        ("detection", ["## detection", "## detection signals", "## apply when"]),
        ("controls", ["## required controls", "## baseline controls", "## mandatory controls"]),
        ("capabilities", ["## compatible capabilities", "## capability map", "## baseline capabilities"]),
        ("verification", ["## verification", "## validation", "## release gates"]),
    ],
    "bundles": [
        ("outcome", ["## outcome", "## purpose"]),
        ("capabilities", ["## required capabilities"]),
        ("selection", ["## selection rules"]),
        ("order", ["## implementation order"]),
        ("verification", ["## verification"]),
        ("human review", ["## human review"]),
    ],
    "skills": [
        ("purpose", ["## purpose"]),
        ("inputs", ["## inputs"]),
        ("procedure", ["## procedure", "## workflow"]),
        ("outputs", ["## outputs"]),
        ("permission", ["## permission boundary"]),
        ("evaluation", ["## evaluation"]),
    ],
}
HIGH_RISK_TERMS = {"legal", "finance", "trading", "security", "privacy", "healthcare", "authentication", "production"}


def markdown_files(directory: str) -> list[Path]:
    base = ROOT / directory
    if not base.exists():
        return []
    return sorted(p for p in base.rglob("*.md") if p.name != "README.md")


def check_concepts(path: Path, kind: str, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8").lower()
    for label, alternatives in CONCEPTS[kind]:
        if not any(value in text for value in alternatives):
            errors.append(f"{path.relative_to(ROOT)}: missing {label} section")


def validate_json(errors: list[str]) -> None:
    output_dir = ROOT / "outputs"
    if not output_dir.exists():
        errors.append("missing outputs directory")
        return
    for path in sorted(output_dir.glob("*.json")):
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
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).resolve().exists():
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
            risky = any(term in path.as_posix().lower() or term in text for term in HIGH_RISK_TERMS)
            if risky and "human review" not in text:
                errors.append(f"{path.relative_to(ROOT)}: high-risk artifact lacks human review")


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_ROOT:
        if not (ROOT / rel).exists():
            errors.append(f"missing root artifact {rel}")
    if not CAPABILITY_FILE.exists():
        errors.append("missing capabilities/CAPABILITY-GRAPH.md")
    for kind in ["commands", "playbooks", "profiles", "stacks", "bundles"]:
        for path in markdown_files(kind):
            check_concepts(path, kind, errors)
    for path in markdown_files("skills"):
        if path.name == "SKILL.md":
            check_concepts(path, "skills", errors)
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
