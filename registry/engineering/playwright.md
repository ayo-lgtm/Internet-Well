---
name: Playwright
category: engineering
subcategory: e2e-testing
status: approved
tier: B
human_reviewed: false
type: framework
canonical_repo: https://github.com/microsoft/playwright
website: https://playwright.dev
pinned_version: "@playwright/test 1.61.1 (npm, published 2026-06-23)"
license: Apache-2.0
score: 90
confidence: high
tested: true
last_verified: 2026-07-23
---

# Playwright — cross-browser end-to-end testing

## What it does
Automates Chromium, Firefox, and WebKit for end-to-end tests with
auto-waiting, tracing, parallelism, and CI-friendly reporters. Also widely
used as a general browser-automation library for agents.

## When to use
- E2E coverage of the founder's critical user journeys (signup, checkout,
  auth) in CI before every deploy
- Cross-browser regression checks before launch

## When not to use
- Unit/component logic (use Vitest/pytest — E2E is slow and flaky-prone)
- Load testing (different tool class)

## Evidence
- License Apache-2.0 `[V]` — npm registry metadata for @playwright/test
  1.61.1 (2026-07-23); repository microsoft/playwright `[V]`
- Published 2026-06-23; monthly release cadence `[V]` — npm publish history
- Corporate maintainer: Microsoft `[V]` — npm/repo org
- Broad industry adoption `[C]` — ecosystem integrations; context only

## Validation results (sandboxed test, 2026-07-23)
- `npm i -D @playwright/test@1.61.1` — reproducible
- Ran a real browser test (launch Chromium, set DOM content, locator
  assertion): **1 passed**
- Environment note: the sandbox's preinstalled Chromium revision differed
  from the version 1.61.1 expects, requiring an explicit
  `launchOptions.executablePath`; on a normal host `npx playwright install`
  removes this friction. Recorded as environment artifact, not a defect.

## Security findings
- Downloads browser binaries from Microsoft/Playwright CDN on install
  (pinned per release) `[V]` — documented, observed
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- Apache-2.0 — commercial use, SaaS, redistribution permitted. Bundled
  browsers carry their own licenses (Chromium BSD-style, WebKit LGPL/BSD)
  — relevant only if you redistribute browser builds.

## Installation
`npm i -D @playwright/test@1.61.1 && npx playwright install --with-deps`

## Agent integration
First-class: deterministic selectors, JSON reporters, trace files an agent
can read. Keep agent-driven browsing pointed only at environments you own.

## Required human review
Flaky-test quarantine decisions; any test that touches production systems.

## Score notes
Functional 20/20 · Security 17/20 · Maintenance 15/15 · Docs 10/10 ·
License 10/10 · Reproducibility 9/10 · Provenance 9/10 (single corporate
sponsor — concentration) · Integration 5/5 → capped at **90** for browser-
download runtime dependency.
