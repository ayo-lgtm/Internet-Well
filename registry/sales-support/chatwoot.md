---
name: Chatwoot
category: sales-support
subcategory: customer-support
status: approved-with-restrictions
type: tool
canonical_repo: https://github.com/chatwoot/chatwoot
website: https://www.chatwoot.com
pinned_version: v4.16.0 (2026-07-18)
license: MIT (core); enterprise/ directory under proprietary enterprise license
score: 80
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Chatwoot — live chat and omni-channel support desk

## What it does
Self-hosted Intercom/Zendesk-class support: website live chat, shared
email inbox, WhatsApp/social channels, help-center articles, canned
responses, and automation rules.

## When to use
- Founder support inbox + website chat once email alone stops scaling,
  with customer conversations on infrastructure you control

## When not to use / restrictions
- **Open-core boundary**: files under `enterprise/` are NOT MIT — they are
  under a proprietary license `[V]` — LICENSE file quoted during
  verification. When self-hosting the community build, confirm which
  features load from `enterprise/` before relying on them.
- A solo founder with tiny volume may be better served by plain email +
  a shared label system until volume justifies running Rails + Postgres +
  Redis `[I]`

## Evidence
- Core license MIT with explicit enterprise/ carve-out `[V]` — LICENSE
  file (2026-07-23)
- Latest v4.16.0, 2026-07-18; active `[V]` — repo page
- Corporate maintainer: Chatwoot Inc. `[C]`
- Note: repo sidebar shows "MIT" without the carve-out — an example of why
  this registry reads LICENSE files, not badges `[V]`

## Validation results
- Not execution-tested this pass (Rails+Postgres+Redis stack; Phase 2).

## Security findings
- Holds customer PII and conversation history — same data-protection
  surface as a CRM; no unresolved material advisories located; `[U]`
  Scorecard

## Legal / licensing findings
- MIT core: commercial use, SaaS permitted. Enterprise-directory features
  require a commercial relationship for production use — verify per
  feature. Trademark "Chatwoot" is the company's.

## Installation
Official docker-compose pinned to v4.16.0.

## Agent integration
REST API + webhooks; agent-drafted replies should run in
suggest-then-approve mode, not autonomous send, until accuracy is proven
on your product.

## Required human review
License boundary on enterprise features; customer-data retention policy;
agent reply supervision.

## Score notes
Functional 18/20 · Security 14/20 · Maintenance 14/15 · Docs 8/10 ·
License 7/10 (open-core management) · Reproducibility 7/10 · Provenance
7/10 · Integration 5/5 → **80**
