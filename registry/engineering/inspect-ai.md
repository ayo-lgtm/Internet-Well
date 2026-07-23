---
name: Inspect AI
category: engineering
subcategory: llm-evaluation
status: approved
tier: B
human_reviewed: false
type: framework
canonical_repo: https://github.com/UKGovernmentBEIS/inspect_ai
website: https://inspect.aisi.org.uk
pinned_version: 0.3.249 (PyPI, published 2026-07-21)
license: MIT
score: 84
confidence: high
tested: true
last_verified: 2026-07-23
---

# Inspect AI — LLM evaluation framework from the UK AI Security Institute

## What it does
Python framework for building and running LLM evaluations: datasets,
solvers (prompting/agent scaffolds), scorers, an eval-log viewer, and
support for all major model providers. Built and used by the UK government's
AI Security Institute (AISI) for frontier-model evaluations.

## When to use
- Regression-testing the AI features in your product: build an eval set of
  real user scenarios and run it on every prompt/model change
- Comparing model/provider swaps with scored evidence instead of vibes

## When not to use
- Simple string-assertion prompt tests (promptfoo-class tools are lighter;
  see RECHECK — promptfoo not yet fully validated)
- Production runtime guardrails (evals are offline QA, not a firewall)

## Evidence
- License MIT `[V]` — PyPI metadata 0.3.249 (2026-07-23)
- Published 2026-07-21; very frequent releases `[V]` — PyPI history
- Institutional provenance: UK Government BEIS/AISI org repo; documented
  use in AISI's published model evaluations `[C]` — strongest provenance
  in the AI-tooling space
- Provider-agnostic (OpenAI, Anthropic, Google, local models) `[M]` — docs

## Validation results (sandboxed test, 2026-07-23)
- `pip install inspect-ai==0.3.249` in fresh venv — reproducible
- Authored a minimal Task (dataset + generate solver + includes scorer)
  and ran `inspect eval --model mockllm/model` fully offline: exit 0,
  eval-log artifact produced. Full pipeline exercised without any API key.

## Security findings
- Real evals send your prompts/data to the model provider you configure —
  route through the same data-handling review as production traffic `[I]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- MIT — commercial use permitted. Crown-copyright considerations do not
  attach to your usage of the MIT-licensed code `[I]`.

## Installation
`pip install inspect-ai==0.3.249` (Python ≥3.10)

## Agent integration
Evals-as-code in your repo; agents can add eval cases from bug reports for
human review. Use `mockllm` in CI smoke tests to avoid key exposure.

## Required human review
Eval design (what "good" means for your product) and any decision driven
by eval deltas.

## Score notes
Functional 17/20 · Security 16/20 · Maintenance 14/15 · Docs 9/10 ·
License 10/10 · Reproducibility 9/10 · Provenance 9/10 · Integration 4/5
→ capped **84** (fast-moving 0.x API; pin versions).
