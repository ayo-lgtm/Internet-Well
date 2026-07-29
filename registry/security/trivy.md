---
name: Trivy
category: security
subcategory: dependency-scanning-sbom
status: approved
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/aquasecurity/trivy
website: https://trivy.dev
pinned_version: v0.70.0
license: Apache-2.0
score: 89
confidence: high
tested: true
last_verified: 2026-07-29
---

# Trivy — vulnerability, misconfiguration, secret, and SBOM scanner

## What it does

Scans container images, filesystems, git repositories, and infrastructure-as-code for known vulnerabilities, misconfigurations, exposed secrets, and license issues; it can also generate SPDX and CycloneDX SBOMs.

## When to use

- Broad default scanning for applications, containers, filesystems, and IaC.
- Pre-deploy image scanning and recurring re-scans of released artifacts.
- Teams that need one pinned scanner covering several baseline capabilities.

## When not to use

- As a DAST tool or substitute for source review, authorization testing, or business-logic testing.
- Where an air-gapped environment has no deliberate vulnerability-database mirroring strategy.
- As proof that a clean result means the product is secure or vulnerability-free.

## Evidence

- Apache-2.0 license and Aqua Security stewardship `[V]`.
- Exact evaluated release `v0.70.0` is immutable and signed, with checksums, SBOM, Sigstore metadata, and release attestation `[V]`.
- Tranche 02 installed the exact pin, captured version evidence, and exercised harmless scanning behavior in CI `[V]`.
- The dedicated Tranche 02 and main Internet-Well workflows completed successfully on 2026-07-29 `[V]`.

## Validation results

The Tranche 02 workflow downloaded the exact standalone pin, recorded the reported version, ran controlled fixture checks, validated generated evidence, and retained artifacts. Failure to install or a version mismatch would fail the workflow.

## Security findings

- Trivy may download vulnerability and policy databases; pin the scanner and define database update, caching, and offline behavior.
- Broad filesystem access can expose confidential source, configuration, and secrets to reports. Exclude sensitive paths deliberately and restrict artifact retention.
- Untrusted repositories must not control ignore files or scanner configuration without review.
- A vulnerability match requires version, platform, exploitability, fix state, and runtime-context analysis.

## Legal / licensing findings

Apache-2.0 permits commercial use, modification, redistribution, and SaaS use with preservation of notices and includes a patent grant. Republished vulnerability databases or third-party policy content may carry separate terms.

## Installation

Use the official binary or container pinned to `v0.70.0`; record checksum or image digest and the database-update policy in CI.

## Agent integration

Suitable for read-only automated scanning with JSON and SARIF output. Agents must preserve timeout, skipped-target, stale-database, unsupported-format, and partial-scan warnings and must not auto-create suppressions.

## Required human review

A developer or security reviewer must triage findings, approve severity thresholds and ignore rules, and determine remediation priority. Every suppression requires an owner, rationale, expiry, and review record.

## Score notes

Functional 19/20 · Security 17/20 · Maintenance 14/15 · Documentation 9/10 · License 10/10 · Reproducibility 9/10 · Provenance 7/10 · Integration 4/5 → **89**.
