---
name: Uptime Kuma
category: devops-infrastructure
subcategory: uptime-monitoring
status: approved
type: tool
canonical_repo: https://github.com/louislam/uptime-kuma
website: https://uptime.kuma.pet
pinned_version: 2.4.0 (2026-05-31)
license: MIT
score: 78
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Uptime Kuma — self-hosted uptime monitoring and status pages

## What it does
Monitors HTTP(S)/TCP/DNS/Docker targets, alerts through 90+ notification
providers, and serves public status pages — a self-hosted UptimeRobot
replacement.

## When to use
- External uptime checks + a public status page for a founder's product at
  zero SaaS cost (run it on a separate cheap VPS from production)

## When not to use
- As your only monitoring (it is black-box up/down checking; pair with
  Prometheus for internals)
- Multi-region synthetic monitoring guarantees (single-instance vantage)

## Evidence
- License MIT `[V]` — repository license indicator (2026-07-23)
- Latest release 2.4.0, 2026-05-31; 7,100+ commits, active `[V]` — repo page
- Maintainer concentration: project founded and led by Louis Lam;
  historically high single-maintainer concentration `[C]` — contributor
  records; moderate bus-factor risk
- Large user base (89k stars — context only) `[V]`

## Validation results
- Not execution-tested this pass (server app; Phase 2 docker test).
  Versioned image `louislam/uptime-kuma:2.4.0` documented `[V]`.

## Security findings
- Status pages are public by design — review what monitor names/URLs reveal
  about your infrastructure `[I]`
- Keep the admin UI off the public internet or behind auth proxy `[I]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- MIT — commercial use, SaaS, redistribution permitted.

## Installation
Docker: `louislam/uptime-kuma:2.4.0` with a persistent volume.

## Agent integration
Has an API and a Terraform provider maintained by the community `[R]`;
treat monitor config as code where possible.

## Required human review
Notification-channel credentials; what the public status page exposes.

## Score notes
Functional 16/20 · Security 14/20 · Maintenance 12/15 (bus factor) ·
Docs 8/10 · License 10/10 · Reproducibility 8/10 · Provenance 5/10
(individual-led) · Integration 5/5 → **78**
