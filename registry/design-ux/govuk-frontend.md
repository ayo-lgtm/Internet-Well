---
name: GOV.UK Frontend (GOV.UK Design System)
category: design-ux
subcategory: design-system
status: approved
type: framework
canonical_repo: https://github.com/alphagov/govuk-frontend
website: https://design-system.service.gov.uk
pinned_version: 6.4.0 (npm, published 2026-07-16)
license: MIT
score: 85
confidence: high
tested: true
last_verified: 2026-07-23
---

# GOV.UK Frontend — institutionally maintained accessible design system

## What it does
The UK Government Digital Service's production design system: HTML/CSS/JS
components (forms, tables, navigation, error patterns) with documented,
user-researched accessibility behavior; a reference implementation of
accessible-by-default UI patterns.

## When to use
- Form-heavy, content-heavy products where accessibility and clarity beat
  visual branding (admin panels, onboarding flows)
- As a **reference implementation** for how components should behave
  (focus management, error summaries) even when using another UI kit

## When not to use
- Consumer products needing distinctive branding (it looks like GOV.UK;
  Crown-branding assets are excluded from the MIT grant)

## Evidence
- License MIT `[V]` — npm metadata 6.4.0 (2026-07-23)
- Published 2026-07-16; steady cadence `[V]` — npm history
- Institutional provenance: maintained by the UK Government Digital
  Service (alphagov org); in production across gov.uk services used by
  millions `[C]` — public service records; strongest provenance of any
  design system evaluated this phase
- Components documented with user-research rationale `[M]` — design-system
  site

## Validation results (sandboxed test, 2026-07-23, Phase 2)
- `npm i govuk-frontend@6.4.0` — reproducible; dist bundle present
- Rendered a form group (label+input) and button with the package's
  compiled CSS in headless Chromium: components styled correctly
  (computed styles applied), and an axe-core 4.12.1 scan of the rendered
  page reported **zero violations**

## Security findings
- Static assets; no network egress `[I]`

## Legal / licensing findings
- MIT for the code; **Crown copyright applies to GOV.UK branding/crests** —
  do not reuse UK government identity assets `[C]` — repo docs.

## Installation
`npm i govuk-frontend@6.4.0`

## Agent integration
Well-structured Nunjucks/HTML examples an agent can pattern-match when
generating accessible markup.

## Required human review
Brand differentiation decisions; accessibility still needs manual testing.

## Score notes
Functional 16/20 · Security 17/20 · Maintenance 14/15 · Docs 10/10 ·
License 9/10 (branding carve-out) · Reproducibility 8/10 · Provenance
10/10 · Integration 3/5 → **85**
