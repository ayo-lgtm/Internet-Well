---
name: Google ARTEMIS
category: engineering
subcategory: android-agent-testing
status: experimental
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/google/artemis
website: https://github.com/google/artemis
pinned_version: 351ca8422f7b5b54e80a9c1ce03a222e02415b6b (2026-09-29)
license: Apache-2.0
score: 65
confidence: medium
tested: false
last_verified: 2026-10-23
---

# Google ARTEMIS

## What it does
Natural-language Android automation for real devices and emulators, exposed through CLI, web console, MCP and a Python client [M]. Flash uses a reactive loop; Pro adds planning, action checks, diagnostics and verification [M]. Candidate for exploratory mobile QA and bug reproduction, not a substitute for deterministic acceptance tests [I].

## When to use
Evaluate authorized Android app workflows on an isolated emulator or dedicated test device with synthetic accounts. Selected for Android UI execution and device diagnostics; browser-oriented Playwright remains appropriate for web acceptance tests rather than replacing this device layer [I].

## When not to use
- iOS device or simulator testing: iOS expansion remains an unchecked roadmap item in the README [V].
- Production accounts, purchases, messages, account changes or sensitive app data without separate authorization and bounded scope.
- A strict no-external-data environment without a verified provider and network configuration. Local hosting of the console does not establish local inference [I].
- Unbounded unattended tasks: README states Flash has no turn cap by default and Pro supports continuous monitoring [V].
- Do not equate model-generated completion reports or benchmark claims with verified acceptance results.

## Evidence
- Repository metadata identifies the public, non-archived project under the Google organization [V].
- [Immutable source pin](https://github.com/google/artemis/commit/351ca8422f7b5b54e80a9c1ce03a222e02415b6b) is dated 2026-09-29 [V].
- [LICENSE](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/LICENSE) contains Apache License 2.0 [V].
- [README](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/README.md) documents Android automation, host launchers for macOS/Linux/Windows, MCP, diagnostic traces, accessibility-helper installation and the iOS roadmap [V]. Feature behavior has not been execution-tested here [U].
- README claims 99%+ AndroidWorld completion and typical Flash/Pro step latencies [M]. Neither results nor generalization to a user's app were independently reproduced [U].
- [Environment template](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/.env.example) lists model-provider API credentials, optional Cloud Vision OCR, default Flash mode and automatic helper installation enabled [V].
- [Python metadata](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/pyproject.toml) requires Python 3.12+, includes ADB/UIAutomator2, model SDKs, LangChain/LangGraph and a PostHog dependency [V]. Dependency presence alone does not establish active telemetry; emitted events, payloads and opt-out behavior remain unverified [U].
- [MCP documentation](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/mcp_server/README.md) describes global client/rule installation, detached tasks, webhook notifications and custom command hooks [V].
- [Model configuration](https://github.com/google/artemis/blob/351ca8422f7b5b54e80a9c1ce03a222e02415b6b/artemis/config/llm.py) defines provider/model mappings and fallback chains [V]. Actual provider availability, prices and data processing terms require deployment-specific verification [U].

## Validation results
Reviewed repository metadata, commit identity, license, README, environment template, Python metadata, model configuration and MCP documentation on 2026-10-23. No upstream installers, dependencies, model calls, device connections or tests were executed. No benchmark, privacy guarantee or production readiness is asserted. Latest stable release, cadence, maintainer concentration, security advisories, unresolved security issues, release signing/provenance, SBOM and installation reproducibility remain unverified [U]. Runtime confidence is capped at medium.

## Security findings
ADB, accessibility services, app installation, screenshots, UI hierarchies, Logcat, recordings and trace storage create meaningful device-access and data-handling boundaries [I]. Review what goes to each model, fallback, OCR provider, notification endpoint and telemetry sink. Inspect global configuration writes before running start scripts or MCP installers. Treat screen content and logs as untrusted input; require independent assertions for consequential actions. Review authentication, network binding and authorization before exposing the web console or remote Python client. No security audit was performed.

## Legal/licensing findings
Application license is Apache-2.0 [V]. Commercial use and modification are permitted subject to the license's conditions, including applicable license/notice preservation and modified-file notices; no trademark permission is granted. Upstream identifies third-party mobile-use code with separate LICENSE/METADATA under third_party; the full dependency license inventory has not been audited [M/U]. Model APIs, device software and test data have separate terms. Google organization hosting does not establish an SLA or product-support commitment [I].

## Installation
Catalog addition only: no install, device connection, provider credential use or global agent-rule change is authorized by this entry. Before an authorized trial, inspect launchers and package/build configuration at the exact pin, review dependencies, and use a disposable environment. Upstream launchers can install host toolchains and offer global MCP/rule configuration [M]. Model API costs and rate limits are additional to the source license [I]. On shared/personal devices review ARTEMIS_HELPER_AUTO_INSTALL=false; changing that setting is a separate operation.

## Agent integration
Registry candidate only; no adapter or default bundle is enabled.
1. Define Android target, permitted actions, synthetic test data and observable success criteria.
2. Pin source, dependencies and provider configuration; inspect model fallback and notification paths.
3. Use a dedicated emulator/device and explicitly select its serial.
4. Set finite execution, time and cost limits; verify stop/cancellation before extended tasks.
5. Compare with a deterministic baseline; inspect screenshots, UI state and logs independently.
6. Test failure recovery, permission denial and hostile on-screen instructions with synthetic fixtures.
7. Verify network egress, trace retention and cleanup before any sensitive-data use.
8. Recheck upstream changes before changing the pin. Roll back catalog inclusion by removing this record and regenerating INDEX.md; application/helper removal requires a separate tested procedure.

## Required human review
Approve device access, package installation, provider processing, global rule changes and the intended action scope before adoption. Review privacy, license and runtime evidence before promotion from tier C. Benchmark claims alone do not justify promotion.

## Score notes
Provisional evidence score: functional quality 14/20; security posture 8/20; maintenance health 9/15; documentation/usability 8/10; license suitability 9/10; reproducibility/testing 4/10; professional provenance 9/10; integration readiness 4/5 = 65/100. Institutional source identity improves provenance; untested execution, incomplete dependency/telemetry review and device authority limit confidence.
