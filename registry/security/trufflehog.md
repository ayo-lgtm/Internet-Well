---
name: TruffleHog
category: security
subcategory: verified-secret-detection
status: approved-with-restrictions
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/trufflesecurity/trufflehog
website: https://trufflesecurity.com/trufflehog
pinned_version: v3.95.2
license: AGPL-3.0-only
score: 80
confidence: high
tested: true
last_verified: 2026-07-29
---

# TruffleHog — verified-secret investigation

## What it does
Scans repositories and other supported sources for secret-shaped material and can verify some candidates against external providers.

## When to use
Use as an additional high-confidence investigation layer when Gitleaks alone is insufficient and provider verification is justified.

## When not to use
Do not enable live verification automatically on sensitive repositories. Do not treat a detection as proof that a credential is active, authorized, or exploitable.

## Evidence
- Canonical repository and AGPL-3.0-only license `[V]`.
- Exact evaluated release `v3.95.2` `[V]`.
- Tranche 02 installed the exact pin and exercised safe CLI behavior with live verification disabled `[V]`.

## Validation results
The dedicated Tranche 02 workflow completed successfully and retained exact-version evidence.

## Security findings
Provider verification may transmit candidate credentials or metadata to third parties. Reports may contain sensitive fragments and require restricted retention. History rewriting and credential rotation are consequential operations.

## Legal / licensing findings
AGPL-3.0-only requires legal review for modified, network-served, or redistributed deployments. SaaS and internal-use boundaries must be analyzed for the intended implementation.

## Installation
Use the official release pinned to `v3.95.2` and retain checksum evidence.

## Agent integration
Agents may run read-only scans with verification disabled. Provider verification, history rewriting, credential revocation, and report sharing require explicit approval.

## Required human review
A security reviewer must approve provider verification, report access, credential rotation, suppression, repository-history changes, and AGPL obligations.

## Score notes
Functional 17/20 · Security 14/20 · Maintenance 14/15 · Documentation 8/10 · License 5/10 · Reproducibility 9/10 · Provenance 8/10 · Integration 5/5 → **80**.
