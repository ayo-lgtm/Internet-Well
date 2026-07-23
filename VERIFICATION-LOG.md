# Execution-Test Verification Log

Reproducible record of every sandboxed execution test behind a
`tested: true` flag. Environment for all tests: isolated Linux container
(Ubuntu noble base), no credentials present, outbound network limited to
package registries (npm, PyPI, crates.io, Go module proxy), Ubuntu apt
mirrors, and DNS. Dates: 2026-07-23. Full command transcripts lived in
the session scratchpad; the commands below reproduce each result.

| # | Tool @ version | Test | Result |
|---|---|---|---|
| 1 | gitleaks v8.30.1 | `go install …@v8.30.1`; `gitleaks dir` on dir with planted AWS key | Detected `aws-access-token`, exit 1, JSON report |
| 2 | semgrep 1.171.0 | pip install; local rule, `--metrics=off` on `shell=True` sample | 1 expected finding, offline; `--config auto` correctly requires network |
| 3 | pytest 9.1.1 | pip install; sample test run | 1 passed, exit 0 |
| 4 | ruff 0.15.22 | pip install; lint file with 2 unused imports | 2 findings, exit 1 |
| 5 | pre-commit 4.6.1 | pip install; `repo: local` hook running ruff in fresh git repo | Hook executed, failed on planted errors (exit 1) as expected |
| 6 | vitest 4.1.10 | npm install; sample test | 1 passed (initial failure was a researcher flag error, documented) |
| 7 | @playwright/test 1.61.1 | npm install; DOM test in real Chromium (explicit executablePath) | 1 passed |
| 8 | axe-core 4.12.1 | injected into Playwright page with missing alt | `image-alt` violation detected |
| 9 | syft v1.49.0 | `go install`; SBOM of npm project dir | Valid SPDX-2.3 JSON, exit 0 |
| 10 | OpenTofu v1.12.5 | source build from module proxy (go install unsupported — verified); providerless config | init/plan/apply/output all exit 0; output `answer = 42` |
| 11 | scancode-toolkit 32.5.0 | pip install; scan fixture with SPDX MIT header + copyright | Detected `mit` + exact copyright |
| 12 | hledger 1.30.1 (distro; pin 1.52.1 untested) | apt install; 2-txn journal | Balances arithmetically correct; `check` exit 0 |
| 13 | govuk-frontend 6.4.0 | npm install; render form+button with package CSS in Chromium; axe scan | Styled correctly; zero axe violations |
| 14 | restic v0.19.1 | `go install`; init→backup→delete→restore→check (encrypted repo) | Restored file byte-identical; all exit 0 |
| 15 | Inspect AI 0.3.249 | pip install; minimal Task; `inspect eval --model mockllm/model` | Exit 0; eval log artifact produced, fully offline |
| 16 | Lighthouse 13.4.1 | npm install; audit locally served page (headless Chromium) | Exit 0; scores perf 1.0 / a11y 1.0 / BP 0.96 / SEO 1.0 |
| 17 | checkdmarc 5.17.3 | pip install; live DNS validation of gitlab.com | Exit 0; DMARC valid `p=reject`; SPF flagged invalid (not adjudicated) |
| 18 | PostgreSQL 16.13 (distro) | apt install; live cluster; create/insert/select | All succeeded, exit 0 |
| 19 | FastAPI 0.139.2 (also 0.116.1) | pip install; endpoint via TestClient under pytest | 1 passed, offline |
| 20 | Scrapy 2.17.0 (also 2.13.3) | pip install; HtmlResponse CSS-selector extraction | Exact expected values asserted |
| 21 | dbmate v2.34.1 (also v2.28.0) | `go install`; SQLite migration new→up→status→insert→rollback | Full roundtrip clean, exit 0 |
| 22 | parsedmarc 10.2.4 | pip install; `--offline` parse of constructed RUA XML | Exit 0; alignment computed correctly |

Failed/blocked attempts, preserved for honesty:

- **trivy v0.72.0**: source build failed under Go 1.24.7 and go1.26.5
  (stdlib `encoding/json/v2` build-constraint conflict — sandbox
  artifact); binaries unfetchable. Untested.
- **BorgBackup 1.4.x**: pip source build requires system dev headers
  absent in sandbox; Ubuntu package broken in this container (missing
  compiled `borg.crypto.low_level`). Untested; retest via official
  standalone binary.
- **grype**: runtime vulnerability DB download blocked. Untested.
- **fastlane**: RubyGems unreachable; store credentials required for a
  meaningful lane. Untested.
- Server-class deployments (Grafana, Penpot, Chatwoot, Twenty,
  Plausible, Umami, listmonk, ZAP, Prometheus, Uptime Kuma, Metabase,
  EspoCRM, Documenso, Threat Dragon): Docker daemon unavailable.
