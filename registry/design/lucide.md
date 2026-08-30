---
name: Lucide
category: design
subcategory: interface-iconography
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/lucide-icons/lucide
website: https://lucide.dev
pinned_version: 1.37.0 (published 2026-08-29)
license: ISC AND MIT
score: 84
confidence: medium
tested: false
last_verified: 2026-08-30
---

# Lucide — consistent open interface icons

## What it does
Provides a large, consistent SVG interface-icon family and official packages
for major web and native frameworks `[V]`.

## When to use
- For coherent interface actions, navigation, status, and object metaphors
- Where tree-shakable framework components or static SVGs are useful
- Under a product-specific sizing, stroke, labeling, and fallback policy

## When not to use
- For a company's logo, wordmark, app icon, trademark, or social-brand icon;
  the project intentionally excludes brand logos `[V]`
- As the only cue for unfamiliar, destructive, legal, health, or financial
  actions
- To mix arbitrary icons from several families without visual review

## Evidence
- Official repository and documentation reviewed `[V]`
- Release 1.37.0 published 2026-08-29 with downloadable icon/font assets `[V]`
- Repository license is ISC; listed Feather-derived icons retain MIT notices
  in the license file `[V]`

## Validation results
Source, release metadata, and licensing inspected. Framework packages were
not execution-tested in this pass.

## Security findings
Static SVG/components have a small runtime surface, but applications should
pin packages and avoid injecting untrusted SVG markup or attributes.

## Legal / licensing findings
Preserve ISC and applicable MIT notices when redistribution triggers notice
obligations. The library's exclusion of brand logos avoids granting any
rights in third-party trademarks.

## Installation
Pin the framework package, for example `lucide-react@1.37.0`, after confirming
the selected package's published version and peer dependencies.

## Agent integration
Select by documented semantic meaning, use one family consistently, mark
decorative icons hidden, add accessible names to icon-only controls, and
never substitute a Lucide glyph for a brand mark.

## Required human review
Metaphor clarity, cultural/localization fit, critical-action labeling,
accessibility, and rendered alignment.

## Score notes
Functional 18/20 · Security 17/20 · Maintenance 15/15 · Docs 9/10 ·
License 9/10 · Reproducibility 7/10 · Provenance 6/10 · Integration 3/5
→ **84**.

