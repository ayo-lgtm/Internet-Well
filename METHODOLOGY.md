# Validation Methodology

This document defines how every resource in the registry is discovered,
validated, classified, scored, and recorded. Agents extending the registry
must follow this protocol; entries that do not follow it must be marked
`recheck-required`.

## 1. Discovery sources (in order of preference)

1. Official standards bodies and professional organizations (OWASP, OpenSSF,
   Linux Foundation, CNCF, FSFE, W3C, NIST, government design systems)
2. GitHub organizations maintained by established institutions
3. Official project documentation and websites
4. Package registries (npm, PyPI, crates.io, Go module proxy) — download
   stats, dependent counts, publish history
5. Release and commit histories via the GitHub REST API
6. Published security advisories (GitHub Security Advisories, NVD/CVE)
7. Independent technical evaluations and academic publications
8. Real-world adoption evidence (public production users, distro packaging,
   inclusion in institutional toolchains)

**Not acceptable as sufficient evidence:** promotional listicles,
"awesome-*" list inclusion, repository self-descriptions, social-media
claims, GitHub stars. Stars may be recorded as context but never justify
approval.

## 1a. Standard verification signals

The verification foundation uses these named, defensible signals:

- **OpenSSF Scorecard** — automated open-source security-health checks
  (API access noted per environment; see §4)
- **SLSA** — build integrity and software provenance levels; recorded
  where releases publish provenance/attestations
