---
name: pre-commit
category: testing-quality
subcategory: git-hooks
status: approved
type: framework
canonical_repo: https://github.com/pre-commit/pre-commit
website: https://pre-commit.com
pinned_version: 4.6.1 (PyPI, published 2026-07-21)
license: MIT
score: 85
confidence: high
tested: true
last_verified: 2026-07-23
---

# pre-commit — multi-language git hook manager

## What it does
Manages git hooks declaratively (`.pre-commit-config.yaml`), installing and
running linters/formatters/scanners (ruff, gitleaks, prettier, …) at commit
time and in CI, with hook repos pinned by revision.

## When to use
- Baseline hygiene for every repo: format, lint, and secret-scan before
  every commit — highest-leverage 30-minute setup a solo founder can do

## When not to use
- As a replacement for CI (hooks can be skipped with `--no-verify`; CI must
  re-run the same checks)

## Evidence
- License MIT `[V]` — PyPI metadata (2026-07-23)
- Latest 4.6.1 published 2026-07-21 `[V]` — PyPI JSON API
- Maintainer: Anthony Sottile (asottile), long-running project with high
  individual concentration `[C]` — bus-factor noted
- De facto standard; hook ecosystem spans hundreds of tools `[C]`

## Validation results (sandboxed test, 2026-07-23)
- `pip install pre-commit==4.6.1`; configured a `repo: local` hook running
  ruff in a fresh git repo; `pre-commit run --all-files` executed the hook
  and correctly failed on planted lint errors (exit 1)
- Remote-hook fetching (cloning pinned hook repos from GitHub) was not
  testable offline — marked untested; it is the standard usage mode `[U]`

## Security findings
- Hook repos execute code on your machine: **pin hooks by full SHA or tag**
  and review before updating; `pre-commit autoupdate` changes should be
  diffed like dependencies `[I]`

## Legal / licensing findings
- MIT — commercial use permitted. Individual hooks carry their own
  licenses.

## Installation
`pip install pre-commit==4.6.1 && pre-commit install`

## Agent integration
Agents should run `pre-commit run --all-files` before proposing commits;
autoupdate PRs are fine but require human merge.

## Required human review
Every hook addition/update (it's arbitrary code execution at commit time).

## Score notes
Functional 17/20 · Security 16/20 (hook supply-chain surface) · Maintenance
13/15 (single-maintainer concentration) · Docs 9/10 · License 10/10 ·
Reproducibility 9/10 · Provenance 7/10 · Integration 4/5 → **85**
