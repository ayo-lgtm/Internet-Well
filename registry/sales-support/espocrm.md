---
name: EspoCRM
category: sales-support
subcategory: crm
status: approved-with-restrictions
type: tool
canonical_repo: https://github.com/espocrm/espocrm
website: https://www.espocrm.com
pinned_version: 10.0.3 (2026-07-17)
license: AGPL-3.0
score: 79
confidence: medium
tested: false
last_verified: 2026-07-23
---

# EspoCRM — mature self-hosted CRM

## What it does
Full CRM: leads, contacts, opportunities, campaigns, support cases, with
REST API and strong in-app customization (entities, layouts, workflows).
The "boring, proven" counterpart to Twenty's modern take.

## When to use
- A founder wanting a stable, long-lived CRM on a plain PHP+MySQL/
  Postgres stack (cheap hosting, well-understood ops)
- Heavier customization needs without code (entity manager)

## When not to use / restrictions
- AGPL-3.0 network copyleft on modifications you serve
- Extensions marketplace includes paid proprietary add-ons (open-core at
  the edges — the core is fully AGPL) `[C]`
- UI is functional rather than modern; if that matters for daily use,
  compare Twenty (`registry/sales-support/twenty.md`) before committing
  data `[I]`

## Evidence
- License AGPL-3.0 `[V]` — repository (2026-07-23)
- Latest 10.0.3, 2026-07-17; 302 releases, 22,900+ commits — long,
  steady history `[V]`
- Maintainer: EspoCRM company (Letrium Ltd) `[C]`

## Validation results
- Not execution-tested (PHP+DB server app; Docker unavailable). RECHECK.

## Security findings
- CRM = customer PII surface; same hardening rules as Chatwoot/Twenty
  `[I]`; no unresolved material advisories located; Scorecard `[U]`

## Legal / licensing findings
- AGPL-3.0: commercial/SaaS use permitted; source obligations on served
  modifications; paid extensions are separately licensed — track what
  you install.

## Installation
Official Docker image or tarball, pinned to 10.0.3; PHP 8.3–8.5,
MySQL 8+/Postgres 15+.

## Agent integration
REST API for records/activities; agent data-hygiene (dedupe, enrichment
drafts) with human approval on outbound anything.

## Required human review
Data-protection posture; extension licenses; migration plan in/out.

## Score notes
Functional 17/20 · Security 13/20 · Maintenance 14/15 · Docs 8/10 ·
License 7/10 · Reproducibility 7/10 · Provenance 6/10 · Integration 4/5
→ **79**
