#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "integrations" / "agent-systems" / "wassim-agent-systems.json"
REQUIRED = {
    "autonomous-loop",
    "event-driven-autonomous-loop",
    "flywheel",
    "sentience-loop",
    "memory",
    "agent-os",
    "cortex",
    "megacycle",
    "fusion",
    "qwen38-uncensored",
}


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    items = data["integrations"]
    ids = {x["id"] for x in items}
    missing = REQUIRED - ids
    assert not missing, f"missing integrations: {sorted(missing)}"
    assert len(ids) == len(items), "duplicate integration ids"
    for item in items:
        pin = item.get("pin", "")
        assert pin and pin.lower() not in {"latest", "main", "master", "head", "*"}
        assert item.get("source", "").startswith("https://github.com/Wassimyounes01/")
        assert item.get("approval_required") is True
    restricted = next(x for x in items if x["id"] == "qwen38-uncensored")
    assert restricted["install_mode"] == "reference-only"
    assert restricted["auto_install"] is False
    assert restricted["auto_execute"] is False
    print(f"verified {len(items)} governed agent-system integrations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
