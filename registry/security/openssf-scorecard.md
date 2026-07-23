---
name: OpenSSF Scorecard
category: security
subcategory: supply-chain-security
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/ossf/scorecard
website: https://scorecard.dev
pinned_version: v5.5.0 (commit c395761df6afe1a69e476bc60a013a94bcbc153f)
license: Apache-2.0
score: 84
confidence: high
tested: false
last_verified: 2026-07-23
---

# OpenSSF Scorecard — automated supply-chain health checks for repos

## What it does
Runs ~19 automated checks (branch protection, dependency pinning, CI tests,
signed releases, dangerous workflows, vulnerability count, …) against a
repository and produces a 0–10 score per check. Usable as a CLI, GitHub
Action, and public API/badge.

## When to use
- Evaluating dependencies before adoption (this registry's own methodology
  uses it where reachable)
- Scoring and hardening the founder's own repos (the Action posts results
  to the code-scanning dashboard and a badge)

## When not to use
- As a complete security assessment: it measures process hygiene signals,
  not code security; a high score is necessary-ish, never sufficient
- Non-GitHub/GitLab repositories (limited support)

## Evidence
- License Apache-2.0 `[V]` — repository license indicator (2026-07-23)
- Latest release v5.5.0, 2026-04-23, commit c395761 `[V]` — Go module proxy
- Institutional provenance: Open Source Security Foundation (Linux
  Foundation) with CODEOWNERS-based multi-maintainer governance `[V]`
- Public API and weekly-scanned dataset of ~1M repos `[M]` — the API was
  not reachable from this research environment (network policy), so its
  availability is maintainer-claimed here

## Validation results
- Not execution-tested this pass: the CLI requires a GitHub token, and this
  research environment's GitHub access is scoped such that third-party-repo
  API calls are blocked. Phase 2: run against the founder's own repos.

## Security findings
- Requires a GitHub token (read scopes) — supply a fine-grained, least-
  privilege token; results for public repos are publishable `[I]`
- No unresolved material advisories located this pass.

## Legal / licensing findings
- Apache-2.0 — commercial use, modification, redistribution permitted.

## Installation
`go install github.com/ossf/scorecard/v5@v5.5.0`; official GitHub Action
`ossf/scorecard-action` (pin by SHA per its own guidance).

## Agent integration
An agent can run Scorecard on candidate dependencies and parse JSON output
(`--format json`) to feed adoption decisions; token provisioning is human.

## Required human review
Interpretation: score deltas and check failures need context before
acting (e.g. "no signed releases" is common and not always disqualifying).

## Score notes
Functional 16/20 · Security 17/20 · Maintenance 14/15 · Docs 8/10 ·
License 10/10 · Reproducibility 7/10 (untested here) · Provenance 9/10 ·
Integration 3/5 → **84**
