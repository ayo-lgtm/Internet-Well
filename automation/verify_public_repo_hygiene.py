#!/usr/bin/env python3
"""Fail CI when the public repository contains high-risk private artifacts."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_EXACT = {
    ".env",
    ".env.local",
    ".env.production",
    "credentials.json",
    "service-account.json",
    "secrets.json",
}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}
HIGH_SIGNAL_PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github-classic-token": re.compile(r"\bghp_[A-Za-z0-9]{30,}\b"),
    "github-fine-grained-token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "openai-style-secret": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
}
KNOWN_PUBLIC_FIXTURES = {
    "AKIAIOSFODNN7EXAMPLE",
    "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
}
TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".yml", ".yaml", ".toml", ".py", ".js", ".ts", ".tsx", ".jsx", ".sh", ".ini", ".cfg"
}


def tracked_files() -> list[Path]:
    proc = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=True
    )
    return [ROOT / line for line in proc.stdout.splitlines() if line.strip()]


def main() -> int:
    problems: list[str] = []
    for path in tracked_files():
        rel = path.relative_to(ROOT)
        name = path.name
        if name in FORBIDDEN_EXACT or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            problems.append(f"forbidden tracked secret/config file: {rel}")
            continue
        if rel.parts and rel.parts[0] == "assessments":
            problems.append(f"private assessment artifacts must not be tracked publicly: {rel}")
        if path.suffix.lower() not in TEXT_SUFFIXES or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for fixture in KNOWN_PUBLIC_FIXTURES:
            text = text.replace(fixture, "")
        for label, pattern in HIGH_SIGNAL_PATTERNS.items():
            if pattern.search(text):
                problems.append(f"possible {label} in {rel}")

    required = [
        "README.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "LICENSE",
        "LICENSE-CONTENT",
        "LICENSES.md",
    ]
    for required_path in required:
        if not (ROOT / required_path).is_file():
            problems.append(f"missing public repository document: {required_path}")

    scope_path = ROOT / "LICENSES.md"
    if scope_path.is_file():
        scope = scope_path.read_text(encoding="utf-8")
        for required_scope in ("Apache License 2.0", "CC-BY-4.0", "Third-party"):
            if required_scope not in scope:
                problems.append(f"LICENSES.md does not define {required_scope} scope")

    if problems:
        print("Public repository hygiene verification failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Public repository hygiene verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
