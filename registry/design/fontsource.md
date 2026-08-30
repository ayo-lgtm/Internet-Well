---
name: Fontsource
category: design
subcategory: typography-delivery
status: approved-with-restrictions
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/fontsource/fontsource
website: https://fontsource.org
pinned_version: core-v0.3.0 (commit 83e7147eefa88fa7de66336b81c96650fe62de6c)
license: MIT (tooling; font licenses vary by package)
score: 82
confidence: medium
tested: false
last_verified: 2026-08-30
---

# Fontsource — packaged self-hosted open fonts

## What it does
Packages open fonts for self-hosting through npm, with CSS, subsets, weights,
styles, and variable-font options depending on the family `[M]`.

## When to use
- To avoid a runtime font-CDN request and control webfont delivery
- To pin only the families, subsets, and weights a product actually uses
- With glyph-coverage, performance, fallback, and license tests

## When not to use
- To assume every font is MIT licensed because the Fontsource tooling is MIT
- To select brand typography solely by package availability
- To omit local fallbacks, supported-script checks, or loading measurements

## Evidence
- Official repository is active and MIT licensed for its software `[V]`
- Latest repository release observed was core-v0.3.0, published 2026-07-26
  at commit `83e7147eefa88fa7de66336b81c96650fe62de6c` `[V]`
- Official site identifies the service as self-hosted open-source font
  packages `[M]`

## Validation results
Repository metadata and license inspected. No font family was chosen or
installed because licensing and glyph requirements are product-specific.

## Security findings
Self-hosting reduces a runtime third-party request, but package acquisition
remains a supply-chain event. Pin exact versions, verify integrity, and do not
load font URLs supplied by untrusted brand files.

## Legal / licensing findings
The repository tooling is MIT. Each bundled font has its own license (often
OFL-1.1 or Apache-2.0), copyright, reserved font names, modification rules,
and possible attribution requirements. Review the selected family package.

## Installation
After approving a family and its license, install its exact package/version,
for example `npm i @fontsource/<family>@<pin>`.

## Agent integration
Agents may shortlist fonts by product needs and script coverage, but must
surface each license, weight/subset cost, fallback stack, and loading plan
before changing a product.

## Required human review
Typography direction, glyph/language coverage, font license and trademark
terms, performance, legibility, and final rendering.

## Score notes
Functional 18/20 · Security 16/20 · Maintenance 14/15 · Docs 9/10 ·
License 7/10 · Reproducibility 7/10 · Provenance 7/10 · Integration 4/5
→ **82**.

