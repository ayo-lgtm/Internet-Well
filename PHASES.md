# Research Phase Plan

Verification quality takes precedence over list size. Each phase produces
fully validated records; no phase publishes unverified entries.

## Phase 1 — Core toolchain and cross-function foundation (IN PROGRESS, started 2026-07-23)

Tranches:

- **1a Security & supply chain**: secrets detection, SAST, DAST, dependency
  scanning, SBOM, threat modeling, security standards (OWASP/OpenSSF).
- **1b Testing, code quality, DevOps**: E2E and unit testing, linting,
  pre-commit hygiene, IaC, monitoring/alerting, uptime.
- **1c Business functions**: accessibility, design systems, product/decision
  templates, API standards, analytics, email/newsletter, CRM/support,
  finance/bookkeeping, license compliance.
- **1d Rejection docket**: commonly recommended tools that fail the
  open-source disqualification rules, with license evidence preserved.

## Phase 2 — Depth and execution testing (IN PROGRESS, started 2026-07-23)

Completed this pass:

- Execution tests closed for syft (SPDX SBOM generation), scancode-toolkit
  (license+copyright detection), hledger (distro version; double-entry
  roundtrip), govuk-frontend (render + clean axe scan), restic (full
  encrypted backup→restore→verify roundtrip), Inspect AI (offline eval via
  mock model); OpenTofu and Trivy source-build attempts documented
  (including the finding that `go install` is not a supported OpenTofu
  install path)
- GitHub advisory sweep for the PII-holding server apps (Grafana 28 GHSAs,
  Chatwoot 4 incl. 2026 SQLi, Uptime Kuma 10+ incl. 2026 SSTI) — recorded
  in the affected records
- New tranches: operations (restic, BorgBackup, PagerDuty incident
  response), mobile (fastlane, OWASP MASVS), AI engineering/governance
  (Inspect AI, OWASP LLM Top 10, NIST AI RMF, promptfoo as experimental)

Still open (carried in RECHECK.md):

- OpenSSF Scorecard API and OSV API remain blocked from this environment
- Docker-requiring server deployments (daemon unavailable in sandbox):
  Grafana, Penpot, Chatwoot, Twenty, Plausible, Umami, listmonk, ZAP,
  Prometheus, Uptime Kuma, Threat Dragon
- BorgBackup executable retest; promptfoo telemetry audit before approval

## Phase 3 — Breadth completion (PLANNED)

- CEO/strategy and market-research frameworks with verifiable provenance
- SEO/content/social tooling; deliverability testing
- Sales pipelines, customer-success playbooks
- Forecasting and operational controls
- Legal templates (with explicit professional-review requirements)

## Phase 4 — Continuous verification (PLANNED)

- 90-day re-verification sweep driven by `last_verified` dates
- CVE/advisory monitoring for approved entries
- License-change detection (several Phase 1 rejections were relicensing
  events; this is a recurring risk)
