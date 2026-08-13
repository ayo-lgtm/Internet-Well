#!/usr/bin/env python3
"""Validate the governed Vibe Coder resource catalog."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "vibe-coder-resources.json"
BUNDLE = ROOT / "bundles" / "vibe-coder-intelligence.md"
GOVERNANCE = ROOT / "governance" / "AGENT-SKILL-SUPPLY-CHAIN.md"

REQUIRED_FIELDS = {
    "slug",
    "name",
    "url",
    "type",
    "capabilities",
    "license",
    "readiness",
    "risk",
    "recommendation",
    "restrictions",
}

HIGH_RISK_MARKERS = {
    "high-session-and-credential-access",
    "high-third-party-supply-chain",
    "high-autonomy-and-permission-bypass",
    "high-copying-and-brand-infringement",
    "high-code-ownership-privacy-and-platform-compliance",
}


def main() -> None:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    resources = data.get("resources")
    assert isinstance(resources, list) and resources, "resources must be a non-empty list"

    slugs: set[str] = set()
    types: set[str] = set()
    for index, resource in enumerate(resources):
        missing = REQUIRED_FIELDS - resource.keys()
        assert not missing, f"resource {index} missing fields: {sorted(missing)}"
        slug = resource["slug"]
        assert slug not in slugs, f"duplicate slug: {slug}"
        slugs.add(slug)
        types.add(resource["type"])
        assert resource["capabilities"], f"{slug} has no capabilities"
        assert resource["restrictions"], f"{slug} has no restrictions"
        assert str(resource["url"]).startswith("https://"), f"{slug} URL must use HTTPS"
        if resource["risk"] in HIGH_RISK_MARKERS:
            joined = " ".join(resource["restrictions"]).lower()
            assert any(word in joined for word in ("approval", "review", "verify", "inspect", "protect")), (
                f"{slug} is high risk but lacks a concrete review or approval restriction"
            )

    required_slugs = {
        "anthropics/skills",
        "vercel-labs/skills",
        "vercel-labs/agent-browser",
        "gsd-build/get-shit-done",
        "Leonxlnx/taste-skill",
        "blader/humanizer",
        "jenna-russell/storyscope",
        "DavidHDev/react-bits",
        "animejs/anime",
        "shadergradient/shadergradient",
        "jitter-video/jitter",
        "refero-design/refero",
        "10x-app-builder/10x",
    }
    assert required_slugs <= slugs, f"missing requested resources: {sorted(required_slugs - slugs)}"
    assert len(types) >= 8, "catalog must preserve distinct resource roles"

    bundle_text = BUNDLE.read_text(encoding="utf-8").lower()
    governance_text = GOVERNANCE.read_text(encoding="utf-8").lower()
    for phrase in (
        "marketplace rank is not approval",
        "never require `--dangerously-skip-permissions`",
        "do not copy exact protected branding",
    ):
        assert phrase.lower() in bundle_text, f"bundle missing safeguard: {phrase}"
    for phrase in ("matched baseline", "browser-agent controls", "reverification"):
        assert phrase.lower() in governance_text, f"governance missing section: {phrase}"

    print(f"Validated {len(resources)} vibe-coder resources across {len(types)} resource types.")


if __name__ == "__main__":
    main()
