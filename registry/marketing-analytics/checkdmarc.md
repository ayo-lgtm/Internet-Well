---
name: checkdmarc
category: marketing-analytics
subcategory: email-deliverability
status: approved
type: tool
canonical_repo: https://github.com/domainaware/checkdmarc
website: https://domainaware.github.io/checkdmarc/
pinned_version: 5.17.3 (PyPI, published 2026-06-23)
license: Apache-2.0
score: 79
confidence: high
tested: true
last_verified: 2026-07-23
---

# checkdmarc — SPF/DMARC (and related DNS) validation

## What it does
Validates a domain's email-authentication posture: parses and checks
SPF records (including the 10-DNS-lookup limit), DMARC records/policies,
MX, and related DNS, with JSON output. The technical half of email
deliverability (the other half is sender reputation).

## When to use
- Before any listmonk/transactional-email launch: verify your domain's
  SPF, DKIM alignment prerequisites, and DMARC policy are actually valid
- Scheduled CI check so DNS drift doesn't silently break deliverability

## When not to use
- As a deliverability guarantee: valid auth is necessary, not sufficient
  — content, volume ramp, and list hygiene drive inbox placement `[I]`
- DKIM key testing is limited (DKIM is verified per-selector; know your
  selectors)

## Evidence
- License Apache-2.0 `[V]` — PyPI metadata 5.17.3 (2026-07-23)
- Published 2026-06-23; steady maintenance `[V]` — PyPI history
- Maintainer: domainaware (author of parsedmarc, the companion DMARC
  aggregate-report analyzer — Phase 4 validation candidate) `[C]`

## Validation results (sandboxed test, 2026-07-23)
- `pip install checkdmarc==5.17.3` — reproducible
- Ran against a real domain (gitlab.com) with live DNS: exit 0, JSON
  output parsed; DMARC reported valid with policy `reject`; SPF reported
  invalid (plausibly the common >10-lookup issue — we did not
  independently adjudicate the target's SPF). Demonstrates real
  record-retrieval, parsing, and policy evaluation.

## Security findings
- Makes DNS queries only; no data leaves beyond DNS lookups `[V]` —
  observed behavior

## Legal / licensing findings
- Apache-2.0 — commercial use permitted.

## Installation
`pip install checkdmarc==5.17.3`

## Agent integration
JSON output; an agent can run it on your sending domains weekly and
open an issue on any validity change. DNS fixes are human-applied.

## Required human review
Any DNS record change; DMARC policy escalation (none→quarantine→reject)
is a deliberate, staged human decision.

## Score notes
Functional 16/20 · Security 17/20 · Maintenance 12/15 · Docs 8/10 ·
License 10/10 · Reproducibility 9/10 · Provenance 5/10 · Integration 4/5
→ **79** (repo test coverage not assessed `[U]`)
