---
name: Twenty
category: sales-support
subcategory: crm
status: approved-with-restrictions
type: tool
canonical_repo: https://github.com/twentyhq/twenty
website: https://twenty.com
pinned_version: v2.23.0 (2026-07-22)
license: AGPL-3.0 (core); files marked "@license Enterprise" under Twenty Commercial License
score: 76
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Twenty — modern open-source CRM

## What it does
Self-hosted CRM (contacts, companies, pipelines, notes, email sync) with a
modern data-model-first UI; positioned as an open Salesforce alternative.

## When to use
- Founder sales pipeline once spreadsheets break down, with CRM data
  self-hosted and exportable

## When not to use / restrictions
- **Dual-license by file marker**: enterprise files are identified only by
  a `/* @license Enterprise */` header, not a directory `[V]` — LICENSE
  read during verification. Production use of those files requires a
  subscription; auditing which features touch them is **harder than a
  directory-based carve-out** — a material compliance burden for a solo
  founder building on it.
- AGPL-3.0 network copyleft on modified core.
- Young project with fast-moving schema; check upgrade/migration notes
  before committing business data `[I]`

## Evidence
- License structure `[V]` — LICENSE file: AGPLv3 + Commercial-by-marker
  (2026-07-23)
- Latest v2.23.0, 2026-07-22; very active `[V]` — repo page
- Corporate maintainer: Twenty (YC-backed startup) `[C]`

## Validation results
- Not execution-tested this pass (Phase 2 docker test).

## Security findings
- CRM data is customer PII — your data-protection surface `[I]`; no
  unresolved material advisories located; Scorecard `[U]`

## Legal / licensing findings
- AGPL-3.0 core: commercial/SaaS use permitted with network-copyleft
  obligations on modifications. Enterprise-marked files: development/test
  use free, production use requires subscription `[V]`.

## Installation
Official docker-compose pinned to v2.23.0.

## Agent integration
GraphQL/REST APIs; agent data-entry (logging calls, enriching contacts) is
low-risk; outbound communication remains human-approved.

## Required human review
Enterprise-file audit for your deployed feature set; data migration plan.

## Score notes
Functional 16/20 · Security 13/20 · Maintenance 13/15 · Docs 7/10 ·
License 6/10 (marker-based dual licensing) · Reproducibility 7/10 ·
Provenance 6/10 · Integration 4/5 → **76**

## Alternatives note
EspoCRM (AGPL-3.0, longer history) is a Phase 2 validation candidate for
founders preferring a mature option over a modern UI.
