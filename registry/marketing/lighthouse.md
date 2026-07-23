---
name: Lighthouse
category: marketing
subcategory: seo-performance-audit
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/GoogleChrome/lighthouse
website: https://developer.chrome.com/docs/lighthouse
pinned_version: 13.4.1 (npm, published 2026-07-20)
license: Apache-2.0
score: 88
confidence: high
tested: true
last_verified: 2026-07-23
---

# Lighthouse — automated performance, SEO, and accessibility audits

## What it does
Audits any URL in headless Chrome and scores performance (Core Web
Vitals lab data), SEO fundamentals, accessibility (axe-powered), and
best practices, with concrete fix recommendations. Runs as CLI, CI
action, or in Chrome DevTools.

## When to use
- Pre-launch and every-release audit of your marketing site and app
  (`lighthouse-ci` budgets in CI catch regressions)
- SEO technical hygiene: the SEO category covers crawlability/meta
  fundamentals that actually matter before content strategy does

## When not to use
- Rank tracking/keyword research (different tool class; no OSS standout
  validated yet)
- Lab metrics ≠ field data: pair with real-user Core Web Vitals from
  Search Console/CrUX for launch decisions `[C]`

## Evidence
- License Apache-2.0 `[V]` — npm metadata 13.4.1 (2026-07-23)
- Published 2026-07-20; steady cadence `[V]` — npm history
- Corporate maintainer: Google Chrome team `[V]` — repo org
- Powers PageSpeed Insights; industry-standard audit `[C]`

## Validation results (sandboxed test, 2026-07-23)
- `npm i lighthouse@13.4.1` — reproducible
- Audited a locally served semantic HTML page in headless Chromium:
  exit 0, JSON report with category scores (performance 1.0,
  accessibility 1.0, best-practices 0.96, SEO 1.0). Fully offline
  (local server; no external calls needed for the audit itself).

## Security findings
- Audits run in a local browser; the audited URL's content executes in
  that browser — audit only pages you trust or sandbox appropriately `[I]`

## Legal / licensing findings
- Apache-2.0 — commercial use permitted.

## Installation
`npm i -D lighthouse@13.4.1` (requires Chrome/Chromium; set CHROME_PATH
if non-standard).

## Agent integration
JSON output with per-audit details is ideal for agent fix-loops
(minify, alt text, meta descriptions). Score-chasing beyond ~90s has
diminishing returns — agents should fix cited audits, not optimize the
number.

## Required human review
Performance-budget thresholds; any SEO structural changes.

## Score notes
Functional 19/20 · Security 17/20 · Maintenance 14/15 · Docs 9/10 ·
License 10/10 · Reproducibility 9/10 · Provenance 8/10 (single corporate
sponsor) · Integration 5/5 → capped **88** (lab-data limits).
