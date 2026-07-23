---
name: pytest
category: testing-quality
subcategory: unit-testing-python
status: approved
type: framework
canonical_repo: https://github.com/pytest-dev/pytest
website: https://docs.pytest.org
pinned_version: 9.1.1 (PyPI, published 2026-06-19)
license: MIT
score: 91
confidence: high
tested: true
last_verified: 2026-07-23
---

# pytest — Python testing framework

## What it does
The standard Python test framework: plain-assert tests, fixtures,
parametrization, and a very large plugin ecosystem (coverage, asyncio,
xdist parallelism, hypothesis integration).

## When to use
- All Python unit/integration testing for a founder's backend or tooling

## When not to use
- Non-Python stacks; browser E2E (Playwright)

## Evidence
- License MIT `[V]` — PyPI `license_expression: MIT` (2026-07-23)
- Latest 9.1.1 published 2026-06-19 `[V]` — PyPI JSON API
- Community-governed multi-maintainer org (pytest-dev) with long history
  (since 2004 lineage) `[C]` — repo org and release history
- Enormous production adoption (default test runner of the Python
  ecosystem) `[C]` — context

## Validation results (sandboxed test, 2026-07-23)
- `pip install pytest==9.1.1` in fresh venv; wrote and ran a sample test:
  **1 passed**, exit code 0 — fully offline

## Security findings
- No network activity; test code runs with your privileges (as with any
  test runner, don't run untrusted test suites outside a sandbox) `[I]`

## Legal / licensing findings
- MIT — commercial use, SaaS, redistribution permitted.

## Installation
`pip install pytest==9.1.1`

## Agent integration
Deterministic exit codes and `--junitxml`/`--json-report` (plugin) outputs;
ideal for agent-driven test-fix loops.

## Required human review
None for running; test-deletion or assertion-weakening changes by agents
must be human-reviewed.

## Score notes
Functional 20/20 · Security 18/20 · Maintenance 15/15 · Docs 10/10 ·
License 10/10 · Reproducibility 10/10 · Provenance 8/10 · Integration 5/5
→ capped by rubric weights: **91** (deduction: plugin-ecosystem quality
varies; core only is scored).
