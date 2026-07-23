---
name: ZAP (Zed Attack Proxy)
category: security-engineering
subcategory: dast
status: approved
type: tool
canonical_repo: https://github.com/zaproxy/zaproxy
website: https://www.zaproxy.org
pinned_version: v2.17.0 (2025-12-15)
license: Apache-2.0
score: 85
confidence: medium
tested: false
last_verified: 2026-07-23
---

# ZAP — dynamic application security testing (DAST) proxy and scanner

## What it does
Intercepting proxy and active/passive web-app vulnerability scanner.
Automated baseline scans for CI plus a full manual pen-testing toolkit.
Long-running former OWASP flagship project, now stewarded under Checkmarx
("ZAP by Checkmarx") while remaining Apache-2.0.

## When to use
- Pre-launch and recurring DAST baseline scans of your own web app/staging
  environment (docker `zap-baseline.py` in CI)
- Manual security exploration of your own application

## When not to use
- **Never against systems you do not own or lack written authorization to
  test** — active scanning is intrusive
- As a SAST substitute (pair with Semgrep/CodeQL-class tools)
- Headless API-only microservices with no web surface may get more value
  from schema-based API scanning configs (ZAP supports OpenAPI import, but
  configuration effort is higher)

## Evidence
- License Apache-2.0 `[V]` — repository license indicator (2026-07-23)
- Latest release v2.17.0, 2025-12-15 `[V]` — repository releases page;
  release cadence is roughly 1–2 core releases/year with weekly add-on
  updates `[C]`
- Stewardship moved from OWASP to Checkmarx in 2024; project states it
  remains free and open source `[C]` — zaproxy.org and independent coverage
- Active: 10,300+ commits, CI + CodeQL + SonarCloud quality gates visible
  on the repository `[V]`

## Validation results
- Not execution-tested this pass (Java desktop/daemon app; containerized
  test deferred to Phase 2). Installation methods documented and versioned
  (Docker `ghcr.io/zaproxy/zaproxy:stable`, installers, cross-platform
  bundles) `[V]`

## Security findings
- Calls home by default for news/add-on update checks; disable via
  `-config` options for hermetic CI `[R]` — verify against current docs
- Mature security-tool pedigree; no unresolved material advisories located
  this pass; Scorecard unretrievable `[U]`

## Legal / licensing findings
- Apache-2.0: commercial use, modification, redistribution, SaaS permitted.
- "ZAP" branding/trademark now associated with Checkmarx stewardship; don't
  imply endorsement when marketing services built on it `[I]`.

## Installation
Docker: `ghcr.io/zaproxy/zaproxy:stable` (pin digest for reproducibility);
platform installers from zaproxy.org. Requires Java 17+ for non-Docker use.

## Agent integration
Use the automation framework / baseline scan with JSON report output.
An agent must be constrained to targets on an allowlist the human owns;
active-scan invocation should require explicit human approval each run.

## Required human review
Authorization for every target; triage of alerts (baseline passive alerts
have meaningful false-positive rates).

## Score notes
Functional 18/20 · Security 16/20 · Maintenance 13/15 (core releases
infrequent but add-ons continuous) · Docs 9/10 · License 10/10 ·
Reproducibility 7/10 (untested this pass) · Provenance 9/10 (OWASP heritage,
corporate steward) · Integration 3/5 (heavier setup) → **85**
