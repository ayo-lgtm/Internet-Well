---
name: Mobile Next mobile-mcp
category: engineering
subcategory: ios-mcp-automation
status: experimental
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/mobile-next/mobile-mcp
website: https://github.com/mobile-next/mobile-mcp
pinned_version: 294f403f2fe94ae86fc086181ebc1c1ec5b5c990 (2026-10-25)
license: Apache-2.0
score: 60
confidence: medium
tested: false
last_verified: 2026-10-25
---

# Mobile Next mobile-mcp

## What it does
Agent-facing mobile interaction and verification for supported devices, including iOS [M]. Candidate for mobile Safari and native-app QA; no successful execution against a product is asserted.

## When to use
Evaluate iPhone user journeys on a dedicated test device or simulator with synthetic data. Inspect live state, interact, then retain independently reviewable evidence. See [iPhone testing adoption guide](../../docs/IPHONE-TESTING.md).

## When not to use
Do not use production/client accounts, privileged documents or personal device contents in an unreviewed agent/device environment. Do not treat accessibility snapshots as a complete VoiceOver audit, simulator success as physical-device proof, or a tool-returned success flag as an acceptance verdict.

## Evidence
- [Canonical repository](https://github.com/mobile-next/mobile-mcp) metadata confirms a public, non-archived project at inspection [V].
- [Immutable commit](https://github.com/mobile-next/mobile-mcp/commit/294f403f2fe94ae86fc086181ebc1c1ec5b5c990) and [README](https://github.com/mobile-next/mobile-mcp/blob/294f403f2fe94ae86fc086181ebc1c1ec5b5c990/README.md) inspected on 2026-10-25 [V].
- [License file](https://github.com/mobile-next/mobile-mcp/blob/294f403f2fe94ae86fc086181ebc1c1ec5b5c990/LICENSE) confirms Apache-2.0 [V]; [package metadata](https://github.com/mobile-next/mobile-mcp/blob/294f403f2fe94ae86fc086181ebc1c1ec5b5c990/package.json) was also inspected [V].
- Node.js 20+ in package metadata [V]. Upstream documents iOS simulators, physical iPhones, Android and optional hosted devices, with URL opening, UI interaction, screenshots, recordings and diagnostic tools [M]. Local iOS setup requires the Apple platform tooling and proper device preparation; cloud support is a separate service [M].
- README describes optional cloud reservation, notifications/agent integration and local device tooling [M].
- Maintainer capability and privacy descriptions are not independently reproduced runtime results.

## Validation results
Source metadata, exact pin, license, README and package manifest reviewed; no installation, device connection, upstream tests, signing, model request or runtime benchmark performed. Latest stable release, release cadence, maintainer concentration, dependency advisories, unresolved security issues, signing/provenance, SBOM, full license inventory and installation reproducibility remain unverified [U]. Confidence capped at medium; experimental tier C.

## Security findings
README explicitly documents usage telemetry through PostHog and Scarf and MOBILEMCP_DISABLE_TELEMETRY=1 as the disable control [V]. Set it before an approved trial and verify actual egress. Local hosting does not establish local model inference or a no-egress guarantee [I]. Cloud devices and agent/model services have separate privacy and retention terms [U].
Screenshots, logs, recordings, typed credentials, downloaded files and traces can expose sensitive data. Use test-only accounts, controlled artifact storage, serial device mutations, bounded runs and an exercised cancellation path. Review remote-service authentication before exposing device control. No security audit was performed.

## Legal/licensing findings
Apache-2.0 permits commercial use and modification subject to applicable license/notice preservation, changed-file notices and other conditions; it grants no trademark permission. Dependencies, device software and hosted services retain their own terms. Full dependency and service-term review is outstanding [U].

## Installation
Registry candidate only: no software, runner, global agent rules or MCP configuration is installed by this addition. Inspect the pinned build/install scripts and select a reviewed immutable package/source version before an isolated trial. Do not substitute latest for the recorded pin. Hardware, signing, cloud rental and model services may impose separate costs and requirements [I].

## Agent integration
Use the [adoption guide](../../docs/IPHONE-TESTING.md). No executable adapter or default bundle is enabled. First verify host/toolchain, target identifier, synthetic account, permitted actions, provider routing, finite time/cost limits and artifact controls. Compare with deterministic browser/app assertions. Recheck upstream changes before updating the pin. Roll back catalog inclusion by removing this record and rebuilding registry/INDEX.md.

## Required human review
Review installation/device access, signing, cloud or model-provider processing and any external communication before adoption. No record here authorizes purchases, messages, actual legal submissions or production-data use. Validate microphone, audio playback and VoiceOver on a physical device before asserting accessibility or voice-only acceptance.

## Score notes
Provisional score 60/100: functional quality 13/20; security posture 7/20; maintenance health 8/15; documentation/usability 8/10; license suitability 9/10; reproducibility/testing 3/10; professional provenance 8/10; integration readiness 4/5. No runtime evidence; score is a selection aid, not approval.
