# Recheck Required

Open verification debts. Each item lists what could not be verified, why,
and how to close it. Items closed in Phase 2 (2026-07-23) are moved to the
log at the bottom.

## Environment-blocked (retry from a less restricted environment)

| Item | Affects | How to close |
|---|---|---|
| OpenSSF Scorecard results | All approved tool entries | `api.scorecard.dev` and deps.dev unreachable in Phases 1–2 (network policy). Fetch scores; update Security findings per record. |
| OSV/NVD CVE sweep | All approved entries | `api.osv.dev` unreachable. Partial substitute done via GitHub advisory pages for Grafana/Chatwoot/Uptime Kuma; complete the sweep per package. |
| Release signing / provenance | trivy, syft, grype, gitleaks, restic, others | Release-asset downloads blocked. Verify cosign/SLSA artifacts. |
| NIST AI RMF primary-source check | compliance/nist-ai-rmf.md | nist.gov blocked; identifiers AI 100-1 / AI 600-1 corroborated but not primary-verified. Confirm at nist.gov and lift confidence to high. |
| Fastlane execution test | mobile/fastlane.md | RubyGems unreachable; also needs store credentials for a real lane. Metadata-only validation so far. |

## Execution tests still deferred (Docker daemon unavailable in sandbox)

zaproxy, threat-dragon, prometheus, grafana, uptime-kuma, penpot,
plausible-ce, umami, listmonk, chatwoot, twenty, grype (needs vuln DB
download; blocked), trivy (source build failed on a sandbox toolchain
artifact and binaries were unfetchable — fully untested, see its record).

## New items opened in Phase 2

- **Chatwoot**: verify GHSA-x288-jh8j-348c (2026-07-16, cross-account
  resource transfer) is fixed in pinned v4.16.0 (released two days after
  the advisory) before recommending deployment.
- **BorgBackup**: install failed in sandbox (source build needs system dev
  headers; distro package broken in this specific container). Retest via
  official standalone binary; verify roundtrip like restic's.
- **promptfoo** (experimental): telemetry default + opt-out audit,
  open-core boundary audit, offline execution test — all required before
  any promotion to approved.
- **OWASP GenAI project URL drift**: LLM Top 10 canonical home is
  reorganizing under genai.owasp.org; re-verify canonical repo next pass.
- **hledger**: tested at distro 1.30.1; retest at pinned 1.52.1 when a
  binary source is reachable.
- **OpenTofu**: `go install` is NOT a supported install path (go.mod
  replace directives — verified by attempt). Record updated; official
  binary/package verification still owed.

## Fact-decay watchlist (verify on every touch)

- Open-core boundaries: Chatwoot `enterprise/`, Twenty `@license
  Enterprise` marker set — changes between releases.
- Semgrep rules-license terms; Opengrep fork maturity.
- Sentry SDK licenses (MIT claimed, unverified per-SDK).
- ZAP stewardship/telemetry defaults per release.
- Single-maintainer projects: gitleaks, pre-commit, uptime-kuma, listmonk,
  hledger — re-check activity each pass.
- Plausible privacy claims — verify tracker network behavior empirically.

## Closed in Phase 2 (2026-07-23)

- ✅ syft: SPDX-2.3 SBOM generated offline at v1.49.0 (source-built from
  module proxy)
- ✅ scancode-toolkit 32.5.0: MIT license + copyright detected on fixture
- ✅ hledger (distro 1.30.1): double-entry balances correct, check passes
- ✅ govuk-frontend 6.4.0: rendered in Chromium, axe-core scan zero
  violations
- ✅ restic v0.19.1: encrypted init→backup→restore→verify roundtrip,
  restored bytes identical
- ✅ Inspect AI 0.3.249: full offline eval pipeline via mockllm
- ✅ Advisory-page sweep: Grafana (28 GHSAs), Chatwoot (4), Uptime Kuma
  (10+) recorded in records
