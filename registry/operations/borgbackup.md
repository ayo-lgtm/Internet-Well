---
name: BorgBackup
category: operations
subcategory: backup-restore
status: approved
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/borgbackup/borg
website: https://www.borgbackup.org
pinned_version: 1.4.5 (PyPI, latest stable 1.x)
license: BSD-3-Clause
score: 78
confidence: medium
tested: false
last_verified: 2026-07-23
---

# BorgBackup — deduplicated, compressed, encrypted backups

## What it does
Mature deduplicating backup with compression and authenticated encryption;
repository-based snapshots over SSH or local storage. Commonly paired with
Borgmatic for declarative config.

## When to use
- Linux-server backups to SSH-reachable storage, especially where Borg's
  append-only mode fits a ransomware-resistant design `[M]`

## When not to use
- Native S3/object-storage targets (restic covers this natively; Borg
  needs intermediaries) — see `registry/operations/restic.md`
- Windows-first environments (support is limited) `[C]` — docs

## Evidence
- License BSD-3-Clause `[V]` — PyPI metadata 1.4.5 (2026-07-23)
- Long history, active maintenance, multiple maintainers `[C]` — repo
- Widely packaged in distros `[C]`

## Validation results (attempted, 2026-07-23)
- **Execution test failed in this sandbox — recorded honestly:**
  (a) `pip install borgbackup` (1.4.1, 1.4.5) failed: source-only build
  requiring system dev headers absent here; (b) Ubuntu noble's
  `borgbackup` package was broken in this container (missing compiled
  `borg.crypto.low_level` — likely a sandbox/multiarch artifact, seen on
  one environment only, not evidence against the package generally).
- Consequence: installation is **less turnkey than restic** on minimal
  systems; on standard distros with standalone binaries (project publishes
  PyInstaller binaries on GitHub releases `[M]`) this is likely a
  non-issue. Retest queued in RECHECK.

## Security findings
- Same key-custody criticality as restic; no unresolved material
  advisories located; Scorecard `[U]`

## Legal / licensing findings
- BSD-3-Clause: commercial use, SaaS, redistribution permitted.

## Installation
Distro package or official standalone binary; verify with
`borg --version` + a test roundtrip before trusting.

## Agent integration
As restic: reads/backups autonomous, prunes and restores human-approved.

## Required human review
Same as restic; plus verify your install actually executes (see above).

## Score notes
Functional 17/20 · Security 17/20 · Maintenance 13/15 · Docs 9/10 ·
License 10/10 · Reproducibility 4/10 (observed install friction; binaries
unverified here) · Provenance 5/10 · Integration 3/5 → **78**
