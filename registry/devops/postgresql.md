---
name: PostgreSQL
category: engineering
subcategory: database
status: approved
type: tool
canonical_repo: https://git.postgresql.org/gitweb/?p=postgresql.git (GitHub mirror: postgres/postgres)
website: https://www.postgresql.org
pinned_version: 16.13 (tested; current majors 16–18 supported upstream)
license: PostgreSQL (OSI-approved, BSD-like)
score: 93
confidence: high
tested: true
last_verified: 2026-07-23
---

# PostgreSQL — the default relational database

## What it does
Full-featured ACID relational database: SQL standard coverage, JSONB,
full-text search, logical replication, row-level security, and a vast
extension ecosystem (PostGIS, pgvector). The boring-technology default
for a founder's primary datastore.

## When to use
- Default choice for the product database unless a specific workload
  proves otherwise; also serves queueing (SKIP LOCKED), search, and
  vector needs at solo scale before adding specialized infra `[I]`

## When not to use
- Embedded/edge single-file needs (SQLite); massive analytical scans
  (columnar warehouses); don't shard prematurely `[I]`

## Evidence
- License: PostgreSQL License, OSI-approved permissive `[V]` — project
  license page long-established
- Institutional provenance: PostgreSQL Global Development Group,
  independent multi-vendor community, ~30 years of history, annual major
  releases with 5-year support windows `[C]` — project documentation and
  release records
- Production adoption: default relational DB across the industry and of
  every major cloud's managed offering `[C]`

## Validation results (sandboxed test, 2026-07-23)
- Installed Ubuntu noble's postgresql 16.13, started a live cluster:
  `SELECT version()` OK; created a table, inserted rows, queried count —
  all successful (exit 0). Real server exercised, not a mock.

## Security findings
- Long CVE history handled by a mature security team with coordinated
  releases `[C]`; subscribe to pgsql-announce. Default local auth is
  peer/scram — never expose 5432 publicly without TLS + strict pg_hba
  `[C]` — official docs

## Legal / licensing findings
- PostgreSQL License: commercial use, modification, redistribution, SaaS
  — effectively no obligations beyond notice preservation.

## Installation
Distro packages, official apt/yum repos (pgdg) for current majors, or
managed cloud Postgres.

## Agent integration
Agents should get a least-privilege role (no superuser, no DDL in prod);
schema changes go through migrations (see dbmate record), never ad-hoc
agent DDL.

## Required human review
Schema migrations, backup/restore drills (pair with restic +
`pg_dump`), extension installs.

## Score notes
Functional 20/20 · Security 18/20 · Maintenance 15/15 · Docs 10/10 ·
License 10/10 · Reproducibility 9/10 · Provenance 10/10 · Integration
1/5 (it's a server you must operate — or pay a managed provider) → **93**
