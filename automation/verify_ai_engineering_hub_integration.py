#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "integrations" / "ai-engineering-hub" / "source.json"
SKILLS = {
    "persistent-agent-memory": ROOT / "skills" / "experimental" / "persistent-agent-memory" / "SKILL.md",
    "agentic-rag": ROOT / "skills" / "experimental" / "agentic-rag" / "SKILL.md",
    "deep-research": ROOT / "skills" / "experimental" / "deep-research-orchestration" / "SKILL.md",
    "agent-delegation": ROOT / "skills" / "experimental" / "agent-delegation" / "SKILL.md",
}
EXPECTED_SOURCE = "https://github.com/patchy631/ai-engineering-hub"
REQUIRED_CANDIDATES = {
    "aieh-agent-memory",
    "aieh-agent-delegation",
    "aieh-agentic-rag",
    "aieh-deep-research",
    "aieh-web-extraction",
    "aieh-document-vision",
    "aieh-reasoning-model",
}
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["source"] == EXPECTED_SOURCE
    assert SHA40.fullmatch(data.get("pin", "")), "upstream source must use an immutable 40-character commit pin"
    assert data.get("approval_required") is True
    assert data.get("auto_install") is False
    assert data.get("auto_execute") is False
    assert data.get("status") == "governed-reference-source"

    candidates = data.get("capability_candidates", [])
    ids = {item["id"] for item in candidates}
    assert len(ids) == len(candidates), "duplicate ai-engineering-hub capability ids"
    missing = REQUIRED_CANDIDATES - ids
    assert not missing, f"missing capability candidates: {sorted(missing)}"

    for item in candidates:
        assert item.get("status") == "candidate", f"{item['id']} must remain candidate until independently evaluated"
        assert item.get("path"), f"{item['id']} missing upstream path"
        assert item.get("capabilities"), f"{item['id']} missing capabilities"
        assert item.get("restrictions"), f"{item['id']} missing restrictions"

    for skill_id, path in SKILLS.items():
        assert path.exists(), f"missing derived skill: {skill_id}"
        text = path.read_text(encoding="utf-8")
        for heading in ("## Purpose", "## Inputs", "## Procedure", "## Outputs", "## Permission boundary", "## Evaluation"):
            assert heading in text, f"{skill_id} missing {heading}"

    print(f"verified ai-engineering-hub source, {len(candidates)} candidates, and {len(SKILLS)} experimental skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
