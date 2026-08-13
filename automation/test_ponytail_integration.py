#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from automation import ponytail_integration as pi


def main() -> None:
    manifest = pi.load_manifest()
    assert manifest["id"] == "ponytail"
    assert manifest["source"] == "https://github.com/DietrichGebert/ponytail"
    assert "ponytail-review" in manifest["skills"]
    assert manifest["approval_required"] is True

    with tempfile.TemporaryDirectory() as tmp:
        plan = pi.plan("v4.8.4", Path(tmp) / "ponytail")
        assert plan["planned_checkout"][-1] == "v4.8.4"
        assert plan["execution"] == "not-performed"
        assert "selectively" in plan["adoption_rule"].lower()

    for floating in ("latest", "main", "master", "HEAD", "*"):
        try:
            pi.validate_ref(floating)
        except pi.PonytailError:
            pass
        else:
            raise AssertionError(f"floating ref accepted: {floating}")

    try:
        pi.install("v4.8.4", None, approve=False)
    except pi.PonytailError as exc:
        assert "--approve" in str(exc)
    else:
        raise AssertionError("installation ran without approval")

    print(json.dumps({"integration": "ponytail", "status": "ok"}))


if __name__ == "__main__":
    main()
