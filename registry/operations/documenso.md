---
name: Documenso
category: operations-legal
subcategory: e-signature
status: approved-with-restrictions
type: tool
canonical_repo: https://github.com/documenso/documenso
website: https://documenso.com
pinned_version: v2.15.0 (2026-07-21)
license: AGPL-3.0 (enterprise plan exists; verify per-directory licensing at pin)
score: 76
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Documenso — open-source document signing

## What it does
Self-hostable DocuSign alternative: upload documents, place signature
fields, send for signing, collect legally-attributable e-signatures with
audit trails; API and embedding support.

## When to use
- Signing NDAs, contractor agreements, and customer contracts (pairs
  naturally with Common Paper templates —
  `registry/operations/common-paper-csa.md`) without per-envelope SaaS
  fees, keeping signed documents on your infrastructure

## When not to use / restrictions
- AGPL-3.0 network copyleft; an enterprise plan exists — audit the repo
  for commercial-licensed directories/markers at your pinned version
  before building on advanced features `[M→RECHECK]` (README references
  an enterprise tier; boundary not verified this pass)
- **E-signature legal validity varies by jurisdiction and document type**
  (some documents require notarization/wet ink). Validity of
  self-hosted signatures for your use cases is a counsel question, not
  a software feature `[I]`
- Young project relative to the function's seriousness; keep signed-PDF
  archives backed up independently (restic) `[I]`

## Evidence
- License AGPL-3.0 `[V]` — repository (2026-07-23)
- Latest v2.15.0, 2026-07-21; active (53 releases) `[V]`
- Corporate maintainer: Documenso Inc. `[C]`

## Validation results
- Not execution-tested (Next.js+DB deployment; Docker unavailable).
  RECHECK.

## Security findings
- Holds legally significant documents and signer PII — hardening,
  backups, and access control are compliance-relevant `[I]`
- No unresolved material advisories located; Scorecard `[U]`

## Legal / licensing findings
- AGPL-3.0 core: commercial/SaaS use permitted with network-copyleft
  obligations; enterprise boundary unverified (RECHECK).

## Installation
Official Docker compose pinned to v2.15.0.

## Agent integration
API for envelope creation from templates; **agents must never send
documents for signature autonomously** — every outbound signing request
is human-approved.

## Required human review
Enforceability per jurisdiction/document type (counsel); every signing
request; retention policy for signed documents.

## Score notes
Functional 16/20 · Security 13/20 · Maintenance 13/15 · Docs 8/10 ·
License 7/10 · Reproducibility 7/10 · Provenance 6/10 · Integration 4/5
→ **76**
