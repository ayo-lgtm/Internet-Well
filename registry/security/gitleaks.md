---
name: Gitleaks
category: security-engineering
subcategory: secrets-detection
status: approved
type: tool
canonical_repo: https://github.com/gitleaks/gitleaks
website: https://gitleaks.io
pinned_version: v8.30.1 (commit 8d1f98c7967eb1e79cb44ac6241a124e145d2165)
license: MIT
score: 84
confidence: high
tested: true
last_verified: 2026-07-23
---

# Gitleaks — secrets detection for git repositories

## What it does
Scans git history, working directories, and files for hardcoded secrets
(API keys, tokens, private keys) using a maintained ruleset of regex +
entropy detectors. Runs as a CLI, pre-commit hook, or GitHub Action.

## When to use
- Pre-commit and CI secret scanning for every repository a founder owns
- One-off audits of a repo's full history before open-sourcing it

## When not to use
- As the only secrets control — it cannot find secrets it has no pattern
  for, and cannot revoke anything it finds. Pair with provider-side secret
  scanning (GitHub push protection) and short-lived credentials.
- Scanning non-git binary artifacts (limited support).

## Evidence
- License MIT `[V]` — GitHub API `license.spdx_id: MIT` (2026-07-23)
- Actively maintained `[V]` — GitHub API `pushed_at: 2026-07-22`, not archived
- Latest release v8.30.1, 2026-02-21 `[V]` — Go module proxy
  `proxy.golang.org/github.com/zricethezav/gitleaks/v8/@latest` returned
  version, timestamp, and VCS hash (verifiable provenance)
- Widely adopted (28.2k stars, used via pre-commit/Actions ecosystems) `[C]`
  — stars recorded as context only, per methodology
- Maintainer concentration: project is led by a single primary maintainer
  (Zachary Rice) `[C]` — bus-factor risk noted

## Validation results (sandboxed test, 2026-07-23)
- `go install github.com/zricethezav/gitleaks/v8@v8.30.1` from the Go module
  proxy — reproducible, no install scripts executed
- Ran `gitleaks dir` against a sample directory containing a planted
  AWS-format key ID and a GitHub-PAT-shaped string: the AWS key was detected
  (rule `aws-access-token`, exit code 1, JSON report); the synthetic PAT
  string did not match the stricter `github-pat` pattern — a reminder that
  detection is pattern-bound, not exhaustive

## Security findings
- No unresolved material advisories found during verification `[U→partial]`:
  the OpenSSF Scorecard API was unreachable from the research environment;
  scheduled for recheck. No known-exploited CVEs surfaced in searches.
- Tool runs fully offline; no telemetry observed in the smoke test run `[V]`
  (no network egress required after install)

## Legal / licensing findings
- MIT: commercial use, modification, redistribution, SaaS use all permitted;
  attribution in copies of the software required. No copyleft.

## Installation
`go install github.com/zricethezav/gitleaks/v8@v8.30.1`, Homebrew, Docker
(`ghcr.io/gitleaks/gitleaks`), or pre-commit hook (`rev: v8.30.1`).

## Agent integration
Safe for autonomous use: read-only scanner, deterministic exit codes
(1 = leaks found), JSON report output (`--report-format json`). Pin the
version. Do not let an agent auto-"fix" findings by rewriting git history
without human approval.

## Required human review
Every finding — rotation/revocation of a leaked credential is a human
decision. History rewrites require explicit approval.

## Score notes
Functional 18/20 · Security 16/20 (no Scorecard data retrievable, single
primary maintainer) · Maintenance 13/15 · Docs 8/10 · License 10/10 ·
Reproducibility 9/10 · Provenance 6/10 (individual-led, not institutional) ·
Integration 4/5 → **84**
