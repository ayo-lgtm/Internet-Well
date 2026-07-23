---
name: Renovate
category: post-launch-maintenance
subcategory: dependency-updates
status: approved-with-restrictions
type: tool
canonical_repo: https://github.com/renovatebot/renovate
website: https://docs.renovatebot.com
pinned_version: 43.278.3 (npm, published 2026-07-22)
license: AGPL-3.0-only
score: 82
confidence: medium
tested: false
last_verified: 2026-07-23
---

# Renovate — automated dependency update PRs

## What it does
Scans your repos' manifests/lockfiles across dozens of ecosystems and
opens versioned, changelog-annotated update PRs on your schedule, with
grouping, automerge rules, and vulnerability-driven prioritization. The
core engine of post-launch dependency maintenance.

## When to use
- Every founder repo, from day one: unattended minor/patch update PRs
  keep the upgrade treadmill short; CVE-triggered updates arrive as PRs
  you can ship same-day
- Self-hosted CLI/container run on a schedule, or the hosted Mend app

## When not to use / restrictions
- **License history**: Renovate was MIT and was relicensed to
  AGPL-3.0-only (v41+, 2025) by Mend `[C]` — fine for using the tool
  (running it imposes nothing on your codebase), but forks/embedding
  inherit AGPL; the registry's license-drift watchlist applies
- The hosted "Mend Renovate" app is a commercial service wrapping the
  OSS engine — data-handling review applies if you grant it repo access
- Automerge without tests is how updates break prod: gate automerge on
  your CI being genuinely trustworthy `[I]`

## Evidence
- License AGPL-3.0-only `[V]` — npm metadata 43.278.3 (2026-07-23)
- Published 2026-07-22; extremely high release cadence (multiple/day)
  `[V]` — npm history
- Corporate maintainer: Mend (formerly WhiteSource) `[C]`
- Very wide adoption incl. major OSS orgs `[C]`

## Validation results
- Not execution-tested this pass: a meaningful run requires repo-host
  credentials (GitHub App/token), excluded from the isolated
  environment by design. Config-only dry runs are a follow-up.

## Security findings
- Requires write access to repos to open PRs — scope a fine-grained
  token/App to specific repos; treat its config (`renovate.json`) as
  security-sensitive (it can run postUpgradeTasks) `[C]` — docs

## Legal / licensing findings
- AGPL-3.0-only: using/running it is unrestricted for you; network
  copyleft matters only if you modify and offer it as a service.

## Installation
Self-hosted: `renovate/renovate:43.278.3` container on cron; or GitHub
Marketplace app (hosted by Mend — separate trust decision).

## Agent integration
Renovate is itself an agent; your review agent can triage its PRs
(read changelogs, check CI, flag majors). Automerge policy is human.

## Required human review
Token scoping; automerge rules; major-version updates.

## Score notes
Functional 19/20 · Security 15/20 (write-access surface) · Maintenance
15/15 · Docs 9/10 · License 7/10 (AGPL fine for use; relicense history
noted) · Reproducibility 5/10 (untested here) · Provenance 7/10 ·
Integration 5/5 → **82**
