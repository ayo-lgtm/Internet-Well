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

Each record is a Markdown file with YAML front matter:

```yaml
name: ""
category: ""            # one of the 15 scope areas
subcategory: ""
status: ""              # approved | approved-with-restrictions | experimental | rejected | recheck-required
type: ""                # tool | framework | template | standard | reference-implementation | agent-skill
canonical_repo: ""
website: ""
pinned_version: ""      # release tag or commit verified
license: ""             # SPDX id; note open-core boundaries in body
score: 0                # per rubric; omit for standards/templates where execution dimensions don't apply
confidence: ""          # high | medium | low
tested: false           # sandboxed execution test performed
last_verified: ""       # YYYY-MM-DD
```

Body sections: What it does · When to use · When not to use · Evidence
(with claim tags and sources) · Validation results · Security findings ·
Legal/licensing findings · Installation · Agent integration · Required
human review · Score notes.
