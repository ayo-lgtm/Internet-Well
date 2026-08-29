---
name: FingerprintJS
category: security
subcategory: browser-fingerprinting-abuse-prevention
status: approved-with-restrictions
tier: C
human_reviewed: false
type: production-dependency
canonical_repo: https://github.com/fingerprintjs/fingerprintjs
website: https://fingerprint.com/github/
pinned_version: v5.2.0
license: MIT
score: 78
confidence: high
tested: false
last_verified: 2026-08-29
---

# FingerprintJS — client-side browser fingerprinting

## What it does
FingerprintJS queries browser attributes and computes a hashed visitor identifier. Its documentation states that the identifier can persist across private/incognito mode and browser-data clearing. Version 5.x is MIT licensed; the latest GitHub release observed on 2026-08-29 is v5.2.0.

## When to use
- Abuse prevention and duplicate-signup friction where a device/browser signal is genuinely necessary.
- Risk scoring as one weak signal among several, never as sole proof of identity.
- Security research and controlled anti-fraud experiments with documented privacy review.

## When not to use
- Covert cross-context tracking, employee/user surveillance, or circumventing privacy choices.
- As a replacement for authentication, account recovery, KYC, or authoritative identity.
- As a sole blocking signal: the project documents lower accuracy than its commercial product and notes that client-side fingerprints are vulnerable to spoofing and reverse engineering.
- Where applicable consent, notice, retention, purpose-limitation, and regional privacy requirements have not been reviewed.

## Evidence
- Official repository metadata reports an active TypeScript project under the MIT license `[V]`.
- Official README describes client-side fingerprint generation and persistence across incognito/private mode and browser-data clearing `[V]`.
- Official README expressly warns that client-side fingerprints are vulnerable to spoofing/reverse engineering and less accurate than the commercial offering `[V]`.
- Official licensing documentation states that FingerprintJS v5.0.0+ is MIT licensed `[V]`.
- Official GitHub releases report v5.2.0 published 2026-04-07 `[V]`.

## Security findings
- The output is a probabilistic browser/device signal, not a cryptographic identity primitive.
- An attacker controlling browser signals can attempt evasion or spoofing; never use it as the only anti-abuse control.
- Loading from a third-party CDN creates an additional supply-chain/network dependency; prefer the pinned npm package when adopted.
- Treat the identifier as potentially sensitive/pseudonymous telemetry and protect it accordingly.

## Privacy / legal findings
Browser fingerprinting can be materially more privacy-sensitive than ordinary first-party analytics because it is designed to recognize a browser without relying on cookies or local storage. Adoption therefore requires a documented purpose, data-flow map, notice/consent analysis where applicable, retention limits, access controls, deletion handling, and jurisdiction-specific privacy review. Do not repurpose a fingerprint collected for fraud/security into marketing or behavioral profiling without a separate lawful-basis and product review.

## Internet Well adoption policy
**Restricted production dependency.** Internet Well may recommend FingerprintJS for narrowly scoped abuse/fraud controls only when the target product has a documented threat model and privacy review. Prefer server-side account/security signals first when they can achieve the objective with less tracking surface.

For AI-agent integrations, the agent may propose installation and implementation, but production activation must remain behind explicit human approval. Agents must not silently introduce browser fingerprinting as generic analytics.

## Required human review
Security/product/privacy review before production activation; legal/privacy review for tracking/consent/retention questions in the jurisdictions served by the product.

## Score notes
Functional 17/20 · Security 13/20 · Maintenance 14/15 · Documentation 9/10 · License 10/10 · Reproducibility 7/10 · Provenance 8/10 · Integration 4/5 → **82**, capped to **78** because browser fingerprinting creates material privacy/abuse risk and this pass did not execute-test the package.