- **SPDX** — standardized license identifiers and SBOM data (used in
  every record's `license` field and in Syft/Trivy SBOM output)
- **GitHub dependency graph** — dependency, license, and vulnerability
  visibility for hosted repos
- **GitHub Dependabot alerts** — known-vulnerable dependency signals

These signals do not prove a repository is safe. They provide defensible
verification evidence; interpretation and acceptance remain judgments,
and sensitive areas additionally require human review (§5a).

## 1b. No vendoring

The registry never copies upstream repositories into this repository.
Copies create license/attribution complications, rapidly outdated code,
unpatched vulnerabilities, enormous history, dependency conflicts,
upstream-tracking difficulty, and malicious-code exposure. Every record
points to a pinned upstream release (with a VCS hash where obtainable).
Fork only when you actually need to modify or preserve a project — and
only after confirming its license allows the intended use.

## 2. Mandatory validation checklist

Every record must capture (or explicitly mark `unknown` with a reason):

- Canonical repository URL and official website
- Exact purpose and the company function(s) it serves
- Resource type: executable tool / framework / template / standard /
  reference implementation / agent skill / combination
- License as an SPDX identifier, verified from the repository's license
  file or the registry metadata of the package — never from the README badge
  alone when they conflict
- Commercial-use, modification, redistribution, and SaaS permissions;
  copyleft, attribution, source-disclosure, and network-use (AGPL §13)
  obligations; open-core boundaries (directories under a different license)
- Latest stable release, release cadence, last meaningful commit
- Maintainer count and concentration (bus factor), institutional backing
- Archived / abandoned / maintenance-mode status
- Security policy presence, known CVEs, unresolved material security issues
- Release signing / provenance and SBOM availability, where ascertainable
- CI status and test evidence
- Documentation quality and installation reproducibility
- Supported platforms and stacks
- External services, API keys, paid dependencies, telemetry, hidden costs
- Data handling and privacy implications
- Limitations — what it cannot reliably do
- Verification date for the record

## 3. Claim classification

Every material claim in a record is tagged with one of:

| Tag | Meaning |
|---|---|
| `[V]` Verified | Confirmed directly from primary evidence (API response, license file, registry metadata, official release page) during this research |
| `[C]` Corroborated | Multiple independent reliable sources agree |
| `[M]` Maintainer-claimed | Stated by the project; not independently verified |
| `[R]` Community-reported | Reported by users; not independently verified |
| `[I]` Inference | Reasoned conclusion from verified facts |
| `[U]` Unknown | Could not be determined |

Prohibited language: a project may not be described as "expert-verified,"
"secure," "production-ready," "compliant," or "best" unless evidence
supports that exact description. Use precise statements ("no unresolved
critical advisories found as of the verification date") instead.

## 4. Testing protocol

Where safe and practicable, in an isolated environment with no credentials:

1. Pin the exact commit or release tested
2. Inspect installation scripts before execution
3. Install from the official package registry (not arbitrary curl|sh)
4. Generate or inspect the dependency inventory
5. Run the documented test suite or a representative workflow
6. Record reproducible commands, outputs, failures, and environment details

Never execute untrusted code on a host holding credentials or confidential
data. If testing was not performed, the record's `validation.tested` field
must say `false` and confidence must be capped at `medium`.

### Environment limitations of the initial research pass (2026-07)

Recorded here so results are interpretable:

- GitHub REST API, package registries (npm, PyPI, crates.io, Go proxy), and
  public web pages were reachable → license files, archived flags, release
  and commit recency, publish histories, and official docs were verifiable
  first-hand.
- The OpenSSF Scorecard API (`api.securityscorecards.dev`, `api.scorecard.dev`)
  and `deps.dev` were **not reachable** from the research environment
  (network policy). Scorecard results are therefore marked `[U]` unless
  visible through another primary source, and listed in `RECHECK.md`.
- Cloning arbitrary third-party repositories was restricted; execution
  testing was limited to packages installable from the allowed registries.
  Records state per-entry whether a smoke test ran.

## 5. Scoring rubric (0–100)

| Dimension | Weight |
|---|---|
| Functional quality | 20 |
| Security posture | 20 |
| Maintenance health | 15 |
| Documentation and usability | 10 |
| License suitability | 10 |
| Reproducibility and testing | 10 |
| Professional provenance | 10 |
| Integration readiness | 5 |
| **Total** | **100** |

Scores are comparative judgments grounded in the recorded evidence; the
per-dimension notes in each record explain deductions. A high score is not a
warranty.

## 5a. Approval tiers (A/B/C/D)

Every record carries a `tier` in addition to its status and score:

| Tier | Meaning |
|---|---|
| **A** | Strong primary evidence, active maintenance, suitable license, strong security posture, reproducibly tested — **and reviewed by a competent human** |
| **B** | Generally reliable but has documented limitations or dependencies |
| **C** | Promising and useful for experimentation; insufficient evidence for critical work |
| **D** | Rejected: abandoned, unsafe, legally unsuitable, or unverifiable (recorded in `rejected/README.md`) |

Enforced rules (`automation/verify_registry.py`):

- Tier A requires status `approved`, `tested: true`, `confidence: high`,
  and `human_reviewed: true`. **Automated scoring alone can never produce
  Tier A** — in sensitive areas (security, legal-compliance, finance,
  privacy, production deployment) this is non-negotiable, and the rule is
  applied registry-wide for consistency.
- `human_reviewed` is set by a person after reviewing the record and its
  evidence; agents must never set it.
- Experimental records are always Tier C.
- The registry's initial state is zero Tier A — every entry was validated
  by agent research; founders promote entries after their own review.

## 6. Hard disqualification rules

A resource is `rejected` regardless of score if any of the following holds:

- No ascertainable license, or license prohibits commercial use
- License is source-available but not open source per the Open Source
  Definition (e.g. BUSL, SSPL, Elastic License, FSL, Sustainable Use
  License, Commons Clause) — recorded in `REJECTED.md` with evidence, since
  these are the most common false "open source" recommendations
- Malicious or suspicious behavior (typosquatting, undisclosed telemetry,
  credential collection)
- Material unresolved vulnerabilities without mitigation
- Abandoned/archived where active maintenance is essential to the function
- False or unverifiable professional claims central to its value
- Irreproducible installation

`approved-with-restrictions` is used where the resource is genuinely open
source but carries obligations a founder must actively manage (AGPL network
copyleft, open-core boundaries, non-OSS rule/content licenses, trademark
constraints).

## 7. Record schema

The record front-matter contract lives in
[`schemas/record-schema.md`](schemas/record-schema.md) (human-readable)
and [`schemas/record.schema.json`](schemas/record.schema.json)
(machine-readable), and is enforced by `automation/verify_registry.py` —
including the tier rules from §5a. Categories are the nine registry
directories; finer functions go in `subcategory`.

Body sections: What it does · When to use · When not to use · Evidence
(with claim tags and sources — see `evidence/README.md`) · Validation
results · Security findings · Legal/licensing findings · Installation ·
Agent integration · Required human review · Score notes.
