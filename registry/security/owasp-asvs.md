---
name: OWASP Application Security Verification Standard (ASVS)
category: security
subcategory: security-standard
status: approved
tier: B
human_reviewed: false
type: standard
canonical_repo: https://github.com/OWASP/ASVS
website: https://owasp.org/www-project-application-security-verification-standard/
pinned_version: v5.0.0 (May 2025)
license: CC-BY-SA-4.0
score: null
confidence: high
tested: not-applicable
last_verified: 2026-07-23
---

# OWASP ASVS — application security requirements standard

## What it does
A structured catalog of verifiable security requirements for web
applications and services, organized in three assurance levels. The de
facto open standard for "what does a secure application actually require."

## When to use
- Deriving a founder's security requirements checklist (Level 1 first) for
  design, code review, and pre-launch verification
- Answering enterprise security questionnaires with a recognized framework
- Grounding an AI code-review agent with concrete, citable requirements

## When not to use
- As proof of compliance: self-assessment against ASVS is not certification
  and must never be presented as such
- Mobile-specific requirements (use OWASP MASVS, to be validated in
  Phase 2)

## Evidence
- License CC-BY-SA-4.0 `[V]` — repository license (2026-07-23)
- Current stable v5.0.0, released May 2025 at Global AppSec EU `[V]` — repo
  and release notes; v5.0.1 patch in progress `[V]`
- Professional provenance: OWASP flagship-class project, named project
  leads (Cuthbert, Grossman, Lang) and an active working group `[V]` — repo
- Distributed as PDF/Word/CSV per version `[V]`

## Validation results
- Standard document, not executable — `tested: not-applicable`. Verified the
  v5.0.0 artifacts exist and the repo is actively maintained.

## Security findings
Not applicable (document).

## Legal / licensing findings
- CC-BY-SA-4.0: commercial use and adaptation permitted with attribution;
  **ShareAlike**: derivative checklists/documents you distribute must be
  licensed CC-BY-SA-4.0 as well. Internal use carries no disclosure
  obligation. OWASP trademarks may not imply endorsement.

## Installation
Download versioned artifacts from the GitHub release; commit the CSV into
your compliance repo for traceability.

## Agent integration
Load the CSV form as grounding for security-review agents; require the
agent to cite requirement IDs (e.g. "V2.1.1") in findings so humans can
verify against the standard text.

## Required human review
Level selection, requirement applicability decisions, and any external
claims of conformance.

## Score notes
Not scored: execution dimensions (security posture, reproducibility,
integration) don't apply to a standards document. Provenance and
maintenance are strong per evidence above.
