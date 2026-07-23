---
name: promptfoo
category: engineering
subcategory: llm-testing-redteaming
status: experimental
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/promptfoo/promptfoo
website: https://promptfoo.dev
pinned_version: 0.121.19 (npm, published 2026-07-14)
license: MIT
score: null
confidence: low
tested: false
last_verified: 2026-07-23
---

# promptfoo — declarative prompt testing and LLM red-teaming

## What it does
YAML-declared test cases for prompts/models (assertions on outputs,
side-by-side comparisons) plus automated red-team probes for LLM apps.

## Status: experimental — why not yet approved

Validated only at metadata level this pass:

- License MIT `[V]` — npm metadata 0.121.19 (2026-07-23)
- Very active releases `[V]` — npm history
- Corporate maintainer (Promptfoo, Inc., VC-funded) with a commercial
  cloud offering `[C]`

Open items blocking approval (tracked in RECHECK):
1. Execution test (assertion run with a mock/echo provider, offline)
2. **Telemetry audit** — the CLI has usage telemetry; verify current
   default state and opt-out env var against the shipped version `[R]`
3. Open-core boundary audit (cloud/enterprise feature coupling in the
   CLI)

## When to use (once approved)
- Lightweight CI assertions on prompt outputs; pre-release red-team
  sweeps of chat endpoints

## When not to use
- Structured research-grade evals (Inspect AI —
  `registry/engineering/inspect-ai.md` — is the approved entry)

## Required human review
Red-team runs against anything but your own endpoints; telemetry posture.
