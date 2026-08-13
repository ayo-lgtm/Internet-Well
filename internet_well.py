#!/usr/bin/env python3
"""Privacy-first public CLI for Internet-Well.

Internet-Well performs local, preliminary repository assessment. It does not upload
source code or reports. Hosted documentation providers require explicit consent.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from automation import founder_os_engine as engine

VERSION = "0.3.0"
REPORT_NOTICE = (
    "Preliminary static assessment only. No runtime penetration test, legal opinion, "
    "privacy certification, production approval, or guarantee has occurred."
)
SENSITIVE_NAMES = {
    ".env", ".env.local", ".env.production", ".npmrc", ".pypirc", "id_rsa",
    "id_ed25519", "credentials.json", "service-account.json", "secrets.json",
}
HOSTED_PROVIDERS = {"codewiki"}


def configure_knowledge_root(project: Path) -> Path | None:
    candidates: list[Path] = []
    if os.environ.get("INTERNET_WELL_ROOT"):
        candidates.append(Path(os.environ["INTERNET_WELL_ROOT"]).expanduser())
    candidates.extend([project, Path.cwd(), Path(__file__).resolve().parent])
    seen: set[Path] = set()
    for candidate in candidates:
        try:
            root = candidate.resolve()
        except OSError:
            continue
        if root in seen:
            continue
        seen.add(root)
        catalog = root / "catalog" / "curated-repositories.json"
        registry = root / "registry"
        if catalog.is_file() and registry.is_dir():
            engine.ROOT = root
            engine.CATALOG = catalog
            engine.REGISTRY = registry
            return root
    return None


def require_knowledge_root(project: Path) -> Path:
    root = configure_knowledge_root(project)
    if root is None:
        raise RuntimeError(
            "Planning requires the verified catalog and registry. Run from an "
            "Internet-Well checkout or set INTERNET_WELL_ROOT to a verified release."
        )
    return root


def safe_project_label(project: Path, include_paths: bool) -> str:
    resolved = project.resolve()
    return str(resolved) if include_paths else resolved.name or "project"


def sensitive_file_summary(project: Path) -> dict[str, Any]:
    found: list[str] = []
    skipped = {".git", "node_modules", ".venv", "venv", "dist", "build", ".next"}
    try:
        for path in project.rglob("*"):
            if any(part in skipped for part in path.parts):
                continue
            if path.is_file() and (path.name in SENSITIVE_NAMES or path.suffix in {".pem", ".key", ".p12", ".pfx"}):
                found.append(path.name)
                if len(found) >= 25:
                    break
    except OSError:
        pass
    return {
        "potential_sensitive_files_detected": sorted(set(found)),
        "contents_read": False,
        "warning": "Sensitive file names are reported without reading their contents. Exclude them from any external provider.",
    }


def report_metadata(project: Path, include_paths: bool, classification: str) -> dict[str, Any]:
    return {
        "internet_well_version": VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "report_classification": classification,
        "project": safe_project_label(project, include_paths),
        "path_redacted": not include_paths,
        "processing": "local-only",
        "notice": REPORT_NOTICE,
        "shareability": (
            "Review and sanitize before sharing." if classification != "shareable" else
            "Shareable classification was explicitly selected; review remains required."
        ),
    }


def sanitize_paths(value: Any, project: Path, include_paths: bool) -> Any:
    if include_paths:
        return value
    root = str(project.resolve())
    home = str(Path.home())
    if isinstance(value, dict):
        return {k: sanitize_paths(v, project, include_paths) for k, v in value.items()}
    if isinstance(value, list):
        return [sanitize_paths(v, project, include_paths) for v in value]
    if isinstance(value, str):
        return value.replace(root, "<project>").replace(home, "<home>")
    return value


def add_public_safety(payload: dict[str, Any], project: Path, include_paths: bool, classification: str) -> dict[str, Any]:
    payload = sanitize_paths(payload, project, include_paths)
    return {
        "metadata": report_metadata(project, include_paths, classification),
        "sensitive_file_gate": sensitive_file_summary(project),
        "result": payload,
    }


def git_root(path: Path) -> Path | None:
    try:
        proc = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=False, timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return Path(proc.stdout.strip()).resolve() if proc.returncode == 0 and proc.stdout.strip() else None


def validate_output_path(project: Path, output: Path | None, allow_in_repo_output: bool) -> None:
    if output is None or allow_in_repo_output:
        return
    root = git_root(project)
    if root is None:
        return
    try:
        output.resolve().relative_to(root)
    except ValueError:
        return
    raise RuntimeError(
        "Refusing to write a potentially sensitive report inside the assessed Git repository. "
        "Choose an output path outside the repository or pass --allow-in-repo-output after review."
    )


def markdown_assessment(data: dict[str, Any]) -> str:
    meta, result = data["metadata"], data["result"]
    lines = ["# Internet-Well Preliminary Project Assessment", "", f"> **{meta['notice']}**", ""]
    lines += [f"- **Project:** `{meta['project']}`", f"- **Classification:** `{meta['report_classification']}`", f"- **Risk class:** `{result['risk_class']}`", ""]
    lines += ["## Product types", ""]
    lines += [f"- **{x['name']}** — {x['evidence']} ({x['confidence']} confidence)" for x in result.get("product_types", [])] or ["- None detected."]
    lines += ["", "## Detected stacks", ""]
    lines += [f"- **{x['name']}** — {x['evidence']}" for x in result.get("stacks", [])] or ["- None detected."]
    lines += ["", "## Risks", ""]
    lines += [f"- {x}" for x in result.get("risks", [])] or ["- No specialized risk markers detected by the current static model."]
    lines += ["", "## Required capabilities", ""]
    lines += [f"- {x}" for x in result.get("required_capabilities", [])] or ["- None inferred."]
    lines += ["", "## Privacy gate", ""]
    sensitive = data["sensitive_file_gate"]["potential_sensitive_files_detected"]
    lines += [f"- Potential sensitive filenames detected: {', '.join(sensitive) if sensitive else 'none by filename scan'}", "- File contents were not read by this privacy gate."]
    lines += ["", "## Limits", ""]
    lines += [f"- {x}" for x in result.get("limitations", [])]
    lines += [f"- {REPORT_NOTICE}"]
    return "\n".join(lines) + "\n"


def markdown_plan(data: dict[str, Any]) -> str:
    meta, payload = data["metadata"], data["result"]
    assessment, selection = payload["assessment"], payload["selection"]
    lines = ["# Internet-Well Preliminary Implementation Plan", "", f"> **{meta['notice']}**", ""]
    lines += [f"- **Project:** `{meta['project']}`", f"- **Classification:** `{meta['report_classification']}`", f"- **Goal:** {selection.get('goal') or 'Not supplied'}", f"- **Risk class:** `{selection['risk_class']}`", ""]
    lines += ["## Selected resources", ""]
    for resource in selection.get("selected_resources", []):
        status = resource.get("evidence_status", "unknown")
        matched = ", ".join(resource.get("matched_capabilities", []))
        review = "; human review required" if resource.get("requires_human_review") else ""
        lines.append(f"- **{resource['name']}** — {status}; covers {matched}{review}")
    if not selection.get("selected_resources"):
        lines.append("- None selected.")
    lines += ["", "## Uncovered capabilities", ""]
    lines += [f"- {x}" for x in selection.get("uncovered_capabilities", [])] or ["- None detected by the current model."]
    lines += ["", "## Required implementation order", "", "1. Confirm product, jurisdiction, data sensitivity, and deployment context.", "2. Reject unnecessary or overlapping resources.", "3. Obtain explicit authorization.", "4. Implement in reversible slices.", "5. Run project-specific runtime and security checks.", "6. Record human approvals and residual risks.", "7. Produce a launch verdict with blockers and owners."]
    lines += ["", "## Warnings", ""]
    lines += [f"- {x}" for x in selection.get("warnings", [])]
    lines += [f"- {REPORT_NOTICE}"]
    lines += ["", "## Assessment summary", "", f"Detected product types: {', '.join(x['name'] for x in assessment.get('product_types', [])) or 'none'}." ]
    return "\n".join(lines) + "\n"


def documentation_manifest(project: Path, provider: str, provider_consent: bool, include_paths: bool, classification: str) -> dict[str, Any]:
    if provider in HOSTED_PROVIDERS and not provider_consent:
        raise RuntimeError(
            "Hosted documentation providers require explicit --provider-consent after reviewing retention, training, access, and data residency terms."
        )
    assessment = engine.detect_project(project)
    return {
        "metadata": report_metadata(project, include_paths, classification),
        "provider": provider,
        "provider_mode": "hosted" if provider in HOSTED_PROVIDERS else "local-or-user-managed",
        "provider_consent_recorded": provider_consent,
        "purpose": "Generate navigable code documentation without replacing evidence, approvals, or launch decisions.",
        "required_sections": ["system overview", "repository map", "architecture and component boundaries", "critical user journeys", "data flows and trust boundaries", "authentication and authorization", "external services and deployment", "tests and verification", "known limitations and unknowns"],
        "required_labels": ["verified fact", "inference", "product decision", "unknown"],
        "source_linking": {"required": True, "rule": "Every technical claim must point to a repository path, symbol, configuration file, test, or explicit project decision."},
        "prohibited_claims": ["security approved", "legally compliant", "privacy compliant", "bug free", "production ready", "Tier A approved"],
        "privacy_gate": {"private_repository_requires_authorization": True, "secrets_and_personal_data_must_be_excluded": True, "provider_retention_and_training_terms_must_be_reviewed": True, "default_path_redaction": not include_paths},
        "detected_context": sanitize_paths({"risk_class": assessment["risk_class"], "product_types": [x["name"] for x in assessment.get("product_types", [])], "stacks": [x["name"] for x in assessment.get("stacks", [])], "risks": assessment.get("risks", [])}, project, include_paths),
        "sensitive_file_gate": sensitive_file_summary(project),
        "governance_reference": "docs/PRIVACY-AND-DATA-HANDLING.md",
    }


def markdown_docs(manifest: dict[str, Any]) -> str:
    meta = manifest["metadata"]
    lines = ["# Internet-Well Documentation Manifest", "", f"> **{meta['notice']}**", "", f"- **Provider:** `{manifest['provider']}`", f"- **Provider mode:** `{manifest['provider_mode']}`", f"- **Project:** `{meta['project']}`", f"- **Classification:** `{meta['report_classification']}`", "", "## Required documentation sections", ""]
    lines += [f"- {x}" for x in manifest["required_sections"]]
    lines += ["", "## Prohibited conclusions", ""] + [f"- {x}" for x in manifest["prohibited_claims"]]
    lines += ["", "## Governance", "", manifest["purpose"], "", f"See `{manifest['governance_reference']}`."]
    return "\n".join(lines) + "\n"


def run(project: Path, command: str, goal: str, capabilities: list[str], provider: str, provider_consent: bool, include_paths: bool, classification: str) -> dict[str, Any]:
    project = project.resolve()
    if not project.exists() or not project.is_dir():
        raise RuntimeError("Project path must be an existing directory.")
    if command == "docs":
        return documentation_manifest(project, provider, provider_consent, include_paths, classification)
    assessment = engine.detect_project(project)
    if command == "assess":
        return add_public_safety(assessment, project, include_paths, classification)
    require_knowledge_root(project)
    if command == "security":
        goal = goal or "preliminary security review and secure launch planning"
        capabilities = capabilities + ["sast", "dast", "sbom", "container-scanning"]
    elif command == "launch-review":
        goal = goal or "preliminary launch readiness review"
    payload = {"assessment": assessment, "selection": engine.select_resources(assessment, goal, capabilities)}
    return add_public_safety(payload, project, include_paths, classification)


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well", description="Local, privacy-first preliminary repository assessment.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("assess", "plan", "security", "launch-review", "docs"):
        p = sub.add_parser(name)
        p.add_argument("project", type=Path)
        p.add_argument("--goal", default="")
        p.add_argument("--capability", action="append", default=[])
        p.add_argument("--format", choices=("json", "markdown"), default="json")
        p.add_argument("--output", type=Path)
        p.add_argument("--classification", choices=("private", "internal", "shareable"), default="private")
        p.add_argument("--include-paths", action="store_true", help="Include absolute local paths; disabled by default.")
        p.add_argument("--allow-in-repo-output", action="store_true", help="Allow writing reports inside the assessed Git repository.")
        if name == "docs":
            p.add_argument("--provider", choices=("generic", "codewiki", "open-source-codewiki"), default="generic")
            p.add_argument("--provider-consent", action="store_true", help="Confirm review and acceptance of hosted provider data terms.")
    args = parser.parse_args()
    try:
        validate_output_path(args.project, args.output, args.allow_in_repo_output)
        payload = run(args.project, args.command, args.goal, args.capability, getattr(args, "provider", "generic"), getattr(args, "provider_consent", False), args.include_paths, args.classification)
        if args.format == "markdown":
            text = markdown_assessment(payload) if args.command == "assess" else markdown_docs(payload) if args.command == "docs" else markdown_plan(payload)
        else:
            text = json.dumps(payload, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc), "notice": REPORT_NOTICE}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
