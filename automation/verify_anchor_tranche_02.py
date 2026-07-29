#!/usr/bin/env python3
"""Validate harmless outputs produced by tranche-02 security tools."""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path.cwd()


def require(path: str) -> pathlib.Path:
    target = ROOT / path
    if not target.exists() or target.stat().st_size == 0:
        raise AssertionError(f"missing or empty evidence file: {path}")
    return target


def main() -> int:
    expected = [
        "tranche-02/versions.txt",
        "tranche-02/gitleaks.json",
        "tranche-02/syft.spdx.json",
        "tranche-02/grype.json",
        "tranche-02/semgrep.json",
        "tranche-02/osv.json",
    ]
    for path in expected:
        require(path)

    versions = require("tranche-02/versions.txt").read_text(encoding="utf-8", errors="replace")
    for marker in ["0.70.0", "8.30.1", "2.3.8", "1.44.0", "0.112.0", "3.0.6", "1.162.0", "3.95.2", "2.17.0", "5.5.0"]:
        if marker not in versions:
            raise AssertionError(f"expected version marker not found: {marker}")

    gitleaks = json.loads(require("tranche-02/gitleaks.json").read_text())
    if not isinstance(gitleaks, list) or not gitleaks:
        raise AssertionError("Gitleaks did not detect the synthetic fixture secret")

    syft = json.loads(require("tranche-02/syft.spdx.json").read_text())
    if "packages" not in syft:
        raise AssertionError("Syft output lacks SPDX packages")

    grype = json.loads(require("tranche-02/grype.json").read_text())
    if "matches" not in grype:
        raise AssertionError("Grype output lacks matches field")

    semgrep = json.loads(require("tranche-02/semgrep.json").read_text())
    if not semgrep.get("results"):
        raise AssertionError("Semgrep did not detect the synthetic unsafe construct")

    osv = json.loads(require("tranche-02/osv.json").read_text())
    if not isinstance(osv, dict):
        raise AssertionError("OSV-Scanner output is not a JSON object")

    print(json.dumps({"status": "passed", "validated_files": expected}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
