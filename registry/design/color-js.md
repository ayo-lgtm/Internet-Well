---
name: Color.js
category: design
subcategory: color-science
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/color-js/color.js
website: https://colorjs.io
pinned_version: v0.7.1 (published 2026-07-24)
license: MIT
score: 83
confidence: medium
tested: false
last_verified: 2026-08-30
---

# Color.js — standards-oriented color conversion and calculation

## What it does
Provides color parsing, conversion, manipulation, interpolation, gamut
mapping, and contrast/difference methods across modern color spaces `[M]`.
The project is maintained by editors of CSS Color specifications `[V]`.

## When to use
- For deterministic color-space conversion and palette calculations
- To evaluate candidate token values and generate documented transformations
- With WCAG checks, forced-colors testing, and human visual review

## When not to use
- As a guarantee that a palette is accessible, perceptually uniform in every
  context, brand-distinctive, or suitable for all vision conditions
- To ship wide-gamut colors without tested fallbacks
- To use color as the only carrier of meaning

## Evidence
- Official repository is MIT licensed, active, and identifies its maintainers'
  CSS Color standards role `[V]`
- Stable release v0.7.1 published 2026-07-24 `[V]`
- Official documentation describes supported color operations `[M]`

## Validation results
Release, license, and documentation inspected. Package execution and numeric
fixtures were not run in this pass.

## Security findings
Treat untrusted color strings and plugin/config input as data to validate.
Pin the dependency and avoid evaluating generated code.

## Legal / licensing findings
MIT permits commercial use, modification, and redistribution subject to
notice conditions. Calculated colors do not establish rights in a copied
brand palette or trade dress.

## Installation
`npm i colorjs.io@0.7.1`

## Agent integration
Agents may calculate candidates and record color space, algorithm, inputs,
and outputs. They must retain semantic intent and require rendered contrast,
state, and forced-colors verification.

## Required human review
Brand fit, contrast and non-color cues, wide-gamut fallback, dark mode,
critical status colors, and final display testing.

## Score notes
Functional 18/20 · Security 16/20 · Maintenance 14/15 · Docs 9/10 ·
License 10/10 · Reproducibility 7/10 · Provenance 6/10 · Integration 3/5
→ **83**.

