---
name: C4 Model
category: software-architecture
subcategory: architecture-documentation
status: approved
type: standard
canonical_repo: none (c4model.com; related tooling at github.com/structurizr)
website: https://c4model.com
pinned_version: current site (model stable since ~2011; no versioned releases)
license: CC-BY-4.0
score: null
confidence: medium
tested: not-applicable
last_verified: 2026-07-23
---

# C4 Model — hierarchical software architecture diagrams

## What it does
Four zoom levels for describing a system — Context, Containers,
Components, Code — giving a founder (and a CTO-review agent) a shared,
unambiguous vocabulary for architecture diagrams instead of boxes-and-
arrows soup. Mermaid supports C4 diagrams natively, so they live in
your repo as text.

## When to use
- One Context + one Container diagram per product is the minimum viable
  architecture documentation for a solo founder — enough for security
  review (pairs with Threat Dragon data-flow models), onboarding a
  contractor, or grounding an agent's architecture reasoning
- Refresh alongside MADRs when a decision changes the picture

## When not to use
- Don't diagram to Component/Code depth for a small system — the lower
  levels decay fastest and are rarely worth maintaining `[I]` (aligned
  with the model author's own guidance `[C]`)

## Evidence
- License: c4model.com content CC-BY-4.0 `[C]` — corroborated by
  multiple independent sources including the model's Wikipedia entry;
  the site itself was unreachable from this environment (RECHECK for
  primary confirmation)
- Provenance: created by Simon Brown; taught and used industry-wide;
  tooling ecosystem (Structurizr, Mermaid C4, PlantUML/C4) `[C]`

## Legal / licensing findings
- CC-BY-4.0: adaptation with attribution; no ShareAlike.

## Installation
Author diagrams as Mermaid `C4Context`/`C4Container` blocks in your
repo docs.

## Agent integration
Text-based C4 diagrams are ideal agent grounding: agents can check
that new services/dependencies appear in the Container diagram and
propose diagram diffs alongside code changes.

## Required human review
Architectural accuracy; keep diagrams honest or delete them — a wrong
diagram is worse than none.

## Score notes
Not scored (standard/notation). Confidence medium pending
primary-source license confirmation.
