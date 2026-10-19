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
# Each derived skill is tied to exactly one governed candidate and the
# restriction that skill must carry forward.
SKILL_CANDIDATES = {
    "persistent-agent-memory": ("aieh-agent-memory", "tenant-isolation"),
    "agentic-rag": ("aieh-agentic-rag", "citation-required-for-derived-claims"),
    "deep-research": ("aieh-deep-research", "bounded-cost"),
    "agent-delegation": ("aieh-agent-delegation", "bounded-delegation"),
}
EXPECTED_SOURCE = "https://github.com/patchy631/ai-engineering-hub"
EXPECTED_PIN = "2c9b106168d4540b88e727e4aa316c06c856c2b7"
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


class VerificationError(Exception):
    pass


def check(condition: bool, message: str) -> None:
    # Explicit checks rather than assert, so `python -O` cannot disable them.
    if not condition:
        raise VerificationError(message)


def verify() -> str:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    check(data.get("source") == EXPECTED_SOURCE, "unexpected upstream source")
    check(bool(SHA40.fullmatch(data.get("pin", ""))), "upstream source must use an immutable 40-character commit pin")
    check(data.get("pin") == EXPECTED_PIN, "unexpected upstream source commit pin")
    check(data.get("approval_required") is True, "approval_required must be true")
    check(data.get("auto_install") is False, "auto_install must be false")
    check(data.get("auto_execute") is False, "auto_execute must be false")
    check(data.get("status") == "governed-reference-source", "status must be governed-reference-source")

    candidates = data.get("capability_candidates", [])
    by_id = {item["id"]: item for item in candidates}
    check(len(by_id) == len(candidates), "duplicate ai-engineering-hub capability ids")
    missing = REQUIRED_CANDIDATES - set(by_id)
    check(not missing, f"missing capability candidates: {sorted(missing)}")

    for item in candidates:
        check(item.get("status") == "candidate", f"{item['id']} must remain candidate until independently evaluated")
        check(bool(item.get("path")), f"{item['id']} missing upstream path")
        check(bool(item.get("capabilities")), f"{item['id']} missing capabilities")
        check(bool(item.get("restrictions")), f"{item['id']} missing restrictions")

    check(set(SKILL_CANDIDATES) == set(SKILLS), "every derived skill needs exactly one candidate mapping")
    for skill_id, path in SKILLS.items():
        check(path.exists(), f"missing derived skill: {skill_id}")
        text = path.read_text(encoding="utf-8")
        for heading in ("## Purpose", "## Inputs", "## Procedure", "## Outputs", "## Permission boundary", "## Evaluation"):
            check(heading in text, f"{skill_id} missing {heading}")

        candidate_id, restriction = SKILL_CANDIDATES[skill_id]
        candidate = by_id.get(candidate_id)
        check(candidate is not None, f"{skill_id} maps to unknown candidate {candidate_id}")
        upstream_ref = f"patchy631/ai-engineering-hub/{candidate['path']}"
        check(upstream_ref in text, f"{skill_id} must reference {upstream_ref} from candidate {candidate_id}")
        refs = set(re.findall(r"patchy631/ai-engineering-hub/([^`\s]+)", text))
        check(refs == {candidate["path"]}, f"{skill_id} references upstream paths {sorted(refs)} not matching {candidate_id}")
        check(restriction in candidate["restrictions"], f"{candidate_id} must keep restriction {restriction}")

    return f"verified ai-engineering-hub source, {len(candidates)} candidates, and {len(SKILLS)} experimental skills"


def main() -> int:
    try:
        print(verify())
    except VerificationError as exc:
        print(f"ai-engineering-hub verification failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
