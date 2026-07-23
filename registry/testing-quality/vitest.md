---
name: Vitest
category: testing-quality
subcategory: unit-testing-javascript
status: approved
type: framework
canonical_repo: https://github.com/vitest-dev/vitest
website: https://vitest.dev
pinned_version: 4.1.10 (npm, published 2026-07-06)
license: MIT
score: 87
confidence: high
tested: true
last_verified: 2026-07-23
---

# Vitest — Vite-native JavaScript/TypeScript unit testing

## What it does
Fast unit/component test runner with Jest-compatible APIs, first-class
TypeScript/ESM support, watch mode, coverage, and browser mode.

## When to use
- Unit and component tests for JS/TS products, especially Vite-based
  frontends; sensible default for new TS projects

## When not to use
- Full browser E2E (Playwright); legacy Jest projects with heavy
  Jest-plugin coupling may not repay migration effort

## Evidence
- License MIT `[V]` — npm registry metadata for vitest 4.1.10 (2026-07-23)
- Published 2026-07-06; frequent patch cadence `[V]` — npm history
- Maintained by the Vitest team within the Vite/VoidZero ecosystem, multiple
  active maintainers `[C]` — repo org
- Wide adoption in modern JS tooling `[C]` — context

## Validation results (sandboxed test, 2026-07-23)
- `npm i -D vitest@4.1.10`; ran a sample test: **1 passed**, exit 0
- Note: an initial failure was researcher error (`--reporter=basic` was
  removed in Vitest 4); recorded for honesty — default reporter works

## Security findings
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- MIT — commercial use, SaaS, redistribution permitted.

## Installation
`npm i -D vitest@4.1.10`

## Agent integration
JSON reporter and programmatic API; good fit for agent test-fix loops.

## Required human review
Same as pytest: agent changes that weaken assertions need human eyes.

## Score notes
Functional 19/20 · Security 16/20 (large transitive dep tree — standard JS
risk) · Maintenance 14/15 · Docs 9/10 · License 10/10 · Reproducibility
9/10 · Provenance 6/10 · Integration 4/5 → **87**
