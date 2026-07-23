---
name: OpenTofu
category: operations
subcategory: infrastructure-as-code
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/opentofu/opentofu
website: https://opentofu.org
pinned_version: v1.12.5 (commit 230349e959a44fb8eb7b83754f9d9b012f3bdb42)
license: MPL-2.0
score: 86
confidence: high
tested: true
last_verified: 2026-07-23
---

# OpenTofu — infrastructure as code (Terraform-compatible)

## What it does
Declarative infrastructure provisioning using HCL, drop-in compatible with
the Terraform language and provider ecosystem. Linux Foundation project
created after HashiCorp relicensed Terraform to the non-open-source BUSL
(see `rejected/README.md` → Terraform).

## When to use
- Any founder infrastructure that should be reproducible and reviewable:
  cloud resources, DNS, object storage, monitoring config
- Where an open-source-licensed IaC toolchain is a requirement (BUSL
  Terraform restricts competitive/embedded use)

## When not to use
- Trivial single-VPS setups may not repay the state-management overhead
- Not a configuration-management tool for inside the OS (that's Ansible
  territory; Phase 2)

## Evidence
- License MPL-2.0 `[V]` — repository license file (2026-07-23)
- Latest release v1.12.5, 2026-07-21, commit 230349e `[V]` — Go module
  proxy metadata
- Institutional stewardship: Linux Foundation project with a public
  steering committee and multiple sponsoring companies `[C]` — opentofu.org
  and LF announcements
- Active release cadence (multiple minor/patch releases per year) `[V]` —
  release history

## Validation results (sandboxed test, 2026-07-23, Phase 2)
- **`go install` is NOT a supported install path** — verified by attempt:
  upstream go.mod contains replace directives that `go install` rejects.
  Use official binaries/packages, or build from source.
- Built from source at v1.12.5 (module-proxy download, verifiable hash;
  `go build ./cmd/tofu`) — reproducible
- Ran a full local lifecycle on a providerless config:
  `init` → `plan` → `apply` → `output` all exit 0, computed output
  correct (`answer = 42`). Cloud-provider provisioning not tested
  (isolated environment holds no credentials by design).

## Security findings
- State files can contain secrets in plaintext — encrypt state (OpenTofu
  has native state encryption) and never commit state to git `[C]` — docs
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- MPL-2.0: commercial use, SaaS, redistribution permitted; file-level
  copyleft only (modified MPL files must remain MPL). No network copyleft.

## Installation
Official release binaries/packages (get.opentofu.org) pinned to v1.12.5,
or source build (`go build ./cmd/tofu`). `go install` does not work —
see validation results.

## Agent integration
Agents may generate and `tofu plan` changes; **`tofu apply` must be
human-approved** — infrastructure mutation is not reversible in general.

## Required human review
Every `apply`; provider credential handling; state storage location.

## Score notes
Functional 18/20 · Security 16/20 · Maintenance 13/15 (younger fork, but LF
governance) · Docs 9/10 · License 10/10 · Reproducibility 7/10 · Provenance
9/10 · Integration 4/5 → **86**
