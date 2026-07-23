---
name: Semgrep CE (Community Edition)
category: security
subcategory: sast
status: approved-with-restrictions
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/semgrep/semgrep
website: https://semgrep.dev
pinned_version: 1.171.0 (PyPI, published 2026-07-22)
license: LGPL-2.1-only (engine); official rules are NOT open source — Semgrep Rules License v1.0
score: 78
confidence: high
tested: true
last_verified: 2026-07-23
---

# Semgrep CE — pattern-based static analysis (SAST)

## What it does
Fast semantic static analysis across 30+ languages using patterns that look
like source code. Finds bug classes, insecure API usage, and policy
violations; runs locally and in CI.

## When to use
- CI SAST for a founder's own codebase using official rules for **internal
  business purposes** (explicitly permitted)
- Writing custom organization-specific rules (your own rules are yours)

## When not to use / restrictions
- **Do not** embed the official Semgrep-maintained rules in a product or
  service you sell, or redistribute them: the Semgrep Rules License v1.0
  (introduced December 2024) limits rules to internal, non-competing,
  non-SaaS use `[C]` (semgrep.dev/docs/licensing; independent coverage of
  the 2024–2025 licensing change and the resulting Opengrep fork)
- If you need fully-OSS rules + engine for a security product, evaluate the
  **Opengrep** fork (LGPL, vendor coalition, Jan 2025) — currently
  `experimental` status, not yet validated in this registry

## Evidence
- Engine license LGPL-2.1 `[V]` — repository license indicator (2026-07-23)
- Latest version 1.171.0 published 2026-07-22 `[V]` — PyPI JSON API
- Rules license: "Semgrep Rules License v. 1.0" `[V]` — LICENSE file of
  semgrep/semgrep-rules; restriction terms `[C]` — Semgrep licensing docs +
  multiple independent analyses (Josh Grossman 2025-01-28; Opengrep launch
  press coverage)
- Corporate maintainer: Semgrep, Inc. `[V]`; active development (release
  cadence ~weekly) `[V]` — PyPI release history

## Validation results (sandboxed test, 2026-07-23)
- `pip install semgrep==1.171.0` in a fresh venv — reproducible;
  `semgrep --version` → 1.171.0
- With a local rule file and `--metrics=off`, scanning a sample containing
  `subprocess.call(cmd, shell=True)` produced exactly the expected finding
  (JSON output, correct line) with zero network egress
- `--config auto` failed in the offline sandbox — confirms registry configs
  require network access; use local rules for hermetic CI

## Security findings
- **Telemetry**: using registry configs (e.g. `--config auto`) sends usage
  metrics to semgrep.dev; disable with `--metrics=off` and use local rule
  files for zero egress `[M]` — documented behavior; verify per version
- No unresolved material advisories found; Scorecard unretrievable `[U]`

## Legal / licensing findings
- LGPL-2.1 engine: commercial and SaaS use permitted; modifications to the
  engine itself must be released under LGPL if distributed
- Official rules: internal use only; no redistribution, no competing
  product/SaaS embedding `[C]`. Rules you author are not encumbered.
- This is an open-core project; features like Semgrep AppSec Platform,
  Assistant, and Pro rules are commercial.

## Installation
`pip install semgrep==1.171.0` (binary wheels; Python ≥3.10), Homebrew, or
Docker `semgrep/semgrep`.

## Agent integration
Run with pinned version, `--metrics=off`, JSON/SARIF output. For agent
pipelines, prefer explicit local rule files over `--config auto` to avoid
network dependence and telemetry.

## Required human review
License boundary decisions (anything that ships rules outward); triage and
suppression of findings.

## Score notes
Functional 18/20 · Security 15/20 (telemetry default with registry configs,
Scorecard unknown) · Maintenance 14/15 · Docs 9/10 · License 6/10 (engine
fine; official rules non-OSS — material restriction) · Reproducibility 9/10 ·
Provenance 8/10 · Integration 4/5 → **78** (restriction reflected in status)
