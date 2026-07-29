#!/usr/bin/env python3
"""Founder-facing CLI for Internet-Well.

Examples:
  python3 internet_well.py assess .
  python3 internet_well.py plan . --goal "launch legal AI SaaS"
  python3 internet_well.py security .
  python3 internet_well.py launch-review .

The CLI emits JSON by default and Markdown with --format markdown.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from automation.founder_os_engine import detect_project, select_resources


def markdown_assessment(data: dict) -> str:
    lines = ["# Internet-Well Project Assessment", ""]
    lines += [f"- **Project:** `{data['project_path']}`", f"- **Risk class:** `{data['risk_class']}`", ""]
    lines += ["## Product types", ""]
    for item in data.get("product_types", []):
        lines.append(f"- **{item['name']}** — {item['evidence']} ({item['confidence']} confidence)")
    lines += ["", "## Detected stacks", ""]
    for item in data.get("stacks", []):
        lines.append(f"- **{item['name']}** — {item['evidence']}")
    lines += ["", "## Risks", ""]
    lines += [f"- {risk}" for risk in data.get("risks", [])] or ["- No specialized risk markers detected."]
    lines += ["", "## Required capabilities", ""]
    lines += [f"- {cap}" for cap in data.get("required_capabilities", [])]
    lines += ["", "## Limits", ""]
    lines += [f"- {limit}" for limit in data.get("limitations", [])]
    return "\n".join(lines) + "\n"


def markdown_plan(payload: dict) -> str:
    assessment = payload["assessment"]
    selection = payload["selection"]
    lines = ["# Internet-Well Implementation Plan", ""]
    lines += [f"- **Goal:** {selection.get('goal') or 'Not supplied'}", f"- **Risk class:** `{selection['risk_class']}`", ""]
    lines += ["## Selected resources", ""]
    for resource in selection.get("selected_resources", []):
        status = resource.get("evidence_status", "unknown")
        matched = ", ".join(resource.get("matched_capabilities", []))
        review = "; human review required" if resource.get("requires_human_review") else ""
        lines.append(f"- **{resource['name']}** — {status}; covers {matched}{review}")
    lines += ["", "## Uncovered capabilities", ""]
    lines += [f"- {cap}" for cap in selection.get("uncovered_capabilities", [])] or ["- None detected by the current model."]
    lines += ["", "## Implementation order", ""]
    lines += [
        "1. Confirm product and jurisdiction context.",
        "2. Reject unnecessary or overlapping resources.",
        "3. Approve the smallest compatible bundle.",
        "4. Implement in reversible slices.",
        "5. Run project-specific tests and safety gates.",
        "6. Record human approvals and residual risks.",
        "7. Produce a launch verdict with blockers and owners.",
    ]
    lines += ["", "## Warnings", ""]
    lines += [f"- {warning}" for warning in selection.get("warnings", [])]
    lines += ["", "## Assessment summary", "", f"Detected product types: {', '.join(x['name'] for x in assessment.get('product_types', []))}."]
    return "\n".join(lines) + "\n"


def run(project: Path, command: str, goal: str, capabilities: list[str]) -> dict:
    assessment = detect_project(project)
    if command == "assess":
        return assessment
    if command == "security":
        goal = goal or "security review and secure launch"
        capabilities = capabilities + ["sast", "dast", "sbom", "container-scanning"]
    elif command == "launch-review":
        goal = goal or "launch readiness"
    return {
        "assessment": assessment,
        "selection": select_resources(assessment, goal, capabilities),
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("assess", "plan", "security", "launch-review"):
        p = sub.add_parser(name)
        p.add_argument("project", type=Path)
        p.add_argument("--goal", default="")
        p.add_argument("--capability", action="append", default=[])
        p.add_argument("--format", choices=("json", "markdown"), default="json")
        p.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = run(args.project, args.command, args.goal, args.capability)
        if args.format == "markdown":
            text = markdown_assessment(payload) if args.command == "assess" else markdown_plan(payload)
        else:
            text = json.dumps(payload, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
