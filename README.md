# Founder OS — Verified Open-Source Resource Registry

A rigorously verified, evidence-based registry of genuinely free and
open-source tools, frameworks, templates, standards, and reference
implementations for solo software founders building, securing, launching,
operating, and scaling a software company.

**This is not a link collection.** Every entry is individually validated
against primary evidence (repository APIs, package registries, official
project documentation, license texts, release histories) before it is
approved, and every material claim is classified by evidence strength.
Rejected candidates are preserved with reasons so future research does not
re-recommend them.

## How to use this registry

- **Founders**: start at [`registry/INDEX.md`](registry/INDEX.md), filter by
  company function, and read the "when to use / when not to use / required
  human review" fields before adopting anything.
- **AI agents**: treat this registry as a pre-vetted shortlist, not an
  install script. Respect the `required_human_review` field of each record,
  and never install a resource whose `status` is not `approved` or
  `approved-with-restrictions` without human confirmation. Re-verify any
  record whose `last_verified` date is older than 90 days.

## Repository layout

| Path | Contents |
|---|---|
| [`METHODOLOGY.md`](METHODOLOGY.md) | Validation protocol, evidence rules, claim classification, scoring rubric, disqualification rules |
| [`PHASES.md`](PHASES.md) | Research phase plan and current status |
| [`registry/INDEX.md`](registry/INDEX.md) | Master index of all records by status and category |
| `registry/<category>/*.md` | One structured record per resource (YAML front matter + narrative evidence) |
| [`registry/REJECTED.md`](registry/REJECTED.md) | Rejected candidates with preserved reasons |
| [`registry/RECHECK.md`](registry/RECHECK.md) | Entries needing re-verification and why |

## Honest limitations

- This registry does **not** eliminate bugs, guarantee compliance, replace
  licensed professionals (lawyers, accountants, auditors), or ensure
  commercial success. Records state explicitly where professional review is
  required.
- Facts decay. Licenses change (this registry contains examples of formerly
  open-source projects that relicensed), maintainers leave, CVEs appear.
  Every fact carries a `last_verified` date; treat older facts as stale.
- Verification depth varies and is recorded per entry as a confidence level.
  Where sandboxed execution testing was not performed, the record says so.

## License

Registry content (this repository's own text) is licensed under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). The resources it
describes retain their own licenses, recorded per entry as SPDX identifiers.
