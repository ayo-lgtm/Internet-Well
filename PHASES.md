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

## Phase 2 — Depth and execution testing (PLANNED)

- Sandboxed execution tests for entries marked `tested: false` where an
  environment with clone access is available
- OpenSSF Scorecard retrieval for all entries (blocked by network policy in
  Phase 1 — see METHODOLOGY §4)
- Mobile engineering, iOS/Android toolchains, App Store / Play launch
  checklists
- AI engineering and AI governance (evaluation harnesses, model/dataset
  license analysis, NIST AI RMF alignment)
- Backup/restore, incident response, on-call and postmortem templates

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
