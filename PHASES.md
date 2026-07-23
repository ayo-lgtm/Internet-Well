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

## Phase 3 — Breadth completion (IN PROGRESS, started 2026-07-23)

Completed this pass:

- CEO/strategy: GitLab Handbook (MIT, reference implementation of company
  operations), Open Source Guides (CC-BY-4.0, GitHub), Business Model
  Canvas (CC-BY-SA-3.0, restrictions noted)
- SEO/deliverability: Lighthouse (execution-tested: local-page audit,
  category scores produced) and checkdmarc (execution-tested: live DNS
  SPF/DMARC validation)
- Operational controls/BI: Metabase (AGPL + in-repo commercial editions —
  restrictions documented)
- Sales: EspoCRM added as the mature CRM alternative to Twenty
- Legal ops: Common Paper standard agreements (CC-BY-4.0,
  attorney-committee provenance) + Documenso e-signing (AGPL,
  restrictions); both records hard-require counsel review
- Rejections: Crater (abandoned since 2022), Shape Up (free-to-read but
  no open license)

Still open for later passes:

- Market-research tooling with verifiable provenance (no candidate met
  the evidence bar this pass — gap held open deliberately)
- PRD templates with real provenance; customer-success playbooks
- Keyword/rank tooling; social scheduling (candidates are mostly SaaS or
  unproven — needs deeper discovery)

## Phase 4 — Continuous verification (ACTIVE, started 2026-07-23)

Implemented this pass:

- **Verification tooling**: `automation/verify_registry.py` (then tools/) lints every
  record's front matter (schema, status values, INDEX cross-references)
  and flags entries whose `last_verified` exceeds 90 days; wired into CI
  (`.github/workflows/verify-registry.yml`) on push/PR + weekly cron.
  Its first run caught a hand-count error in INDEX.md.
- **RECHECK closures**: Chatwoot advisory fix confirmed at pin;
  Documenso open-core boundary verified (`packages/ee` exists, root
  LICENSE pure AGPL); parsedmarc promoted from candidate to tested
  record.
- **Remaining scope-gap fills with execution tests**: PostgreSQL (live
  server DDL/DML), FastAPI (TestClient roundtrip), dbmate (full
  migration up/insert/rollback on SQLite), Scrapy (extraction core),
  parsedmarc (offline aggregate-report parse); plus Renovate (dependency
  maintenance; AGPL relicense documented) and C4 Model (architecture
  notation).

Standing loop (the ongoing Phase 4 process):

1. Weekly CI run fails when any entry crosses the 90-day window →
   re-verify that entry per METHODOLOGY, update `last_verified`.
2. On every entry touch: re-read the license at the new pin (license
   drift is the registry's most-observed failure mode: Terraform,
   Sentry, n8n, Grafana, Renovate all relicensed).
3. Advisory check per touch: GitHub security tab (reachable) + OSV/
   Scorecard once network access permits.
4. Environment-blocked debts (Scorecard API, OSV API, Docker deployment
   tests, RubyGems) remain enumerated in evidence/RECHECK.md.

## Phase 5 — founder-os restructure (DONE, 2026-07-23)

Per the founder's design directive:

- Records reorganized into nine registry categories (engineering,
  security, product, design, legal-compliance, marketing, finance,
  operations, launch-maintenance); finer functions preserved in
  `subcategory` front matter.
- New top-level structure: `skills/` (approved/experimental/deprecated —
  none approved yet, bar documented), `evaluations/` (execution-test
  transcript), `licenses/` (obligations matrix), `evidence/` (policy +
  RECHECK ledger), `schemas/` (record contract, MD + JSON Schema),
  `workflows/` (adopt-a-dependency, re-verify-entry, incident-response
  bootstrap, launch checklist), `rejected/` (tier-D docket),
  `automation/` (linter + generated index).
- A/B/C/D tier model added to every record with enforced rules: Tier A
  requires human review — always, and non-negotiably in sensitive areas;
  initial state is 0×A, 38×B, 17×C, 6×D. `human_reviewed` may only be
  set by a person.
- `registry/INDEX.md` is now generated (`automation/build_index.py`),
  eliminating the hand-count drift class; CI checks both linter and
  index freshness.
- README now states the no-vendoring rationale and the honest
  cannot-guarantee list; METHODOLOGY §1a names the standard verification
  signals (OpenSSF Scorecard, SLSA, SPDX, dependency graph, Dependabot)
  with the explicit caveat that signals are evidence, not proof of
  safety.
