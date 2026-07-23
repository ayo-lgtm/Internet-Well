---
name: Umami
category: marketing
subcategory: web-analytics
status: approved
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/umami-software/umami
website: https://umami.is
pinned_version: v3.2.0 (2026-06-24)
license: MIT
score: 79
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Umami — MIT-licensed privacy-focused web analytics

## What it does
Self-hosted web analytics with pageviews, events, and simple funnels;
positions itself as an open alternative to GA/Mixpanel/Amplitude.

## When to use
- Founders who want permissive-license analytics (no AGPL considerations at
  all) on a simple Postgres/MySQL stack — operationally lighter than
  Plausible CE (no ClickHouse)

## When not to use
- Deep product analytics (cohorts, session replay — different tool class)
- High-traffic sites where ClickHouse-backed options scale better `[I]`

## Evidence
- License MIT `[V]` — repository (2026-07-23)
- Latest v3.2.0, 2026-06-24; active `[V]` — repo page
- Maintainer: umami-software organization with an associated cloud company
  (open-core dynamics milder than most: self-hosted feature set is the
  product) `[C]`

## Validation results
- Not execution-tested this pass (Node+Postgres deployment; Phase 2).

## Security findings
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- MIT — commercial use, SaaS, redistribution permitted; simplest legal
  posture of the analytics candidates.

## Installation
Docker `ghcr.io/umami-software/umami:postgresql-v3.2.0` + Postgres.

## Agent integration
REST API with website/event stats; API-key handling is human.

## Required human review
Same privacy-policy diligence as any analytics: disclose collection in
your privacy policy even without cookies.

## Score notes
Functional 15/20 · Security 15/20 · Maintenance 13/15 · Docs 8/10 ·
License 10/10 · Reproducibility 7/10 · Provenance 6/10 · Integration 5/5
→ **79**
