---
name: OWASP Top 10 for LLM Applications / GenAI Security Project
category: ai-engineering
subcategory: ai-security-standard
status: approved
type: standard
canonical_repo: https://github.com/OWASP/www-project-top-10-for-large-language-model-applications
website: https://genai.owasp.org
pinned_version: v2.0 list (2024-11-18 release; project continues under OWASP GenAI Security Project)
license: CC-BY-SA-4.0
score: null
confidence: medium
tested: not-applicable
last_verified: 2026-07-23
---

# OWASP LLM Top 10 — the baseline risk taxonomy for LLM-powered products

## What it does
Names and describes the top security risks specific to LLM applications —
prompt injection, insecure output handling, data poisoning, excessive
agency, system-prompt leakage, and more — with mitigations. Now part of
the broader OWASP GenAI Security Project.

## When to use
- Threat-modeling any AI feature (pair with Threat Dragon: use these as
  your AI-specific threat catalog)
- Security review checklist before shipping agentic capabilities —
  "excessive agency" is the founder-relevant risk when giving agents tools

## When not to use
- As a complete AI-governance program (it's security-scoped; pair with
  NIST AI RMF — `registry/compliance/nist-ai-rmf.md`)

## Evidence
- License CC-BY-SA-4.0 `[V]` — repository (2026-07-23)
- v2.0 list released 2024-11-18; project restructured into OWASP GenAI
  Security Project with ongoing activity (1,100+ commits) `[V]` — repo +
  genai.owasp.org
- OWASP provenance; broad industry citation `[C]`
- Note: project reorganization means the canonical home may continue
  moving — recheck the URL on re-verification `[I]`

## Validation results
- Standard document; version/reorganization status verified.

## Legal / licensing findings
- CC-BY-SA-4.0: attribution + ShareAlike on distributed derivatives.

## Installation
Vendor the current list PDF/Markdown into your security docs.

## Agent integration
Ground AI-security review agents with the risk IDs (LLM01…LLM10) and
require citations per finding.

## Required human review
Mitigation applicability; agent-permission (excessive agency) decisions.

## Score notes
Not scored (standard).
