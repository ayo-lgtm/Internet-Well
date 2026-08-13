#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "automation" / "screenshot_integrations.py"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env["INTERNET_WELL_ROOT"] = str(ROOT)
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def must(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    listed = run("list")
    must(listed.returncode == 0, listed.stderr)
    rows = json.loads(listed.stdout)
    ids = {row["id"] for row in rows}
    must({"awesome-claude-skills", "playwright-mcp"}.issubset(ids), "missing screenshot integrations")

    floating = run("plan", "playwright-mcp", "--ref", "latest")
    must(floating.returncode != 0, "floating ref should fail")
    must("Floating refs are prohibited" in floating.stderr, floating.stderr)

    skills = run("plan", "awesome-claude-skills", "--ref", "0123456789abcdef0123456789abcdef01234567")
    must(skills.returncode == 0, skills.stderr)
    skills_payload = json.loads(skills.stdout)
    must(skills_payload["integration"]["id"] == "awesome-claude-skills", "wrong skill integration")
    must(skills_payload["planned_clone"][0:2] == ["git", "clone"], "missing clone plan")
    must("copy only individually approved directories" in skills_payload["post_clone_rule"].lower(), "missing selective-adoption rule")

    pw = run("plan", "playwright-mcp", "--ref", "0.0.42")
    must(pw.returncode == 0, pw.stderr)
    pw_payload = json.loads(pw.stdout)
    shell = pw_payload["planned_command_shell"]
    must("@playwright/mcp@0.0.42" in shell, shell)
    must("latest" not in shell.lower(), shell)

    blocked = run("install", "playwright-mcp", "--ref", "0.0.42")
    must(blocked.returncode != 0, "install without approval should fail")
    must("--approve" in blocked.stderr, blocked.stderr)

    print("Screenshot integration tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
