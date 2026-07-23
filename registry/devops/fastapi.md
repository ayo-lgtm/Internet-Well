---
name: FastAPI
category: engineering
subcategory: backend-api-framework
status: approved
type: framework
canonical_repo: https://github.com/fastapi/fastapi
website: https://fastapi.tiangolo.com
pinned_version: 0.139.2 (PyPI, published 2026-07-16)
license: MIT
score: 87
confidence: high
tested: true
last_verified: 2026-07-23
---

# FastAPI — Python API framework with OpenAPI built in

## What it does
Async Python web framework where type hints produce request validation
(Pydantic) and a live OpenAPI spec automatically — which wires directly
into this registry's OpenAPI-first approach (docs, codegen, ZAP API
scans) with zero extra work.

## When to use
- Python-stack founders building product APIs: validation, docs, and
  the API contract come from one set of type annotations

## When not to use
- Non-Python stacks; heavy server-rendered HTML products (Django's
  batteries may fit better); CPU-bound work still needs workers `[I]`

## Evidence
- License MIT `[V]` — PyPI metadata 0.139.2 (2026-07-23)
- Published 2026-07-16; frequent releases `[V]` — PyPI history
- Maintainer: Sebastián Ramírez (tiangolo) + team; high individual
  concentration historically, now with org backing `[C]` — bus-factor
  noted but mitigated by enormous adoption and contributor base
- Massive production adoption in the Python ecosystem `[C]`

## Validation results (sandboxed test, 2026-07-23)
- `pip install fastapi==0.139.2` — reproducible
- Defined an endpoint and exercised it via `TestClient` under pytest:
  request→validation→JSON response asserted, **1 passed**, fully offline

## Security findings
- Framework-level: keep Pydantic/Starlette (its foundations) updated —
  advisories usually land there `[I]`; no unresolved material advisories
  located this pass; Scorecard `[U]`

## Legal / licensing findings
- MIT — commercial use permitted.

## Installation
`pip install fastapi==0.139.2 uvicorn`

## Agent integration
Type-annotated endpoints and auto-generated OpenAPI make it unusually
agent-legible: agents can diff the live spec against the committed one
to catch contract drift.

## Required human review
API contract changes (breaking-change review); auth middleware choices.

## Score notes
Functional 19/20 · Security 16/20 · Maintenance 14/15 · Docs 10/10 ·
License 10/10 · Reproducibility 10/10 · Provenance 6/10 · Integration
2/5 → **87**
