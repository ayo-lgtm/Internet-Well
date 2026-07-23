---
name: OWASP MASVS (Mobile Application Security Verification Standard)
category: mobile-engineering
subcategory: security-standard
status: approved
type: standard
canonical_repo: https://github.com/OWASP/masvs
website: https://mas.owasp.org
pinned_version: v2.1.0 (2024-01-18)
license: CC-BY-SA-4.0
score: null
confidence: high
tested: not-applicable
last_verified: 2026-07-23
---

# OWASP MASVS — mobile app security requirements standard

## What it does
The mobile counterpart to ASVS: baseline security/privacy requirements for
iOS and Android apps (storage, crypto, auth, network, platform interaction,
code quality, resilience). Part of the OWASP MAS trio: MASVS (requirements)
→ MASWE (weaknesses) → MASTG (testing guide).

## When to use
- Security requirements checklist before building/launching a mobile app
- App-store review preparation: MASVS-STORAGE and MASVS-PRIVACY map well
  to Apple/Google data-safety declarations `[I]`
- With MASTG test cases when verifying your own app

## When not to use
- As certification: self-assessment is not conformance
- Web-only products (use ASVS — `registry/security/owasp-asvs.md`)

## Evidence
- License CC-BY-SA-4.0 `[V]` — repository (2026-07-23)
- Latest v2.1.0, 2024-01-18 `[V]` — releases; slow cadence normal for a
  standard; the MAS project remains active around it `[C]` — mas.owasp.org
- OWASP flagship project status `[C]` — OWASP project listings

## Validation results
- Standard document; artifacts (PDF/checklists) verified present.

## Legal / licensing findings
- CC-BY-SA-4.0: adaptation permitted with attribution; ShareAlike applies
  to distributed derivatives (internal checklists unaffected).

## Installation
Download versioned PDF/checklist; vendor the checklist CSV into your
mobile repo.

## Agent integration
Ground mobile code-review agents with MASVS control IDs (e.g.
MASVS-STORAGE-1) and require ID citations in findings.

## Required human review
Applicability decisions and any public conformance claims.

## Score notes
Not scored (standard).
