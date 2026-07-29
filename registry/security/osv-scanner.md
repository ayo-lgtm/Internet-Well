---
name: OSV-Scanner
category: security
subcategory: dependency-vulnerability-scanning
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/google/osv-scanner
website: https://google.github.io/osv-scanner/
pinned_version: v2.3.8
license: Apache-2.0
score: 87
confidence: high
tested: true
last_verified: 2026-07-29
---

# OSV-Scanner — ecosystem-native dependency vulnerability evidence

## What it does

Scans supported manifests, lockfiles, SBOMs, containers, and package inventories against the Open Source Vulnerabilities database. It is strongest when exact resolved package versions are available.

## When to use

- Repository CI for supported package ecosystems and lockfiles.
- Dependency review where OSV identifiers and affected-version ranges are useful.
- SBOM or container analysis as an additional ecosystem-native signal.

## When not to use

- As proof that unmatched vulnerabilities do not exist.
- As a replacement for source review, runtime testing, exploitability analysis, or vendor advisories.
- Where manifests do not contain resolved versions and no reliable inventory can be produced.

## Evidence

- Canonical Google-maintained repository and Apache-2.0 license `[V]`.
- Exact evaluated release `v2.3.8` `[V]`.
- Tranche 02 installed the exact pin, captured version evidence, and exercised a harmless fixture in CI `[V]`.
- Coverage varies by ecosystem, manifest quality, lockfile state, and OSV data availability `[V/I]`.

## Validation results

The dedicated Tranche 02 GitHub Actions workflow completed successfully on 2026-07-29. The workflow required exact-version installation and failed on version mismatch. It retained version and scan evidence as CI artifacts.

## Security findings

- Vulnerability matching is evidence, not a determination of reachability or exploitability.
- Partial parsing, unsupported formats, stale data, timeouts, or skipped targets must be reported as incomplete rather than clean.
- Scanned dependency names and versions may be sensitive in private products; restrict report retention and access where necessary.

## Legal / licensing findings

Apache-2.0 permits commercial use, modification, redistribution, and SaaS use with preservation of notices and includes a patent grant. Vulnerability-source data may have separate attribution or reuse terms when republished.

## Installation

Use the official release artifact or container pinned to `v2.3.8`. Record the binary checksum or image digest in CI.

## Agent integration

Suitable for read-only automated scanning with machine-readable output. Agents must preserve unsupported-target, timeout, database, and parse warnings and must not automatically suppress or dismiss findings.

## Required human review

A developer or security reviewer must determine affected-version accuracy, runtime reachability, exploitability, compensating controls, remediation priority, and any suppression.

## Score notes

Functional 18/20 · Security 17/20 · Maintenance 14/15 · Documentation 9/10 · License 10/10 · Reproducibility 9/10 · Provenance 7/10 · Integration 3/5 → **87**.
