---
name: restic
category: operations-backups
subcategory: backup-restore
status: approved
type: tool
canonical_repo: https://github.com/restic/restic
website: https://restic.net
pinned_version: v0.19.1 (2026-07-05)
license: BSD-2-Clause
score: 87
confidence: high
tested: true
last_verified: 2026-07-23
---

# restic — encrypted, deduplicated backups

## What it does
Single-binary backup tool: encrypted (AES-256), deduplicated, snapshot-
based backups to local disks, SFTP, S3-compatible storage, and rclone
targets, with integrity checking (`restic check`) and point-in-time
restore.

## When to use
- The founder's default backup layer for databases dumps, config, and
  user-uploaded content — offsite to S3-compatible storage
- Scheduled via cron/systemd with `restic forget --prune` retention policy

## When not to use
- Database-consistent snapshots by itself — dump the DB first (pg_dump),
  then back up the dump; restic sees files, not transactions `[I]`
- Backup targets you never test restores on (an untested backup is a hope,
  not a backup — schedule restore drills)

## Evidence
- License BSD-2-Clause `[V]` — repository (2026-07-23)
- Latest v0.19.1, 2026-07-05; long release history (51+), GOVERNANCE.md
  present `[V]` — repo
- Multi-maintainer with community governance; sponsor-supported cloud
  test infrastructure `[M]` — repo docs

## Validation results (sandboxed test, 2026-07-23)
- Built from source at v0.19.1 via Go module proxy (verifiable provenance)
- Full roundtrip: `init` (encrypted repo) → `backup` → source deleted →
  `restore latest` → **restored file byte-identical (diff clean)** →
  `restic check` integrity pass. All exit 0, fully offline.

## Security findings
- Encryption is client-side; the repo password is a single point of
  failure — store it in a password manager AND a sealed offline copy;
  losing it loses every backup `[C]` — documented model
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- BSD-2-Clause: commercial use, SaaS, redistribution permitted.

## Installation
Distro packages, Homebrew, official binaries, or
`go install github.com/restic/restic/cmd/restic@v0.19.1`.

## Agent integration
Agents may run `backup`, `snapshots`, `check` autonomously on schedule;
`forget --prune` (data deletion) and restore-over-live-data require human
approval.

## Required human review
Retention policy, restore drills, password custody.

## Score notes
Functional 18/20 · Security 18/20 · Maintenance 13/15 · Docs 9/10 ·
License 10/10 · Reproducibility 10/10 · Provenance 6/10 · Integration 3/5
→ **87**
