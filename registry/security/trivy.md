---
name: Trivy
category: security-engineering
subcategory: dependency-scanning-sbom
status: approved
type: tool
canonical_repo: https://github.com/aquasecurity/trivy
website: https://trivy.dev
pinned_version: v0.72.0 (commit 8a32853686209a428179bb3a1688802b25691564)
license: Apache-2.0
score: 89
confidence: high
tested: false
last_verified: 2026-07-23
---

# Trivy — vulnerability, misconfiguration, secret, and SBOM scanner

## What it does
Scans container images, filesystems, git repos, and IaC for known
vulnerabilities (OS + language packages), misconfigurations, exposed
secrets, and license issues; generates SBOMs (SPDX, CycloneDX).

## When to use
- Default CI dependency/container scanner for a solo founder: one binary
  covering vuln scanning, IaC misconfig, and SBOM generation
- Pre-deploy image scanning and scheduled re-scans of shipped images

## When not to use
- As a DAST tool (no runtime testing — pair with OWASP ZAP)
- Where an air-gapped environment cannot fetch its vulnerability DB
  (offline operation requires explicit DB mirroring)

## Evidence
- License Apache-2.0 `[V]` — repository page license indicator (2026-07-23)
- Latest release v0.72.0, 2026-06-30, commit 8a32853 `[V]` — Go module proxy
  metadata with VCS hash
- Corporate maintainer: Aqua Security `[V]` — repo org, trivy.dev
- Broad production adoption (default scanner in multiple registries/CIs,
  e.g. Harbor, GitLab integrations) `[C]` — independent docs of those
  projects; not re-verified individually this pass
- Not archived; active commit history (4,100+ commits) `[V]`

## Validation results
- Not execution-tested this pass (Go compile of the full scanner exceeded
  the session budget; official binaries could not be fetched because
  GitHub release-asset downloads were blocked by the research environment's
  network policy). Marked for Phase 2 execution test.
- Installation reproducibility: pinned `go install` and versioned Docker
  images available `[V]` (methods documented; not run)

## Security findings
- Runtime behavior: downloads its vulnerability DB from ghcr.io on first
  run `[M]` (documented); code being scanned is not uploaded anywhere `[M]`
- Vendor (Aqua) publishes a security policy for the repo `[M]` — presence
  not independently confirmed this pass (API rate-limited); on recheck list
- OpenSSF Scorecard unretrievable from this environment `[U]`

## Legal / licensing findings
- Apache-2.0: commercial use, modification, redistribution, SaaS permitted;
  NOTICE/attribution preservation required; patent grant included.
- The vulnerability database content aggregates public advisory sources;
  redistribution of the DB itself has its own terms `[U]` — only relevant
  if you republish the DB.

## Installation
Pinned Docker image (`aquasec/trivy:0.72.0`), distro packages, or
`go install github.com/aquasecurity/trivy/cmd/trivy@v0.72.0`.

## Agent integration
Safe for autonomous read-only scanning; JSON/SARIF output (`-f json`,
`-f sarif`); deterministic exit codes via `--exit-code`. Pin the version and
DB snapshot for reproducible CI results.

## Required human review
Triage of findings (false-positive rate on language packages is nontrivial);
any decision to suppress a finding (`.trivyignore`) must be human-approved.

## Score notes
Functional 19/20 · Security 17/20 (Scorecard unknown; DB-fetch runtime dep) ·
Maintenance 14/15 · Docs 9/10 · License 10/10 · Reproducibility 8/10 (not
executed this pass) · Provenance 8/10 · Integration 4/5 → **89**
