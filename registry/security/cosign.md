---
name: Cosign
category: security
subcategory: artifact-signing-attestation
status: approved-with-restrictions
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/sigstore/cosign
website: https://docs.sigstore.dev/cosign/
pinned_version: v3.0.6
license: Apache-2.0
score: 86
confidence: high
tested: true
last_verified: 2026-07-29
---

# Cosign — artifact signatures and attestations

## What it does
Verifies and creates signatures and attestations for container images and other artifacts.

## When to use
Use where release provenance, artifact identity, issuer policy, or signed attestations are required.

## When not to use
Do not treat a valid signature as proof that an artifact is secure, appropriate, or vulnerability-free. Do not sign production artifacts without approved identities, keys, issuers, and policy.

## Evidence
- Canonical Sigstore project and Apache-2.0 license `[V]`.
- Exact evaluated release `v3.0.6` `[V]`.
- Tranche 02 installed the exact pin and exercised the CLI without signing production artifacts `[V]`.

## Validation results
The dedicated Tranche 02 workflow completed successfully and retained exact-version evidence.

## Security findings
Trust roots, expected identities, issuers, transparency-log behavior, timestamps, offline bundles, and failure handling must be explicit. Verification against an unpinned tag or weak identity policy is insufficient.

## Legal / licensing findings
Apache-2.0 permits commercial use with notice preservation and includes a patent grant.

## Installation
Use the official binary or image pinned to `v3.0.6` and retain its checksum or digest.

## Agent integration
Agents may perform read-only verification against an approved policy. Signing, key creation, identity changes, and trust-policy changes require explicit authorization.

## Required human review
A competent security reviewer must approve signing identities, issuers, trust roots, key custody, transparency-log policy, offline behavior, and every production exception.

## Score notes
Functional 18/20 · Security 17/20 · Maintenance 14/15 · Documentation 9/10 · License 10/10 · Reproducibility 8/10 · Provenance 7/10 · Integration 3/5 → **86**.
