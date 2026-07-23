# Registry Index

61 entries as of 2026-07-23 (Phase 4) — 55 validated records (42 approved,
12 approved-with-restrictions, 1 experimental) + 6 preserved rejections;
22 records execution-tested. Counts are machine-checked by
`tools/verify_registry.py` (which caught an off-by-one in the previous
hand-counted header).
Statuses: ✅ approved · ⚠️ approved-with-restrictions · 🧪 experimental ·
❌ rejected. Scores per METHODOLOGY §5; standards/templates unscored by
design. `tested` = sandboxed execution test performed (¹ = tested at a
distro version, not the pin — see record).

## Approved

| Name | Function | Type | License | Version pinned | Score | Tested |
|---|---|---|---|---|---|---|
| [Gitleaks](security/gitleaks.md) | Secrets detection | tool | MIT | v8.30.1 | 84 | ✅ |
| [Trivy](security/trivy.md) | Vuln/misconfig/SBOM scanning | tool | Apache-2.0 | v0.72.0 | 89 | – |
| [ZAP](security/zaproxy.md) | DAST | tool | Apache-2.0 | v2.17.0 | 85 | – |
| [Syft](security/syft.md) | SBOM generation | tool | Apache-2.0 | v1.49.0 | 86 | ✅ |
| [Grype](security/grype.md) | Vulnerability scanning | tool | Apache-2.0 | v0.116.0 | 85 | – |
| [OWASP Threat Dragon](security/owasp-threat-dragon.md) | Threat modeling | tool | Apache-2.0 | v2.6.2 | 75 | – |
| [OWASP ASVS](security/owasp-asvs.md) | Security requirements | standard | CC-BY-SA-4.0 | v5.0.0 | n/a | n/a |
| [OpenSSF Scorecard](security/openssf-scorecard.md) | Supply-chain health | tool | Apache-2.0 | v5.5.0 | 84 | – |
| [Playwright](testing-quality/playwright.md) | E2E testing | framework | Apache-2.0 | 1.61.1 | 90 | ✅ |
| [pytest](testing-quality/pytest.md) | Python testing | framework | MIT | 9.1.1 | 91 | ✅ |
| [Vitest](testing-quality/vitest.md) | JS/TS testing | framework | MIT | 4.1.10 | 87 | ✅ |
| [Ruff](testing-quality/ruff.md) | Python lint/format | tool | MIT | 0.15.22 | 88 | ✅ |
| [pre-commit](testing-quality/pre-commit.md) | Git hook manager | framework | MIT | 4.6.1 | 85 | ✅ |
| [OpenTofu](devops/opentofu.md) | Infrastructure as code | tool | MPL-2.0 | v1.12.5 | 86 | ✅ |
| [Prometheus](devops/prometheus.md) | Metrics + alerting | tool | Apache-2.0 | v3.13.1 | 88 | – |
| [Uptime Kuma](devops/uptime-kuma.md) | Uptime + status page | tool | MIT | 2.4.0 | 78 | – |
| [restic](operations/restic.md) | Backups | tool | BSD-2-Clause | v0.19.1 | 87 | ✅ |
| [BorgBackup](operations/borgbackup.md) | Backups | tool | BSD-3-Clause | 1.4.5 | 78 | – |
| [PagerDuty IR Docs](operations/pagerduty-incident-response.md) | Incident response process | reference | Apache-2.0 | master | n/a | n/a |
| [axe-core](design-ux/axe-core.md) | Accessibility testing | tool | MPL-2.0 | 4.12.1 | 88 | ✅ |
| [GOV.UK Frontend](design-ux/govuk-frontend.md) | Design system | framework | MIT | 6.4.0 | 85 | ✅ |
| [Penpot](design-ux/penpot.md) | Design/prototyping | tool | MPL-2.0 | 2.17.0 | 80 | – |
| [Umami](marketing-analytics/umami.md) | Web analytics | tool | MIT | v3.2.0 | 79 | – |
| [hledger](finance/hledger.md) | Bookkeeping | tool | GPL-3.0-or-later | 1.52.1 | 80 | ✅¹ |
| [ScanCode Toolkit](compliance/scancode-toolkit.md) | License compliance | tool | Apache-2.0 + CC-BY-4.0 | 32.5.0 | 82 | ✅ |
| [NIST AI RMF](compliance/nist-ai-rmf.md) | AI governance | standard | Public domain (US) | AI 100-1 / 600-1 | n/a | n/a |
| [Inspect AI](ai-engineering/inspect-ai.md) | LLM evaluation | framework | MIT | 0.3.249 | 84 | ✅ |
| [OWASP LLM Top 10](ai-engineering/owasp-llm-top10.md) | AI security risks | standard | CC-BY-SA-4.0 | v2.0 | n/a | n/a |
| [fastlane](mobile/fastlane.md) | Mobile release automation | tool | MIT | 2.237.0 | 82 | – |
| [OWASP MASVS](mobile/owasp-masvs.md) | Mobile security standard | standard | CC-BY-SA-4.0 | v2.1.0 | n/a | n/a |
| [MADR](product-strategy/madr.md) | Decision records | template | MIT OR CC0-1.0 | 4.0.0 | n/a | n/a |
| [OpenAPI Spec](product-strategy/openapi-specification.md) | API contract standard | standard | Apache-2.0 | 3.2.0 | n/a | n/a |
| [Lighthouse](marketing-analytics/lighthouse.md) | SEO/perf/a11y audits | tool | Apache-2.0 | 13.4.1 | 88 | ✅ |
| [checkdmarc](marketing-analytics/checkdmarc.md) | Email auth validation | tool | Apache-2.0 | 5.17.3 | 79 | ✅ |
| [GitLab Handbook](product-strategy/gitlab-handbook.md) | Company-ops reference | reference | MIT | rolling | n/a | n/a |
| [Open Source Guides](product-strategy/opensource-guide.md) | OSS strategy | reference | CC-BY-4.0 | rolling | n/a | n/a |
| [Common Paper agreements](operations/common-paper-csa.md) | Legal templates (counsel required) | template | CC-BY-4.0 | CSA v2.1 | n/a | n/a |
| [PostgreSQL](devops/postgresql.md) | Database | tool | PostgreSQL | 16.13 | 93 | ✅ |
| [FastAPI](devops/fastapi.md) | Backend API framework | framework | MIT | 0.139.2 | 87 | ✅ |
| [dbmate](devops/dbmate.md) | Schema migrations | tool | MIT | v2.34.1 | 83 | ✅ |
| [parsedmarc](marketing-analytics/parsedmarc.md) | DMARC report analysis | tool | Apache-2.0 | 10.2.4 | 80 | ✅ |
| [C4 Model](product-strategy/c4-model.md) | Architecture diagrams | standard | CC-BY-4.0 | current | n/a | n/a |

