---
name: Metabase (Open Source edition)
category: finance
subcategory: business-intelligence
status: approved-with-restrictions
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/metabase/metabase
website: https://www.metabase.com
pinned_version: v0.63.1 OSS (release "63.1", 2026-07-21)
license: AGPL-3.0 (OSS edition); commercial editions under Metabase Commercial License in same repo
score: 80
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Metabase — self-hosted BI dashboards and SQL exploration

## What it does
Point-and-click + SQL business intelligence over your own databases:
dashboards for revenue, activation, retention, and operational metrics
without exporting data to a SaaS. The practical "operational controls"
layer for a founder's Postgres.

## When to use
- Founder metrics dashboards (MRR, signups, churn, support load) straight
  from your production replica/warehouse
- Weekly-review numbers a founder and an agent can both query

## When not to use / restrictions
- **Open-core in one repo**: OSS edition is AGPL-3.0; enterprise
  code lives in the same repository under the Metabase Commercial
  License, and a separate LICENSE-EMBEDDING governs embedding `[V]` —
  repo licensing statements. Build/deploy the OSS edition
  (`metabase/metabase` OSS jar/image) and audit before embedding
  dashboards in your product — embedded analytics is exactly where
  their commercial boundary sits.
- AGPL network copyleft on modifications you serve to users.
- Query your replica, not your primary (BI queries can be heavy) `[I]`

## Evidence
- Licensing structure `[V]` — repository states AGPL OSS + MCL
  commercial editions + embedding license file (2026-07-23)
- Latest release 63.1, 2026-07-21; 43,500+ commits, very active `[V]`
- Corporate maintainer: Metabase Inc. `[C]`; wide self-hosted adoption
  `[C]` — context

## Validation results
- Not execution-tested (JVM server app; Docker unavailable in sandbox).
  Versioned OSS images documented `[V]`. RECHECK item.

## Security findings
- Holds read credentials to your databases — scope a read-only DB user,
  never admin credentials `[I]`; keep it off the public internet or
  behind SSO `[I]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- AGPL-3.0 OSS edition: commercial/SaaS use permitted; network copyleft
  on modifications; embedding in your product intersects both AGPL and
  their embedding terms — counsel review before customer-facing use.

## Installation
OSS Docker image pinned to the release (`metabase/metabase:v0.63.1`)
with Postgres app-db; or the OSS jar.

## Agent integration
API for cards/dashboards; an agent can draft SQL questions for human
review. Give agents the same read-only DB principle.

## Required human review
Embedding/licensing boundary (counsel); DB credential scoping; any
externally shared dashboard.

## Score notes
Functional 18/20 · Security 14/20 · Maintenance 14/15 · Docs 9/10 ·
License 6/10 (open-core in-repo + embedding terms) · Reproducibility
7/10 · Provenance 7/10 · Integration 5/5 → **80**
