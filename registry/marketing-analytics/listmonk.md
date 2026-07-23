---
name: listmonk
category: marketing-analytics
subcategory: email-newsletter
status: approved-with-restrictions
type: tool
canonical_repo: https://github.com/knadh/listmonk
website: https://listmonk.app
pinned_version: v6.2.0 (2026-06-26)
license: AGPL-3.0
score: 79
confidence: medium
tested: false
last_verified: 2026-07-23
---

# listmonk — self-hosted newsletter and mailing-list manager

## What it does
Single-binary Go application (Postgres-backed) for newsletters, mailing
lists, campaign analytics, and transactional templates; brings email-list
ownership in-house at SMTP cost instead of per-subscriber SaaS pricing.

## When to use
- Founder newsletters/product announcements once a list outgrows free SaaS
  tiers; full data ownership of subscriber lists

## When not to use / restrictions
- **You still need an SMTP/sending provider** (SES, Postmark, …) — inbox
  deliverability is the provider's reputation plus your domain setup (SPF/
  DKIM/DMARC); listmonk does not solve deliverability `[I]`
- AGPL-3.0: network copyleft on modified deployments
- Marketing-automation journeys/drip sequencing are limited vs commercial
  suites `[R]`

## Evidence
- License AGPL-3.0 `[V]` — repository (2026-07-23)
- Latest v6.2.0, 2026-06-26; sustained releases (41+) `[V]`
- Maintainer concentration: authored and led by Kailash Nadh (knadh);
  high single-maintainer concentration `[C]` — bus-factor risk; author also
  maintains it in production at scale at Zerodha `[C]` — public statements

## Validation results
- Not execution-tested this pass (Postgres + SMTP required; Phase 2).

## Security findings
- Subscriber PII lives in your Postgres — backup + access control are your
  compliance surface `[I]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- AGPL-3.0: commercial and SaaS use permitted; source obligations on
  modified network use. Subscriber-data protection law (GDPR/CAN-SPAM)
  applies to your usage regardless of tool license.

## Installation
Single binary or `listmonk/listmonk:v6.2.0` Docker + Postgres.

## Agent integration
Full REST API (campaigns, lists, templates); agent-drafted campaigns must
be human-approved before send — email mistakes are irreversible.

## Required human review
Every outbound campaign; SPF/DKIM/DMARC setup; consent/opt-in compliance.

## Score notes
Functional 16/20 · Security 14/20 · Maintenance 12/15 (bus factor) ·
Docs 8/10 · License 7/10 · Reproducibility 8/10 · Provenance 6/10 ·
Integration 5/5 → **79** (test coverage of repo not assessed — `[U]`)
