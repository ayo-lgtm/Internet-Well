---
name: OpenAPI Specification (OAS)
category: product-strategy
subcategory: api-design-standard
status: approved
type: standard
canonical_repo: https://github.com/OAI/OpenAPI-Specification
website: https://www.openapis.org
pinned_version: 3.2.0 (2025-09-19)
license: Apache-2.0
score: null
confidence: high
tested: not-applicable
last_verified: 2026-07-23
---

# OpenAPI Specification — the standard for describing HTTP APIs

## What it does
Language-agnostic contract format for HTTP APIs. One spec file drives
documentation, client/server codegen, mock servers, contract tests, and
security scanning (e.g. ZAP API scans import OpenAPI).

## When to use
- Design-first API development for any founder product exposing an API;
  the spec becomes the single source of truth across eng, docs, and tests
- Machine-readable input for AI agents generating clients, tests, or docs

## When not to use
- Non-HTTP interfaces (gRPC → protobuf; events → AsyncAPI, Phase 3
  candidate)

## Evidence
- License Apache-2.0 `[V]` — repository (2026-07-23)
- Latest spec release 3.2.0, 2025-09-19 `[V]` — repo releases
- Governance: OpenAPI Initiative, a Linux Foundation collaborative project
  with a Technical Steering Committee meeting in the open `[V]` — repo
  governance docs; strong institutional provenance
- Ecosystem adoption is pervasive (documented tooling across every major
  language) `[C]`

## Validation results
- Standard document; not executable. Version/governance verified.

## Legal / licensing findings
- Apache-2.0 spec text; your API descriptions are your own. "OpenAPI" is
  an LF trademark — don't imply certification.

## Installation
Author `openapi.yaml` in-repo; validate with an OSS validator (e.g.
Redocly CLI or Spectral — Phase 2 validation candidates).

## Agent integration
Agents should treat the spec file as the API contract: propose spec diffs
first, then code, keeping the two in sync.

## Required human review
API design decisions; breaking-change review before publishing spec
changes.

## Score notes
Not scored (standard; execution dimensions inapplicable).