## Approved with restrictions

| Name | Function | Restriction summary | Score | Tested |
|---|---|---|---|---|
| [Semgrep CE](security/semgrep.md) | SAST | LGPL engine ✔; official rules non-OSS (internal use only); telemetry with registry configs | 78 | ✅ |
| [Grafana](devops/grafana.md) | Dashboards | AGPL-3.0 network copyleft; open-core; 28-GHSA history → prompt updates mandatory | 83 | – |
| [Plausible CE](marketing-analytics/plausible-ce.md) | Web analytics | AGPL-3.0; CE trails cloud; ClickHouse ops weight | 81 | – |
| [listmonk](marketing-analytics/listmonk.md) | Newsletter/email | AGPL-3.0; single-maintainer; needs external SMTP | 79 | – |
| [Chatwoot](sales-support/chatwoot.md) | Support desk | MIT core but `enterprise/` proprietary; verify 2026-07 advisory fix in pin | 80 | – |
| [Twenty](sales-support/twenty.md) | CRM | AGPL core + per-file `@license Enterprise` markers | 76 | – |
| [EspoCRM](sales-support/espocrm.md) | CRM (mature) | AGPL-3.0; paid proprietary extensions at edges | 79 | – |
| [Metabase OSS](finance/metabase.md) | BI dashboards | AGPL + in-repo commercial editions; embedding terms | 80 | – |
| [Documenso](operations/documenso.md) | E-signature | AGPL; enterprise boundary unverified; counsel on validity | 76 | – |
| [Business Model Canvas](product-strategy/business-model-canvas.md) | Business modeling | CC-BY-SA-3.0 attribution + ShareAlike on derivatives | n/a | n/a |
| [Scrapy](product-strategy/scrapy.md) | Market-research data collection | Legal/ethical crawl constraints are user's burden | 84 | ✅ |
| [Renovate](devops/renovate.md) | Dependency updates | AGPL-3.0 (2025 relicense from MIT); repo write access | 82 | – |

## Experimental

| Name | Function | Why not yet approved |
|---|---|---|
| [promptfoo](ai-engineering/promptfoo.md) | Prompt testing/red-teaming | Telemetry + open-core audits and execution test outstanding |

## Rejected — see [REJECTED.md](REJECTED.md)

Terraform (BUSL-1.1) · Sentry self-hosted (FSL-1.1) · n8n (Sustainable Use
License) · Invoice Ninja v5 (Elastic License 2.0) · Crater (abandoned
since 2022) · Shape Up (free-to-read, no open license)

## Recheck required — see [RECHECK.md](RECHECK.md)

Scorecard scores, OSV sweep completion, release-signature verification,
Docker-requiring deployment tests, and the Phase 2 items listed there.

## Coverage map vs the 15 scope areas

All 15 scope areas now have at least one validated entry: CEO/strategy
(4), market research (1 — Scrapy, data-collection with legal
restrictions), product/PRD-adjacent standards (MADR, OpenAPI, C4),
architecture (C4, MADR), engineering (PostgreSQL, FastAPI + the testing
stack), testing/quality (5), security (8), compliance incl. privacy/
licensing/AI governance (2 + ScanCode), design/UX/accessibility (3),
DevOps/CI/monitoring/backups/incident response (10+), launch prep
(fastlane, MASVS, Lighthouse), marketing/SEO/email (7), sales/CRM/support
(3), finance/BI (2), post-launch maintenance (Renovate, dbmate,
advisory-sweep practice). **Remaining thin spots, held open honestly**
(see [PHASES.md](../PHASES.md)): PRD templates with real provenance,
customer-success playbooks, keyword/rank tooling, forecasting beyond
hledger budgets + Metabase — no candidate met the evidence bar yet.
