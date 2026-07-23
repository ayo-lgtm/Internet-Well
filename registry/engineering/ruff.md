---
name: Ruff
category: engineering
subcategory: linting-formatting-python
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/astral-sh/ruff
website: https://docs.astral.sh/ruff/
pinned_version: 0.15.22 (PyPI, published 2026-07-16)
license: MIT
score: 88
confidence: high
tested: true
last_verified: 2026-07-23
---

# Ruff — Python linter and formatter

## What it does
Extremely fast Rust-based Python linter + formatter reimplementing the
rule sets of flake8, isort, pyupgrade, and much of pylint, plus a
Black-compatible formatter — one tool replacing four.

## When to use
- Default lint/format for all Python code; pre-commit + CI

## When not to use
- Deep type checking (pair with mypy/pyright); non-Python code

## Evidence
- License MIT `[V]` — PyPI `license_expression: MIT` (2026-07-23)
- Latest 0.15.22 published 2026-07-16; very frequent releases `[V]` — PyPI
- Corporate maintainer: Astral (VC-funded tooling company; also uv) `[C]`
- Adopted by major Python projects (FastAPI, pandas, others) `[C]` —
  their repo configs; context

## Validation results (sandboxed test, 2026-07-23)
- `pip install ruff==0.15.22`; linted a file with two unused imports:
  exactly 2 findings, exit 1 — correct and offline
- Also exercised via pre-commit local hook (see pre-commit record)

## Security findings
- No telemetry; runs offline `[V]` — observed
- Pre-0.x version number belies maturity, but breaking rule changes do
  land between minors — pin the version `[I]`

## Legal / licensing findings
- MIT — commercial use, SaaS, redistribution permitted.

## Installation
`pip install ruff==0.15.22` (binary wheels; no Rust toolchain needed)

## Agent integration
`ruff check --output-format json` and `--fix` for safe autofixes;
agents should not auto-apply `--unsafe-fixes` without review.

## Required human review
Rule-set selection; any `--unsafe-fixes` application.

## Score notes
Functional 19/20 · Security 17/20 · Maintenance 14/15 · Docs 9/10 ·
License 10/10 · Reproducibility 10/10 · Provenance 6/10 (single-vendor
concentration) · Integration 3/5 → **88**
