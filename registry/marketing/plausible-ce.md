---
name: Plausible Analytics (Community Edition)
category: marketing
subcategory: web-analytics
status: approved-with-restrictions
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/plausible/analytics
website: https://plausible.io
pinned_version: v3.2.1 (2026-05-15)
license: AGPL-3.0-or-later (JS tracker snippet MIT)
score: 81
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Plausible CE — privacy-first, cookie-free web analytics

## What it does
Lightweight web analytics (pageviews, sources, goals) without cookies or
per-user tracking; a self-hosted Google Analytics alternative designed for
GDPR-friendly operation.

## When to use
- Founder marketing-site and product analytics where privacy posture
  matters and Google Analytics is undesirable
- Cookie-banner-free analytics (verify with your own counsel — vendor
  guidance, not legal advice)

## When not to use / restrictions
- **AGPL-3.0**: modifications to a network-served instance trigger source
  obligations; keep modifications public or run unmodified builds
- Product analytics with per-user funnels/cohorts (use PostHog — Phase 2
  candidate with its own license caveats — or Umami events)
- CE intentionally trails the cloud product in some features; deployment
  requires Postgres + ClickHouse (real operational weight) `[V]` — CE repo

## Evidence
- Core license AGPL-3.0; tracker script MIT `[V]` — repository (2026-07-23)
- Latest v3.2.1, 2026-05-15 `[V]`; CE deploy repo (plausible/community-
  edition) provides versioned compose files, MIT `[V]`
- Corporate maintainer: Plausible Insights OÜ; "CE is funded by our cloud
  subscribers" `[V]` — CE README
- Privacy claims (no cookies, no personal data storage) `[M]` — vendor
  documentation; independent DPA-level verification not performed

## Validation results
- Not execution-tested this pass (Postgres+ClickHouse stack; Phase 2).

## Security findings
- Self-hosting means you hold visitor data — even "privacy-first" data
  needs a retention policy `[I]`

## Legal / licensing findings
- AGPL-3.0-or-later core; MIT tracker embeds cleanly in your site.
  SaaS use permitted; network copyleft on modified server code.

## Installation
plausible/community-edition docker-compose, pinned to v3.2.1.

## Agent integration
Stats API for reads; goals/site config via UI/API — agent read-access is
low-risk.

## Required human review
Privacy/GDPR posture (counsel), data retention settings, any fork changes.

## Score notes
Functional 17/20 · Security 15/20 · Maintenance 13/15 · Docs 9/10 ·
License 7/10 (AGPL manageable; open-core feature gap) · Reproducibility
7/10 · Provenance 8/10 · Integration 5/5 → **81**
