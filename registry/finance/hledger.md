---
name: hledger
category: finance-operations
subcategory: bookkeeping
status: approved
type: tool
canonical_repo: https://github.com/simonmichael/hledger
website: https://hledger.org
pinned_version: 1.52.1 (2026-04-28)
license: GPL-3.0-or-later
score: 80
confidence: medium
tested: true  # at Ubuntu distro version 1.30.1; pinned upstream 1.52.1 untested
last_verified: 2026-07-23
---

# hledger — plain-text double-entry accounting

## What it does
Double-entry accounting over human-readable plain-text journal files, with
CLI, TUI, and web interfaces: balance sheets, income statements, multi-
currency, budgeting. Your books live in git-versionable text you own.

## When to use
- Founder bookkeeping between "shoebox of receipts" and "hire an
  accountant": auditable, scriptable books with zero SaaS dependency
- Financial forecasting via scripted scenario journals

## When not to use
- **It does not file taxes, produce jurisdiction-specific statutory
  accounts, or replace an accountant** — export reports for a professional
- Invoicing/AR workflows with client portals (different tool class)
- Founders unwilling to learn double-entry basics (real learning curve)

## Evidence
- License GPL-3.0 `[V]` — repository (2026-07-23)
- Latest 1.52.1, 2026-04-28; quarterly-ish release rhythm since 2007 `[V]`
- Maintainer: Simon Michael (primary) + 185+ contributors `[V]` — repo;
  single-primary-maintainer concentration noted, mitigated by the
  ledger-file format being an open convention readable by other tools
  (ledger, beancount) `[I]`
- Strong regression-testing practice `[M]` — project documentation

## Validation results (sandboxed test, 2026-07-23, Phase 2)
- Tested at **Ubuntu noble's packaged 1.30.1** (upstream 1.52.1 binary was
  not fetchable in the research environment — version gap noted honestly)
- Wrote a two-transaction journal (opening balance + expense);
  `hledger balance` returned arithmetically correct double-entry balances
  (assets 960, equity −1000, expenses 40) and `hledger check` passed,
  both exit 0, fully offline
- Journal file format is stable across these versions `[C]` — docs

## Security findings
- Fully local; no network egress; books are files you must back up and
  encrypt at rest `[I]`

## Legal / licensing findings
- GPL-3.0: using the tool imposes nothing on your business data or other
  software; copyleft matters only if you redistribute modified hledger.

## Installation
Distro packages, Homebrew, or official install script (inspect first);
pin 1.52.1.

## Agent integration
Plain-text journals are ideal agent substrate: agents can draft entries
from bank CSVs for human review; `hledger check` validates. Never let an
agent auto-commit uncategorized transactions.

## Required human review
All categorization judgments, reconciliation, anything sent to tax
authorities or investors — professional review required.

## Score notes
Functional 16/20 · Security 17/20 · Maintenance 13/15 · Docs 9/10 ·
License 9/10 · Reproducibility 7/10 · Provenance 6/10 · Integration 3/5
→ **80**
