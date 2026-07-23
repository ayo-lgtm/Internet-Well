---
name: NIST AI Risk Management Framework (AI RMF 1.0)
category: compliance
subcategory: ai-governance
status: approved
type: standard
canonical_repo: none (NIST publication; companion playbook at airc.nist.gov)
website: https://www.nist.gov/itl/ai-risk-management-framework
pinned_version: AI RMF 1.0 (NIST AI 100-1, 2023-01-26); Generative AI Profile (NIST AI 600-1, 2024-07)
license: Public domain (US federal government work, 17 U.S.C. §105)
score: null
confidence: medium
tested: not-applicable
last_verified: 2026-07-23
---

# NIST AI RMF — the reference framework for AI risk governance

## What it does
Voluntary framework for managing AI risks across four functions (Govern,
Map, Measure, Manage), with a companion Playbook and a Generative AI
Profile (AI 600-1) listing GenAI-specific risks and suggested actions.

## When to use
- A founder shipping AI features who needs a defensible, recognized
  structure for "what could go wrong and what do we do about it" —
  especially when enterprise customers ask about AI governance
- Pair with OWASP LLM Top 10 (security-specific) — RMF covers the wider
  risk surface (validity, bias, privacy, transparency)

## When not to use
- As a compliance certification (it is voluntary; no conformance scheme)
- As a substitute for jurisdictional obligations (EU AI Act etc. are law,
  not frameworks — counsel required)

## Evidence
- AI RMF 1.0 released 2023-01-26 `[C]` — NIST announcements + multiple
  independent sources; Generative AI Profile (AI 600-1) July 2024 `[C]`
- Publication identifiers NIST AI 100-1 / AI 600-1 `[C]` — corroborated
  by independent implementation guides; **direct verification against
  nist.gov was blocked by this environment's network policy** — flagged
  in RECHECK for primary confirmation
- License: US government works are not subject to domestic copyright
  (17 U.S.C. §105) `[V]` — statutory basis
- Provenance: NIST — highest institutional tier `[V]`

## Validation results
- Standards document; not executable.

## Legal / licensing findings
- Public domain in the US; NIST name/logo may not be used to imply
  endorsement.

## Installation
Download the PDF artifacts; vendor the GenAI Profile action list into your
risk register.

## Agent integration
Use the Map/Measure/Manage action tables as grounding for an agent
drafting your AI risk register — human owns the risk acceptance.

## Required human review
All risk-acceptance decisions; legal obligations mapping (counsel).

## Score notes
Not scored (standard). Confidence capped at medium until primary-source
verification (nist.gov) is completed — see RECHECK.
