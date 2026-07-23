# License Obligations Matrix

Derived from the validated records (2026-07-23). Each row links the SPDX
family to its practical obligations for a founder using, modifying, or
offering the software as part of a service. **Not legal advice.**

## Permissive — use, modify, redistribute, SaaS all permitted

| License | Obligations | Records |
|---|---|---|
| MIT | Preserve license/copyright notice in copies | Gitleaks, pytest, Vitest, Ruff, pre-commit, FastAPI, Inspect AI, Uptime Kuma, Umami, Chatwoot (core; see open-core row), fastlane, dbmate, GOV.UK Frontend (code; Crown branding excluded), GitLab Handbook (repo), MADR (or CC0) |
| Apache-2.0 | Preserve NOTICE/attribution; patent grant included | Trivy, ZAP, Syft, Grype, OpenSSF Scorecard, Threat Dragon, Playwright, Prometheus, Grafana (exception dirs only), Lighthouse, checkdmarc, parsedmarc, PagerDuty IR docs, OpenAPI Spec, ScanCode (code) |
| BSD-2/3-Clause | Preserve notices | restic (BSD-2), BorgBackup (BSD-3), Scrapy (BSD-3) |
| PostgreSQL License | Preserve notice | PostgreSQL |

## Weak copyleft — file-level share-back on modified files only

| License | Obligations | Records |
|---|---|---|
| MPL-2.0 | Modified MPL files must stay MPL when distributed; rest of your code unaffected | OpenTofu, axe-core, Penpot |
| LGPL-2.1 | Modified engine must be LGPL if distributed; linking/use unaffected | Semgrep CE engine (rules are NOT open source — see non-OSS row) |

## Network copyleft (AGPL-3.0) — §13 applies to modified network services

Using unmodified builds internally or serving users: permitted, no source
obligation. **Modifying** and letting users interact over a network:
offer them the modified source.

| Records | Extra caveats |
|---|---|
| Grafana | Relicensed Apache-2.0→AGPL in 2021; open-core |
| Plausible CE | Tracker snippet is MIT; CE trails cloud features |
| listmonk | — |
| Twenty | Plus per-file `@license Enterprise` commercial markers |
| EspoCRM | Paid proprietary extensions at edges |
| Metabase OSS | In-repo commercial editions + separate embedding terms |
| Documenso | `packages/ee` enterprise directory |
| Renovate | Relicensed MIT→AGPL-3.0-only (2025) |

## Content licenses (standards, templates, references)

| License | Obligations | Records |
|---|---|---|
| CC-BY-4.0 | Attribution | Open Source Guides, Common Paper agreements, C4 Model, ScanCode license data |
| CC-BY-SA-4.0 | Attribution + ShareAlike on distributed derivatives (internal use unaffected) | OWASP ASVS, MASVS, LLM Top 10 |
| CC-BY-SA-3.0 | Attribution (visibly, per Strategyzer terms) + ShareAlike | Business Model Canvas |
| Public domain (17 U.S.C. §105) | None; no endorsement implication | NIST AI RMF |
| GPL-3.0-or-later | Copyleft on distributing modified tool; using it and its output imposes nothing | hledger |

## Open-core boundaries to audit before building on a feature

Chatwoot `enterprise/` · Twenty `@license Enterprise` file markers ·
Metabase commercial editions + LICENSE-EMBEDDING · Documenso
`packages/ee` · EspoCRM paid extensions · Semgrep Pro rules/platform.

## Non-OSS licenses found on commonly recommended tools → rejected

BUSL-1.1 (Terraform) · FSL-1.1 (Sentry) · Sustainable Use License (n8n) ·
Elastic License 2.0 (Invoice Ninja) · Semgrep Rules License v1.0
(official semgrep-rules — internal use only). Details with license-text
evidence: [`../rejected/README.md`](../rejected/README.md).
