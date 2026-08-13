#!/usr/bin/env python3
"""Regression tests for governed Vibe integrations."""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from automation import vibe_integrations as vi


def main() -> None:
    data = vi.load_manifest()
    items = data["integrations"]
    assert len(items) == 13
    ids = {item["id"] for item in items}
    assert len(ids) == 13

    for item in items:
        summary = vi.integration_summary(item)
        assert summary["approval_required"] is True
        assert item["source"].startswith("https://")
        assert item["capabilities"]

    anime = vi.find_integration("animejs")
    anime_plan = vi.plan(anime, "4.0.0", None)
    assert anime_plan["planned_command"] == ["npm", "install", "animejs@4.0.0"]
    assert anime_plan["execution"] == "not-performed"

    skills = vi.find_integration("skills-cli")
    skills_plan = vi.plan(skills, "1.2.3", None)
    assert "@1.2.3" in skills_plan["planned_command"][-1]

    agent_browser = vi.find_integration("agent-browser")
    browser_plan = vi.plan(agent_browser, "0.1.0", None)
    assert browser_plan["integration"]["kind"] == "browser-runtime"

    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "skill-source"
        taste = vi.find_integration("taste-skill")
        taste_plan = vi.plan(taste, "abc1234", dest)
        assert taste_plan["destination"] == str(dest)
        assert taste_plan["planned_checkout"][-1] == "abc1234"
        rule = taste_plan["post_clone_rule"].lower()
        assert "approved" in rule and "whole source" in rule

    provider = vi.find_integration("refero")
    provider_plan = vi.plan(provider, None, None)
    assert provider_plan["provider_review"]["consent_required"] is True
    assert "copy-protected-branding" in provider_plan["provider_review"]["prohibited_uses"]

    for floating in ("latest", "main", "master", "HEAD", "*"):
        try:
            vi.validate_ref(floating)
        except vi.IntegrationError:
            pass
        else:
            raise AssertionError(f"floating ref was accepted: {floating}")

    try:
        vi.execute(anime, "4.0.0", None, approve=False, provider_consent=False)
    except vi.IntegrationError as exc:
        assert "--approve" in str(exc)
    else:
        raise AssertionError("execution occurred without approval")

    print(json.dumps({"validated_integrations": len(items), "status": "ok"}))


if __name__ == "__main__":
    main()
