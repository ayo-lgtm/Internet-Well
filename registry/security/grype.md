---
name: Grype
category: security-engineering
subcategory: vulnerability-scanning
status: approved
type: tool
canonical_repo: https://github.com/anchore/grype
website: https://anchore.com/opensource
pinned_version: v0.116.0 (commit 3b014b00097d43933e5cce485e744db8289a406f)
license: Apache-2.0
score: 85
confidence: high
tested: false
last_verified: 2026-07-23
---

# Grype — vulnerability scanner for images, filesystems, and SBOMs

## What it does
Matches packages (from images, directories, or a Syft SBOM) against known
vulnerability data across OS and language ecosystems; supports EPSS/KEV
risk prioritization and OpenVEX filtering.

## When to use
- Scanning a pinned Syft SBOM in CI — decouples inventory from matching and
  makes scans reproducible
- Complement or alternative to Trivy where the Syft SBOM pipeline is used

## When not to use
- Misconfiguration/IaC scanning (Trivy or dedicated tools)
- Air-gapped use without a mirrored vulnerability DB

## Evidence
- License Apache-2.0 `[V]` — repository license indicator (2026-07-23)
- Latest release v0.116.0, 2026-07-16, commit 3b014b0 `[V]` — Go module
  proxy metadata
- Corporate maintainer: Anchore `[V]`; active (2,300+ commits) `[V]`
- EPSS/KEV/OpenVEX support `[M]` — documented features, not exercised

## Validation results
- Not execution-tested this pass; pinned installs available
  (`go install github.com/anchore/grype@v0.116.0`, Docker, Homebrew) `[V]`

## Security findings
- Downloads vulnerability DB at runtime (configurable/mirrorable) `[M]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- Apache-2.0 — commercial use, modification, redistribution, SaaS permitted.

## Installation
`go install github.com/anchore/grype@v0.116.0`; Homebrew; Docker
`anchore/grype:v0.116.0`.

## Agent integration
JSON output, `--fail-on <severity>` for deterministic CI gating. Safe for
autonomous scanning; suppressions (VEX or ignore rules) need human sign-off.

## Required human review
Finding triage and any suppression/acceptance of risk.

## Score notes
Functional 18/20 · Security 16/20 · Maintenance 14/15 · Docs 8/10 ·
License 10/10 · Reproducibility 8/10 · Provenance 8/10 · Integration 3/5
→ **85**
