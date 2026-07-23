---
name: dbmate
category: launch-maintenance
subcategory: database-migrations
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/amacneil/dbmate
website: https://github.com/amacneil/dbmate
pinned_version: v2.34.1 (commit ddd00ff09d2034168072bc7870f815f9e6f1594d, 2026-07-09)
license: MIT
score: 83
confidence: high
tested: true
last_verified: 2026-07-23
---

# dbmate — framework-agnostic SQL schema migrations

## What it does
Single-binary migration runner: plain-SQL `migrate:up` / `migrate:down`
files, applied in order with a schema_migrations table, for PostgreSQL,
MySQL, SQLite, and others. Language-agnostic — works whatever your app
stack is.

## When to use
- Versioned, reviewable schema changes from the first table onward —
  the "migrations, not ad-hoc DDL" control this registry's PostgreSQL
  record requires
- Mixed stacks where the ORM's migrator would couple schema to one
  framework

## When not to use
- Teams already invested in ORM-native migrations (Django, Prisma,
  ActiveRecord) — one migration system per database, never two `[I]`
- Data (row) migrations at scale need care beyond schema files

## Evidence
- License MIT `[V]` — repository (2026-07-23)
- Latest v2.34.1, 2026-07-09, commit ddd00ff `[V]` — Go module proxy
  (verifiable provenance)
- Maintainer: Adrian Macneil + contributors; individual-led `[C]` —
  bus-factor noted; mitigated by tool simplicity and plain-SQL format
  (migrations remain runnable by hand or by any successor tool) `[I]`

## Validation results (sandboxed test, 2026-07-23)
- Built from module proxy at v2.28.0, then re-verified at v2.34.1
- Full roundtrip on SQLite: `new` → authored up/down SQL → `up`
  (applied) → `status` ([X], Applied: 1) → live insert/count via
  sqlite3 → `rollback` (clean). All exit 0, fully offline.

## Security findings
- Migrations are arbitrary SQL executed with the DB credentials
  provided — same review bar as code; use a migration role, not
  superuser `[I]`

## Legal / licensing findings
- MIT — commercial use permitted.

## Installation
`go install github.com/amacneil/dbmate/v2@v2.34.1`, Homebrew, or
official binaries; `DATABASE_URL` drives targeting.

## Agent integration
Agents draft migration SQL in PRs; applying to production is
human-triggered; `dbmate status` is safe for agents to check.

## Required human review
Every production `up`/`rollback`; destructive migrations (drops,
type changes) need a backup-first checklist.

## Score notes
Functional 17/20 · Security 16/20 · Maintenance 13/15 · Docs 8/10 ·
License 10/10 · Reproducibility 10/10 · Provenance 5/10 · Integration
4/5 → **83**
