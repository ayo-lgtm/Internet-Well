---
name: MADR (Markdown Architectural Decision Records)
category: product
subcategory: decision-records
status: approved
tier: B
human_reviewed: false
type: template
canonical_repo: https://github.com/adr/madr
website: https://adr.github.io/madr/
pinned_version: 4.0.0 (2024-09-17)
license: MIT OR CC0-1.0 (user's choice)
score: null
confidence: high
tested: not-applicable
last_verified: 2026-07-23
---

# MADR — lightweight decision-record template

## What it does
A standardized Markdown template for recording significant decisions
(architecture, vendor choices, strategy calls): context, options
considered, decision, consequences. Variants from bare to full.

## When to use
- Every consequential solo-founder decision — the record is what lets a
  future you (or an AI agent) understand *why* the system is the way it is
- Grounding agents: ADRs in-repo give agents citable context that prevents
  re-litigating settled decisions

## When not to use
- Trivial decisions (template fatigue kills the habit — record only
  decisions that are expensive to reverse or explain)

## Evidence
- License MIT OR CC0-1.0 dual, user's choice `[V]` — repository
  (2026-07-23)
- Latest 4.0.0, 2024-09-17; 19 releases, semantic-versioned with changelog
  `[V]` — a *template* that is itself release-managed
- Slow cadence is appropriate for a stable template; not abandonment `[I]`
- Provenance: maintained within the adr.github.io community (originating
  from academic + practitioner work on architecture decision records) `[C]`

## Validation results
- Template, not executable. Structure verified against the repository.

## Legal / licensing findings
- CC0 option means zero obligations — your ADRs are unencumbered.

## Installation
Copy `template/` into `docs/decisions/` in your repo.

## Agent integration
Instruct agents to (a) read `docs/decisions/` before proposing
architectural changes and (b) draft a new MADR for any significant change,
for human approval.

## Required human review
The decisions themselves — the template only structures them.

## Score notes
Not scored (template; execution dimensions inapplicable).
