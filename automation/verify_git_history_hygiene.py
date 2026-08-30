#!/usr/bin/env python3
"""Fail when reachable Git history contains a high-confidence secret pattern."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HIGH_SIGNAL_PATTERNS = {
    "private-key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "github-token": re.compile(rb"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"),
    "github-fine-grained-token": re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    "aws-access-key": re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "openai-style-secret": re.compile(rb"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    "slack-token": re.compile(rb"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "google-api-key": re.compile(rb"\bAIza[0-9A-Za-z_-]{35}\b"),
}

KNOWN_PUBLIC_FIXTURES = (
    b"AKIAIOSFODNN7EXAMPLE",
    b"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
)


def missing_objects() -> list[str]:
    proc = subprocess.run(
        ["git", "rev-list", "--objects", "--all", "--missing=print"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return [line[1:].split(" ", 1)[0] for line in proc.stdout.splitlines() if line.startswith("?")]


def scan_history() -> list[tuple[str, str, str]]:
    proc = subprocess.Popen(
        ["git", "log", "--all", "--patch", "--no-ext-diff", "--no-color", "--format=commit %H"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert proc.stdout is not None
    current_commit = "unknown"
    current_path = "unknown"
    findings: set[tuple[str, str, str]] = set()

    for raw_line in proc.stdout:
        if raw_line.startswith(b"commit "):
            current_commit = raw_line.removeprefix(b"commit ").strip().decode("ascii", "replace")
        elif raw_line.startswith(b"+++ b/"):
            current_path = raw_line.removeprefix(b"+++ b/").strip().decode("utf-8", "replace")

        line = raw_line
        for fixture in KNOWN_PUBLIC_FIXTURES:
            line = line.replace(fixture, b"")
        for label, pattern in HIGH_SIGNAL_PATTERNS.items():
            if pattern.search(line):
                findings.add((label, current_commit, current_path))

    stderr = proc.stderr.read() if proc.stderr is not None else b""
    return_code = proc.wait()
    if return_code:
        raise RuntimeError(stderr.decode("utf-8", "replace").strip() or "git history scan failed")
    return sorted(findings)


def main() -> int:
    missing = missing_objects()
    if missing:
        print(
            "Git history hygiene verification could not run: "
            f"{len(missing)} reachable objects are missing. Use a full checkout/fetch."
        )
        return 2

    findings = scan_history()
    if findings:
        print("Git history hygiene verification failed:")
        for label, commit, path in findings:
            print(f"- possible {label} in {path} at {commit}")
        print("Values are intentionally redacted. Rotate any live credential before rewriting history.")
        return 1

    print("Git history hygiene verification passed: no high-confidence secret patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
