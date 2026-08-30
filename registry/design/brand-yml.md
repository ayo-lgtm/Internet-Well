---
name: brand.yml
category: design
subcategory: brand-system-source
status: approved
tier: C
human_reviewed: false
type: standard
canonical_repo: https://github.com/posit-dev/brand-yml
website: https://posit-dev.github.io/brand-yml/
pinned_version: py/v0.2.0 (commit 6ec390fd4b741b550bd732254c8def90bf50c4a4)
license: MIT
score: 79
confidence: medium
tested: false
last_verified: 2026-08-30
---

# brand.yml — portable brand-guideline source

## What it does
Defines a single `_brand.yml` structure for brand metadata, logo variants,
color palettes and semantic colors, typography, fonts, and tool-specific
defaults `[V]`. Official Python and R readers can validate and consume the
file; Quarto and Shiny are documented consumers `[M]`.

## When to use
- As the human-readable brand source of truth for logos, color, and type
- To keep reports, presentations, documentation, and supported apps aligned
- Alongside DTCG tokens when a product also needs component-level values

## When not to use
- As proof that a proposed logo is distinctive, registrable, or licensed
- As the only token format for a cross-platform component system
- To invent missing brand decisions from an existing product without review

## Evidence
- Official Posit repository and documentation `[V]`
- Release `py/v0.2.0` published 2026-05-21 at commit
  `6ec390fd4b741b550bd732254c8def90bf50c4a4` `[V]`
- Repository remained active through 2026-08-11 `[V]`
- Repository license is MIT `[V]`

## Validation results
Structure and official examples reviewed. Package execution was not performed
in this pass; confidence is therefore capped at medium.

## Security findings
Local YAML can contain remote font and image URLs. Agents must not fetch
untrusted URLs, private intranet paths, or credentials merely because a file
references them. Apply normal YAML parser and supply-chain controls.

## Legal / licensing findings
MIT covers the project code. Referenced logos, images, trademarks, and fonts
retain their own rights and licenses; `_brand.yml` does not grant permission
to use them.

## Installation
Use the schema directly, or pin `brand_yml` for Python / `brand.yml` for R
after reviewing the target release and dependency tree.

## Agent integration
Agents may extract approved brand guidelines into `_brand.yml`, report
unknown fields, and generate adapter plans. They must not silently substitute
fonts, redraw marks, or approve legal clearance.

## Required human review
Brand positioning, logo/mark selection, asset rights, trademark screening,
color and typography approval, and every production asset.

## Score notes
Functional 17/20 · Security 14/20 · Maintenance 13/15 · Docs 9/10 ·
License 10/10 · Reproducibility 6/10 · Provenance 7/10 · Integration 3/5
→ **79**.

