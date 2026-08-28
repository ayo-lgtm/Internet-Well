#!/usr/bin/env python3
"""Governed SOC 2/GRC planning adapter for Probo.

This adapter is intentionally local and non-attesting. It prepares readiness and
CPA handoff plans; it never claims SOC 2 compliance or submits evidence.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

SOURCE_ROOT = Path(__file__).resolve().parents[1]


class ComplianceError(RuntimeError):
    pass


def resolve_manifest() -> Path:
    roots = []
    configured = os.environ.get("INTERNET_WELL_ROOT")
    if configured:
        roots.append(Path(configured).expanduser().resolve())
    roots.extend([SOURCE_ROOT, Path(sys.prefix), Path(sys.base_prefix)])
    for root in roots:
        candidate = root / "integrations" / "compliance" / "probo.json"
        if candidate.is_file():
            return candidate
    raise ComplianceError("Unable to locate integrations/compliance/probo.json")


def manifest() -> dict[str, Any]:
    data = json.loads(resolve_manifest().read_text(encoding="utf-8"))
    if not re.fullmatch(r"[0-9a-f]{40}", str(data.get("pin", ""))):
        raise ComplianceError("Probo must be pinned to an immutable 40-character commit SHA.")
    if data.get("license") != "MIT":
        raise ComplianceError("Unexpected Probo license metadata; review upstream before use.")
    return data


def readiness_plan(criteria: list[str]) -> dict[str, Any]:
    cfg = manifest()
    selected = criteria or ["security"]
    normalized = []
    for item in selected:
        value = item.strip().casefold().replace(" ", "-")
        if value and value not in normalized:
            normalized.append(value)
    return {
        "status": "readiness-plan-only",
        "framework": "SOC 2",
        "report_type": "Type I",
        "trust_services_criteria": normalized,
        "engine": cfg["name"],
        "source_pin": cfg["pin"],
        "attestation_authority": "independent-licensed-cpa-firm",
        "workstreams": [
            "define-system-boundary-and-scope",
            "map-controls-to-selected-trust-services-criteria",
            "assign-control-owners",
            "approve-policies",
            "collect-and-index-source-evidence",
            "perform-risk-and-vendor-reviews",
            "perform-access-review",
            "document-exceptions-and-remediation",
            "management-readiness-review",
            "prepare-independent-cpa-handoff",
        ],
        "evidence_rules": cfg["evidence_contract"]["rules"],
        "human_gates": cfg["required_human_review"],
        "claims_prohibited": [
            "soc2-certified",
            "soc2-compliant-because-tool-passed",
            "audit-complete-without-cpa-report",
            "control-effective-without-supporting-evidence",
        ],
    }


def auditor_handoff(company: str, criteria: list[str]) -> dict[str, Any]:
    cfg = manifest()
    plan = readiness_plan(criteria)
    return {
        "status": "auditor-handoff-draft",
        "company": company.strip() or "unnamed-company",
        "framework": plan["framework"],
        "report_type": plan["report_type"],
        "trust_services_criteria": plan["trust_services_criteria"],
        "probo_source_pin": cfg["pin"],
        "package": cfg["auditor_handoff"]["package"],
        "auditor_due_diligence": cfg["auditor_handoff"]["auditor_selection_checks"],
        "required_confirmations_before_engagement": [
            "auditor-confirms-cpa-firm-and-peer-review-status",
            "auditor-confirms-acceptance-of-customer-managed-probo-evidence",
            "auditor-confirms-evidence-format-and-secure-transfer-method",
            "auditor-confirms-fixed-or-bounded-fee-in-writing",
            "auditor-confirms-report-issuance-is-included",
            "auditor-confirms-no-mandatory-commercial-grc-platform",
            "scope-and-period-approved-by-management-and-auditor",
        ],
        "submission": "not-performed",
        "attestation": "not-performed",
        "notice": cfg["authority_boundary"],
    }


def evidence_template() -> dict[str, Any]:
    cfg = manifest()
    return {
        "schema": "internet-well/probo-evidence-handoff/v1",
        "classification": "confidential-audit-evidence",
        "required_fields": cfg["evidence_contract"]["required_fields"],
        "privacy": [
            "exclude-secrets-and-private-keys",
            "minimize-personal-data",
            "use-secure-auditor-transfer-channel",
            "retain-source-system-and-collection-timestamps",
        ],
        "example": {
            "control_id": "CC-example",
            "control_objective": "Describe the control objective without claiming effectiveness.",
            "owner": "control-owner",
            "status": "ready-for-review",
            "evidence_items": [],
            "collection_period": "YYYY-MM-DD/YYYY-MM-DD",
            "source_system": "authorized-source",
            "collected_at": "RFC3339 timestamp",
            "reviewer": "human-reviewer",
            "exceptions": [],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-compliance")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show")
    ready = sub.add_parser("soc2-readiness")
    ready.add_argument("--criteria", action="append", default=[])
    handoff = sub.add_parser("auditor-handoff")
    handoff.add_argument("--company", required=True)
    handoff.add_argument("--criteria", action="append", default=[])
    sub.add_parser("evidence-template")
    args = parser.parse_args()
    try:
        if args.command == "show":
            payload: Any = manifest()
        elif args.command == "soc2-readiness":
            payload = readiness_plan(args.criteria)
        elif args.command == "auditor-handoff":
            payload = auditor_handoff(args.company, args.criteria)
        else:
            payload = evidence_template()
        print(json.dumps(payload, indent=2))
        return 0
    except (ComplianceError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
