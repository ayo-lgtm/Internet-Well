---
name: OWASP ZAP
category: security
subcategory: dast
status: approved-with-restrictions
tier: B
human_reviewed: false
type: tool
canonical_repo: https://github.com/zaproxy/zaproxy
website: https://www.zaproxy.org/
pinned_version: v2.17.0
license: Apache-2.0
score: 84
confidence: high
tested: true
last_verified: 2026-07-29
---

# OWASP ZAP — authorized dynamic application security testing

## What it does
Performs passive and active dynamic testing of web applications, including spidering, proxy analysis, and vulnerability checks.

## When to use
Use passive or baseline scans against owned or explicitly authorized preview and test environments. Use active scanning only with written scope, safe accounts, rate limits, and rollback plans.

## When not to use
Do not scan systems without authorization. Do not run active scans against production by default. Do not treat a clean scan as proof that the application is secure.

## Evidence
- Canonical OWASP project and Apache-2.0 license `[V]`.
- Exact evaluated release `v2.17.0` `[V]`.
- Tranche 02 verified the exact container version without launching an active scan `[V]`.

## Validation results
The dedicated Tranche 02 workflow completed successfully and retained exact-version evidence.

## Security findings
Active scanning can create accounts, submit forms, alter data, trigger rate limits, and disrupt services. Authentication scripts and test credentials require restricted handling.

## Legal / licensing findings
Apache-2.0 permits commercial use with notice preservation and includes a patent grant. Target authorization remains a separate legal and operational requirement.

## Installation
Use the official container pinned to `v2.17.0` and retain its image digest.

## Agent integration
Agents may run passive or baseline scans only against an approved target and policy. Active scanning, fuzzing, authentication scripting, and production targets require explicit authorization.

## Required human review
A competent security reviewer must approve target ownership, written scope, scan mode, rate limits, credentials, exclusions, production impact, remediation claims, and every active scan.

## Score notes
Functional 18/20 · Security 15/20 · Maintenance 14/15 · Documentation 9/10 · License 10/10 · Reproducibility 8/10 · Provenance 7/10 · Integration 3/5 → **84**.
