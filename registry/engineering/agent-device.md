---
name: Callstack agent-device
category: engineering
subcategory: ios-agent-verification
status: experimental
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/callstack/agent-device
website: https://github.com/callstack/agent-device
pinned_version: 45125d717b207736dd47bc7969edbff7807a6e6d (2026-10-25)
license: MIT
score: 64
confidence: medium
tested: false
last_verified: 2026-10-25
---

# Callstack agent-device

## What it does
Agent-facing mobile interaction and verification for supported devices, including iOS [M]. Candidate for mobile Safari and native-app QA; no successful execution against a product is asserted.

## When to use
Evaluate iPhone user journeys on a dedicated test device or simulator with synthetic data. Inspect live state, interact, then retain independently reviewable evidence. See [iPhone testing adoption guide](../../docs/IPHONE-TESTING.md).

## When not to use
Do not use production/client accounts, privileged documents or personal device contents in an unreviewed agent/device environment. Do not treat accessibility snapshots as a complete VoiceOver audit, simulator success as physical-device proof, or a tool-returned success flag as an acceptance verdict.

## Evidence
- [Canonical repository](https://github.com/callstack/agent-device) metadata confirms a public, non-archived project at inspection [V].
- [Immutable commit](https://github.com/callstack/agent-device/commit/45125d717b207736dd47bc7969edbff7807a6e6d) and [README](https://github.com/callstack/agent-device/blob/45125d717b207736dd47bc7969edbff7807a6e6d/README.md) inspected on 2026-10-25 [V].
- [License file](https://github.com/callstack/agent-device/blob/45125d717b207736dd47bc7969edbff7807a6e6d/LICENSE) confirms MIT [V]; [package metadata](https://github.com/callstack/agent-device/blob/45125d717b207736dd47bc7969edbff7807a6e6d/package.json) was also inspected [V].
- Node.js 22.12+; Node.js 24+ for its web backend. Local iOS requires Xcode (simctl/devicectl); physical iPhones require pairing/trust, Developer Mode and a signed XCTest runner [V]. CLI, MCP and typed Node.js API share session, interaction and evidence surfaces [M].
- Pinned [installation](https://github.com/callstack/agent-device/blob/45125d717b207736dd47bc7969edbff7807a6e6d/website/docs/docs/installation.md), [limitations](https://github.com/callstack/agent-device/blob/45125d717b207736dd47bc7969edbff7807a6e6d/website/docs/docs/known-limitations.md) and [security guidance](https://github.com/callstack/agent-device/blob/45125d717b207736dd47bc7969edbff7807a6e6d/website/docs/docs/security-trust.md) were inspected [V].
- Maintainer capability and privacy descriptions are not independently reproduced runtime results.

## Validation results
Source metadata, exact pin, license, README and package manifest reviewed; no installation, device connection, upstream tests, signing, model request or runtime benchmark performed. Latest stable release, release cadence, maintainer concentration, dependency advisories, unresolved security issues, signing/provenance, SBOM, full license inventory and installation reproducibility remain unverified [U]. Confidence capped at medium; experimental tier C.

## Security findings
Upstream security guidance describes a local loopback daemon with per-start tokens, a separately authenticated Apple runner and sensitive artifact handling [M]. These controls have not been independently tested. Interactive CLI update checks contact npm; AGENT_DEVICE_NO_UPDATE_NOTIFIER=1 disables the update notice [V/M]. Model-provider processing depends on the connected agent; local device control does not guarantee local inference [I].
Screenshots, logs, recordings, typed credentials, downloaded files and traces can expose sensitive data. Use test-only accounts, controlled artifact storage, serial device mutations, bounded runs and an exercised cancellation path. Review remote-service authentication before exposing device control. No security audit was performed.

## Legal/licensing findings
MIT permits commercial use, modification and redistribution subject to preserving the copyright and permission notice. Dependencies, device software and hosted services retain their own terms. Full dependency and service-term review is outstanding [U].

## Installation
Registry candidate only: no software, runner, global agent rules or MCP configuration is installed by this addition. Inspect the pinned build/install scripts and select a reviewed immutable package/source version before an isolated trial. Do not substitute latest for the recorded pin. Hardware, signing, cloud rental and model services may impose separate costs and requirements [I].

## Agent integration
Use the [adoption guide](../../docs/IPHONE-TESTING.md). No executable adapter or default bundle is enabled. First verify host/toolchain, target identifier, synthetic account, permitted actions, provider routing, finite time/cost limits and artifact controls. Compare with deterministic browser/app assertions. Recheck upstream changes before updating the pin. Roll back catalog inclusion by removing this record and rebuilding registry/INDEX.md.

## Required human review
Review installation/device access, signing, cloud or model-provider processing and any external communication before adoption. No record here authorizes purchases, messages, actual legal submissions or production-data use. Validate microphone, audio playback and VoiceOver on a physical device before asserting accessibility or voice-only acceptance.

## Score notes
Provisional score 64/100: functional quality 14/20; security posture 9/20; maintenance health 8/15; documentation/usability 8/10; license suitability 9/10; reproducibility/testing 3/10; professional provenance 9/10; integration readiness 4/5. No runtime evidence; score is a selection aid, not approval.
