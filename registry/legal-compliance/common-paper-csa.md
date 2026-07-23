---
name: Common Paper Standard Agreements (CSA, DPA, SLA, NDA family)
category: legal-compliance
subcategory: legal-templates
status: approved
tier: B
human_reviewed: false
type: template
canonical_repo: https://github.com/CommonPaper/CSA (siblings: /DPA, /SLA)
website: https://commonpaper.com/standards/
pinned_version: CSA v2.1 (2024-11-05)
license: CC-BY-4.0
score: null
confidence: high
tested: not-applicable
last_verified: 2026-07-23
---

# Common Paper standard agreements — attorney-drafted open contract templates

## What it does
Standardized B2B SaaS legal agreements — Cloud Service Agreement (your
ToS for business customers), DPA, SLA, NDA and more — structured as a
short variable "Cover Page" + stable referenced Standard Terms, the way
the SAFE standardized fundraising docs.

## When to use
- First B2B customers asking for "your MSA": start from CSA v2.1 instead
  of a copy-pasted competitor ToS with someone else's obligations in it
- DPA when customers ask about GDPR data-processing terms
- Negotiation efficiency: counterparties' lawyers increasingly recognize
  the standard terms, reducing redline cycles `[M]`

## When not to use
- **Without counsel review for your specific product, risk profile, and
  jurisdiction — these are starting points, not legal advice.** This is
  a hard requirement of this registry entry, not boilerplate.
- Consumer-facing ToS/privacy policies (different regime: consumer
  protection law; separate counsel-reviewed docs)
- Non-US-law-centric deals without localization review

## Evidence
- License CC-BY-4.0 `[V]` — repository (2026-07-23); "free to use and
  modify… leave in the attribution" `[C]` — commonpaper.com/standards
- Professional provenance: CSA drafted by a committee of 40+ attorneys
  across vendors, procurement, boutique and large firms `[C]` — stated
  by Common Paper and reflected in the published committee list; this is
  a maintainer-claimed-but-plausible provenance — the committee roster
  itself was not independently contacted `[M]`
- Versioning discipline: versions are immutable once published; v2.1
  released 2024-11-05 `[V]` — repo releases

## Legal / licensing findings
- CC-BY-4.0: use, modify, and incorporate into your contracts with
  attribution preserved on the template. (Your executed contracts are
  your documents; attribution applies to reuse of the template text.)

## Installation
Vendor the version-pinned Markdown/PDF into a `legal/` repo; track your
Cover Page variables per customer.

## Agent integration
Agents can diff a counterparty's redlines against the standard terms
and summarize deviations for counsel — never accept/propose legal terms
autonomously.

## Required human review
A licensed attorney, for every agreement before first use and for any
negotiated deviation. Non-negotiable.

## Score notes
Not scored (legal template). Confidence high on license/versioning;
provenance partially maintainer-claimed as tagged.
