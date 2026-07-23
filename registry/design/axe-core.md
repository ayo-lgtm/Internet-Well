---
name: axe-core
category: design
subcategory: accessibility-testing
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/dequelabs/axe-core
website: https://www.deque.com/axe/
pinned_version: 4.12.1 (npm, published 2026-06-10)
license: MPL-2.0
score: 88
confidence: high
tested: true
last_verified: 2026-07-23
---

# axe-core — automated accessibility (WCAG) testing engine

## What it does
JavaScript engine that audits rendered pages against WCAG success criteria
(missing alt text, contrast, ARIA misuse, form labels). Embeddable in
Playwright/Cypress/Jest and browser devtools.

## When to use
- Automated accessibility gate in CI for every founder-built web UI
  (pair with Playwright via `@axe-core/playwright`)

## When not to use
- As proof of accessibility compliance: automated checks catch roughly
  30–50% of WCAG issues by independent estimates `[C]`; manual testing
  (keyboard, screen reader) remains required. Never claim "WCAG compliant"
  from a clean axe run.

## Evidence
- License MPL-2.0 `[V]` — npm metadata 4.12.1 (2026-07-23)
- Published 2026-06-10; steady release cadence `[V]` — npm history
- Professional provenance: Deque Systems, an accessibility consultancy;
  engine also powers Lighthouse's accessibility audit `[C]`

## Validation results (sandboxed test, 2026-07-23)
- Injected axe-core 4.12.1 into a Playwright-rendered page containing an
  `<img>` without alt text: violation `image-alt` correctly reported;
  test passed. Fully offline.

## Security findings
- Runs in-page with no network egress `[V]` — observed

## Legal / licensing findings
- MPL-2.0: commercial use, SaaS, redistribution permitted; file-level
  copyleft on modifications to axe-core files themselves.

## Installation
`npm i -D axe-core@4.12.1` (or `@axe-core/playwright`)

## Agent integration
JSON violation output with rule IDs and DOM selectors — well-suited to
agent fix-loops; agents should link each fix to the WCAG criterion.

## Required human review
Manual accessibility testing; any public conformance claims.

## Score notes
Functional 18/20 · Security 18/20 · Maintenance 14/15 · Docs 9/10 ·
License 10/10 · Reproducibility 10/10 · Provenance 9/10 · Integration 5/5
→ capped **88** (coverage limits inherent to automated a11y testing).
