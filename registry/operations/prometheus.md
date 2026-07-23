---
name: Prometheus
category: operations
subcategory: monitoring-metrics
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/prometheus/prometheus
website: https://prometheus.io
pinned_version: v3.13.1 (Go module v0.313.1, commit 73ff57ce2b8161059ac7fe5188f03f1c3d22b29a, 2026-07-10)
license: Apache-2.0
score: 88
confidence: high
tested: false
last_verified: 2026-07-23
---

# Prometheus — metrics collection, storage, and alerting

## What it does
Pull-based time-series metrics database with the PromQL query language and
integrated alerting (Alertmanager). The de facto open standard for service
metrics; client libraries exist for every mainstream language.

## When to use
- Default metrics + alerting backbone for a founder's production services
- Instrumenting your own app via official client libraries from day one

## When not to use
- Long-term/high-cardinality analytics storage (pair with remote storage
  like Thanos/Mimir when you actually need it — usually not at solo scale)
- Log aggregation or tracing (different tools; Phase 2)

## Evidence
- License Apache-2.0 `[V]` — repository (2026-07-23)
- Latest release: Go proxy reports module v0.313.1 (= project release
  v3.13.1 under Prometheus's module-versioning convention), 2026-07-10,
  commit 73ff57c `[V]`
- Institutional provenance: graduated CNCF project (the second ever, after
  Kubernetes) with multi-org maintainer team `[C]` — CNCF records
- Massive production adoption across the industry `[C]` — CNCF surveys,
  ecosystem integrations; recorded as context

## Validation results
- Not execution-tested this pass (server deployment test deferred to
  Phase 2). Versioned binaries and containers documented `[V]`.

## Security findings
- No authentication on the built-in web UI/API by default — never expose it
  publicly without a reverse proxy or TLS+auth layer `[C]` — official
  security model documentation
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- Apache-2.0 — commercial use, SaaS, redistribution permitted.

## Installation
Official versioned container images (`prom/prometheus:v3.13.1`) or distro
packages; pin image digests in production.

## Agent integration
PromQL over the HTTP API is agent-friendly for read-only health queries;
alert-rule changes should go through code review like any config change.

## Required human review
Alert-rule changes, retention/storage sizing, and anything exposing
endpoints to the internet.

## Score notes
Functional 19/20 · Security 16/20 (no built-in auth; deliberate design but
a real footgun) · Maintenance 15/15 · Docs 9/10 · License 10/10 ·
Reproducibility 7/10 · Provenance 10/10 · Integration 2/5 (server to
operate, client libs to wire) → **88**
