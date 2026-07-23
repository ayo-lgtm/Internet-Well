---
name: Penpot
category: design
subcategory: design-tool
status: approved
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/penpot/penpot
website: https://penpot.app
pinned_version: 2.17.0 (2026-07-22)
license: MPL-2.0
score: 80
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Penpot — open-source design and prototyping platform

## What it does
Figma-class UI design/prototyping tool built on open standards (SVG, CSS);
self-hostable or usable via Penpot's hosted service; design-tokens support
and dev handoff.

## When to use
- Product design/mockups without SaaS lock-in; self-hosting keeps design IP
  on infrastructure you control

## When not to use
- Heavy dependence on Figma-ecosystem plugins/community files
- Solo founders who only need quick wireframes may prefer paper/Excalidraw
  (Phase 3 candidate) — Penpot is a full server deployment when self-hosted

## Evidence
- License MPL-2.0 `[V]` — repository (2026-07-23)
- Latest 2.17.0, 2026-07-22; 84 releases, active `[V]` — repo page
- Corporate maintainer: Kaleidos (the company behind Taiga) `[C]`
- 57k stars — context only `[V]`

## Validation results
- Not execution-tested this pass (multi-service server deployment; Phase 2
  docker-compose test). Official versioned compose files documented `[V]`.

## Security findings
- Self-hosted instance = your patching responsibility; hosted service =
  your designs on their infrastructure (review their DPA) `[I]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- MPL-2.0: commercial use, SaaS, redistribution permitted; file-level
  copyleft on modified Penpot files.

## Installation
Official docker-compose (pin image tags to 2.17.0).

## Agent integration
Exports SVG/CSS and has a plugin API `[M]`; agent-driven design-token
extraction is plausible but unvalidated here.

## Required human review
Hosting choice (data location), backup strategy for design files.

## Score notes
Functional 17/20 · Security 14/20 · Maintenance 14/15 · Docs 8/10 ·
License 10/10 · Reproducibility 7/10 · Provenance 7/10 · Integration 3/5
→ **80**
