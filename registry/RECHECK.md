# Recheck Required

Open verification debts. Each item lists what could not be verified in the
current pass, why, and how to close it.

## Environment-blocked (retry from a less restricted environment)

| Item | Affects | How to close |
|---|---|---|
| OpenSSF Scorecard results | All approved tool entries | `api.scorecard.dev/projects/github.com/<org>/<repo>` was unreachable (network policy). Fetch scores + per-check results; update each record's Security findings. |
| Release signing / provenance verification | trivy, syft, grype, gitleaks, others | Release-asset lists couldn't be fetched (asset API blocked; HTML asset lists failed to load). Verify cosign signatures / SLSA provenance on release artifacts. |
| Security policy (SECURITY.md) presence | All entries marked `[M]`/`[U]` for security policy | Blocked by GitHub API rate limits. Check `/community/profile` or SECURITY.md per repo. |
| CVE history sweep | All approved entries | NVD/OSV API access not attempted this pass (budget). Query OSV per package; record advisory counts + resolution latency. |

## Execution tests deferred to Phase 2 (`tested: false` entries)

trivy, zaproxy, syft, grype, threat-dragon (app), opentofu (plan-only),
prometheus, grafana, uptime-kuma, penpot, plausible-ce, umami, listmonk,
chatwoot, twenty, hledger, scancode-toolkit, govuk-frontend (render+axe).

## Fact-decay watchlist (verify on every touch)

- **Licenses of open-core projects**: Chatwoot enterprise/ scope, Twenty
  `@license Enterprise` file set — the marked file set changes between
  releases.
- **Semgrep**: rules-license terms and any further engine relicensing;
  Opengrep fork maturity (candidate for promotion from mention to record).
- **Sentry SDKs**: MIT status per-SDK (`[C]`, unverified individually).
- **ZAP**: Checkmarx stewardship terms; telemetry defaults per release.
- **Uptime Kuma / listmonk / pre-commit / gitleaks / hledger**:
  single-maintainer bus-factor — check activity on each re-verification.
- **pre-commit remote-hook mode**: untested offline; verify hook-repo
  cloning works as documented in a networked environment.

## Claims capped pending verification

- Umami "open-core dynamics milder" — `[C]` inference from public repo
  scope; verify cloud-vs-self-hosted feature matrix.
- listmonk production use at Zerodha — `[C]` from maintainer statements;
  no independent verification.
- Plausible privacy claims (no cookies / no personal data) — `[M]` vendor
  docs; verify tracker behavior empirically in Phase 2 (inspect requests).
