# Registry Index

43 entries as of 2026-07-23 (Phase 2) — 38 validated records (31 approved,
6 approved-with-restrictions, 1 experimental) + 4 preserved rejections.
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

## Approved with restrictions

| Name | Function | Restriction summary | Score | Tested |
|---|---|---|---|---|
| [Semgrep CE](security/semgrep.md) | SAST | LGPL engine ✔; official rules non-OSS (internal use only); telemetry with registry configs | 78 | ✅ |
| [Grafana](devops/grafana.md) | Dashboards | AGPL-3.0 network copyleft; open-core; 28-GHSA history → prompt updates mandatory | 83 | – |
| [Plausible CE](marketing-analytics/plausible-ce.md) | Web analytics | AGPL-3.0; CE trails cloud; ClickHouse ops weight | 81 | – |
| [listmonk](marketing-analytics/listmonk.md) | Newsletter/email | AGPL-3.0; single-maintainer; needs external SMTP | 79 | – |
| [Chatwoot](sales-support/chatwoot.md) | Support desk | MIT core but `enterprise/` proprietary; verify 2026-07 advisory fix in pin | 80 | – |
| [Twenty](sales-support/twenty.md) | CRM | AGPL core + per-file `@license Enterprise` markers | 76 | – |

## Experimental

| Name | Function | Why not yet approved |
|---|---|---|
| [promptfoo](ai-engineering/promptfoo.md) | Prompt testing/red-teaming | Telemetry + open-core audits and execution test outstanding |

## Rejected — see [REJECTED.md](REJECTED.md)

Terraform (BUSL-1.1) · Sentry self-hosted (FSL-1.1) · n8n (Sustainable Use
License) · Invoice Ninja v5 (Elastic License 2.0)

## Recheck required — see [RECHECK.md](RECHECK.md)

Scorecard scores, OSV sweep completion, release-signature verification,
Docker-requiring deployment tests, and the Phase 2 items listed there.

## Coverage map vs the 15 scope areas

Covered: security engineering (8), testing/quality (5), DevOps/monitoring
(4), operations: backups + incident response (3), design/UX/accessibility
(3), analytics/email (3), CRM/support (2), finance (1), compliance incl.
AI governance (2), AI engineering (3), mobile (2), product/API standards
(2). **Not yet covered** (see [PHASES.md](../PHASES.md)): CEO/strategy
frameworks, market research, PRD templates, SEO/content tooling,
forecasting, legal templates. Gaps are deliberate — no entry ships without
validation.
