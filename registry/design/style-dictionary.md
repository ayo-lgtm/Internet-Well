---
name: Style Dictionary
category: design
subcategory: design-token-transformation
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/style-dictionary/style-dictionary
website: https://styledictionary.com
pinned_version: v5.5.2 (published 2026-08-19)
license: Apache-2.0
score: 86
confidence: medium
tested: false
last_verified: 2026-08-30
---

# Style Dictionary — cross-platform token build system

## What it does
Transforms design-token sources into platform outputs such as CSS,
JavaScript, Android, and iOS formats through configuration, transforms, and
formatters `[V]`. Version 5 supports DTCG-shaped input, with documented gaps
for portions of the 2025.10 format `[M]`.

## When to use
- To generate deterministic platform artifacts from reviewed source tokens
- When several products or platforms must share semantic design decisions
- With snapshot/fixture tests and a reviewed custom-transform allowlist

## When not to use
- As the source of brand decisions or component semantics
- To assume complete DTCG 2025.10 compatibility
- To run unreviewed third-party transforms or configuration from user input

## Evidence
- Official repository moved from `amzn` to the Style Dictionary organization
  and remains Apache-2.0 `[V]`
- Stable release v5.5.2 published 2026-08-19 `[V]`
- Official documentation describes DTCG input, formats, transforms, and
  current compatibility limitations `[V]`

## Validation results
Metadata, license, and documentation inspected. The package was not installed
or executed in this pass; target projects must run fixture builds.

## Security findings
Custom parsers, transforms, actions, and formatters are executable code and
inherit build-system privileges. Pin dependencies, review configuration, and
do not process attacker-controlled token projects in a privileged runner.

## Legal / licensing findings
Apache-2.0 permits commercial use, modification, and redistribution subject
to its notice and license conditions. Generated brand assets and fonts retain
their own rights.

## Installation
`npm i -D style-dictionary@5.5.2`

## Agent integration
Agents should plan inputs/outputs, emit a dry-run diff, preserve the reviewed
source file, test aliases and custom transforms, and require approval before
overwriting generated product files.

## Required human review
Token semantics, custom code, compatibility decisions, generated diffs, and
the rendered product.

## Score notes
Functional 19/20 · Security 15/20 · Maintenance 15/15 · Docs 10/10 ·
License 10/10 · Reproducibility 8/10 · Provenance 6/10 · Integration 3/5
→ **86**.

