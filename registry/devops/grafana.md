---
name: Grafana
category: devops-infrastructure
subcategory: observability-dashboards
status: approved-with-restrictions
type: tool
canonical_repo: https://github.com/grafana/grafana
website: https://grafana.com
pinned_version: v13.1.1 (2026-07-21)
license: AGPL-3.0-only (with per-directory Apache-2.0 exceptions per LICENSING.md)
score: 83
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Grafana — dashboards and observability UI

## What it does
Visualization and alerting layer over Prometheus, Loki, Postgres, and
dozens of other data sources; the standard dashboard companion to
Prometheus.

## When to use
- Self-hosted dashboards over your own metrics/logs for internal use —
  AGPL imposes no obligations for internal operation

## When not to use / restrictions
- **AGPL-3.0**: if you modify Grafana and let users interact with it over a
  network, you must offer your modified source to those users (§13). If you
  embed dashboards in a customer-facing product, involve a lawyer or use
  unmodified upstream builds and keep modifications upstream.
- Relicensed from Apache-2.0 to AGPLv3 in 2021 `[C]` — an example of the
  license-drift risk this registry tracks. Some components remain
  Apache-2.0 per LICENSING.md `[V]`.
- Grafana Cloud/Enterprise features are proprietary (open-core boundary).

## Evidence
- License AGPL-3.0 with documented exceptions `[V]` — repo license +
  LICENSING.md reference (2026-07-23)
- Latest v13.1.1, 2026-07-21; very active (71k+ commits, 628 releases)
  `[V]` — repository page
- Corporate maintainer: Grafana Labs `[V]`
- Massive adoption `[C]` — context only

## Validation results
- Not execution-tested this pass (server deployment; Phase 2 docker test).
  Versioned OSS container images documented `[V]`.

## Security findings
- Ships with default admin credentials on first run — change immediately;
  keep it off the public internet or behind SSO `[C]` — official hardening
  docs. No unresolved material advisories located this pass; note Grafana
  has had serious CVEs historically (e.g. path traversal CVE-2021-43798),
  all patched in current majors `[C]` — advisory records; keep updated.

## Legal / licensing findings
- AGPL-3.0-only: commercial use and SaaS permitted; network-use source
  obligation applies to modified versions made available to users;
  trademark "Grafana" is Grafana Labs'.

## Installation
`grafana/grafana-oss:13.1.1` container image (use the `-oss` image, not
`-enterprise`, to stay on the open-source edition).

## Agent integration
Dashboards/alerts as code via provisioning YAML — agents can propose
provisioning changes through PRs; credentials handling is human.

## Required human review
Any customer-facing embedding (license), auth configuration, upgrades.

## Score notes
Functional 19/20 · Security 15/20 (CVE history, default-cred footgun) ·
Maintenance 15/15 · Docs 9/10 · License 6/10 (AGPL + open-core boundary
management) · Reproducibility 7/10 · Provenance 8/10 · Integration 4/5
→ **83**
