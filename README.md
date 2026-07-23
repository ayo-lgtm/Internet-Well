# Founder OS — Verified Open-Source Resource Registry

A rigorously verified, evidence-based registry of genuinely free and
open-source tools, frameworks, templates, standards, and reference
implementations for solo software founders building, securing, launching,
operating, and scaling a software company.

**This is a registry, not a collection of copied repositories.** Every
entry points to a pinned upstream release and is individually validated
against primary evidence (repository APIs, package registries, license
texts, release histories, sandboxed execution tests). Copying upstream
code here would create license complications, stale copies, unpatched
vulnerabilities, and malicious-code exposure — so we never do it (see
METHODOLOGY §1b). Rejected candidates are preserved with reasons so the
same unsuitable resources are not re-recommended.

## Repository layout

| Path | Contents |
|---|---|
| [`registry/`](registry/INDEX.md) | One validated record per resource, in nine function categories: engineering, security, product, design, legal-compliance, marketing, finance, operations, launch-maintenance |
| [`registry/INDEX.md`](registry/INDEX.md) | **Generated** master index (never hand-edited) |
| [`skills/`](skills/README.md) | Agent skills: approved / experimental / deprecated (none approved yet — the bar is documented) |
| [`evaluations/`](evaluations/README.md) | Reproducible execution-test transcript, including failed attempts |
| [`licenses/`](licenses/README.md) | License obligations matrix across all records |
| [`evidence/`](evidence/README.md) | Evidence policy, claim tags, and the open-debt ledger ([RECHECK.md](evidence/RECHECK.md)) |
| [`schemas/`](schemas/record-schema.md) | Record front-matter contract (Markdown + JSON Schema) |
| [`workflows/`](workflows/) | Professional workflows: adopt-a-dependency, re-verify-entry, incident-response bootstrap, launch checklist |
| [`rejected/`](rejected/README.md) | Tier-D candidates with preserved evidence and reasons |
| [`automation/`](automation/) | Registry linter (tier rules, staleness) + index generator, run weekly in CI |
| [`METHODOLOGY.md`](METHODOLOGY.md) | Validation protocol, evidence rules, tier model, scoring, disqualification rules |
| [`PHASES.md`](PHASES.md) | Research phase history and the standing verification loop |

## Approval tiers

| Tier | Meaning |
|---|---|
| A | Strong primary evidence, active maintenance, suitable license, strong security posture, reproducibly tested — and human-reviewed. **Sensitive areas (security, legal, finance, privacy, production deployment) can never reach Tier A from automated scoring alone.** |
| B | Generally reliable but has documented limitations or dependencies |
| C | Promising, useful for experimentation; insufficient evidence for critical work |
| D | Rejected, abandoned, unsafe, legally unsuitable, or unverifiable |

The registry currently contains **zero Tier A entries** — every record was
validated by agent research, and Tier A requires human review by design.
That is the honest starting state, not a defect.

## How to use this registry

- **Founders**: start at [`registry/INDEX.md`](registry/INDEX.md); read
  each record's "when not to use" and "required human review" before
  adopting; follow [`workflows/`](workflows/) for repeatable processes.
- **AI agents**: treat records as a pre-vetted shortlist, not an install
  script. Respect `required_human_review` and tier rules; never set
  `human_reviewed`; re-verify anything older than 90 days
  ([workflow](workflows/reverify-entry.md)).

## What this registry cannot honestly guarantee

Even the best-verified collection cannot guarantee:

- A launch without bugs
- Compliance in every jurisdiction
- Successful product-market fit
- Secure deployment under every configuration
- Accurate financial or legal conclusions
- Replacement of qualified specialists in high-risk decisions
- Continued safety after upstream updates

The correct promise is narrower and real: **reduce mistakes, provide
repeatable professional workflows, surface risks early, and identify when
specialist review is required.**

## License

Registry content (this repository's own text) is licensed under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). The resources
it describes retain their own licenses, recorded per entry as SPDX
identifiers.
