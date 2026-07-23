---
name: Syft
category: security-engineering
subcategory: sbom-generation
status: approved
type: tool
canonical_repo: https://github.com/anchore/syft
website: https://anchore.com/opensource
pinned_version: v1.49.0 (commit 29fd7d0dec81cf03e0a1194a1985c7c893bb2396)
license: Apache-2.0
score: 86
confidence: high
tested: true
last_verified: 2026-07-23
---

# Syft — SBOM generation for images and filesystems

## What it does
CLI and Go library that catalogs packages in container images, filesystems,
and archives, producing SBOMs in SPDX, CycloneDX, and Syft JSON formats.
Pairs natively with Grype for vulnerability matching.

## When to use
- Generating an SBOM per release artifact (increasingly expected by
  enterprise customers and some regulation)
- Feeding a pinned SBOM into Grype for reproducible vulnerability scans

## When not to use
- As a vulnerability scanner itself (it only inventories; use Grype/Trivy)
- Deep license-compliance analysis of source code (use ScanCode Toolkit)

## Evidence
- License Apache-2.0 `[V]` — repository license indicator (2026-07-23)
- Latest release v1.49.0, 2026-07-20, commit 29fd7d0 `[V]` — Go module
  proxy metadata (verifiable provenance)
- Corporate maintainer: Anchore; regular public community meetings `[M]`
- Supports signed SBOM attestations via in-toto/cosign `[M]` — documented;
  not exercised this pass

## Validation results (sandboxed test, 2026-07-23, Phase 2)
- Built from source at v1.49.0 via
  `go install github.com/anchore/syft/cmd/syft@v1.49.0` (module proxy,
  verifiable hash) — reproducible
- Generated an SPDX SBOM from a real npm project directory: exit 0, valid
  `SPDX-2.3` JSON produced (manifest-level packages cataloged for the
  minimal fixture). Fully offline.
- The project's curl|sh installer exists but pinned package-manager
  installs are preferred per methodology

## Security findings
- Operates offline on local targets; no code egress `[M]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- Apache-2.0 — commercial use, modification, redistribution, SaaS permitted.

## Installation
`go install github.com/anchore/syft/cmd/syft@v1.49.0`; Homebrew; Docker
`anchore/syft:v1.49.0`.

## Agent integration
Deterministic CLI, JSON output; safe for autonomous SBOM generation in CI.
Pin version; store SBOMs alongside release artifacts.

## Required human review
None for generation; interpretation of SBOM contents for customer/legal
requests should be human-reviewed.

## Score notes
Functional 18/20 · Security 16/20 · Maintenance 14/15 · Docs 8/10 ·
License 10/10 · Reproducibility 8/10 · Provenance 8/10 · Integration 4/5
→ **86**
