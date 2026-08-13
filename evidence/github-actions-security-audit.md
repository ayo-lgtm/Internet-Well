# GitHub Actions Workflow Security Audit

**Scope:** All 11 YAML workflow files in `.github/workflows/`
**Date:** 2026-08-10
**Auditor:** Automated security review

---

## Known findings (not repeated here)

1. `verify-anchor-tranche-02.yml` downloads 7 external binaries without SHA256 checksum verification.
2. `verify-registry.yml` runs dynamic test discovery without explicit permissions boundary.
3. All 11 workflows pin GitHub Actions to mutable version tags instead of immutable commit SHAs.

---

## NEW Finding 1: Missing `permissions` block in 3 workflows

**Severity:** Medium
**Category:** Excessive GITHUB_TOKEN permissions (GITHUB_TOKEN with excessive permissions)

### Affected files

| File | Triggers | Line |
|------|----------|------|
| `verification-coverage.yml` | `pull_request`, `push`, `workflow_dispatch` | (no `permissions:` block) |
| `verify-anchor-tranche-01.yml` | `pull_request`, `workflow_dispatch` | (no `permissions:` block) |
| `verify-anchor-tranche-02.yml` | `pull_request`, `workflow_dispatch` | (no `permissions:` block) |

### Explanation

Seven of eleven workflows correctly declare `permissions: contents: read`. The three listed above omit the block entirely and therefore inherit the repository or organization default, which may include write access to `contents`, `issues`, `pull-requests`, `packages`, and other scopes.

### Exploitability

- On `pull_request` from external forks: GitHub restricts the token to read-only regardless, so the risk on that trigger path is minimal.
- On `push` (affects `verification-coverage.yml`): the token carries whatever default write scopes the repository or org grants. A compromised dependency or script could use the token to push code, create releases, or modify issues.
- On `workflow_dispatch`: requires repo write access to invoke, so the actor is already trusted—but the GITHUB_TOKEN given to the job may carry more scopes than the job needs, violating least-privilege.

### Specific concern for `verify-anchor-tranche-02.yml`

This workflow downloads and executes 7 external binaries **and** pulls 2 Docker images, all without integrity verification. Combined with the missing `permissions` block, a supply-chain compromise of any of those 9 external artifacts could grant the attacker a GITHUB_TOKEN with default (potentially write) permissions.

### Recommendation

Add an explicit top-level `permissions:` block to each workflow:

```yaml
permissions:
  contents: read
```

---

## NEW Finding 2: Docker images pulled with mutable tags, not pinned to digest

**Severity:** Medium
**Category:** Supply-chain integrity / Unpinned external dependencies

### Affected file

`verify-anchor-tranche-02.yml`, lines 68–69:

```yaml
docker run --rm ghcr.io/zaproxy/zaproxy:2.17.0 zap.sh -version
docker run --rm ghcr.io/ossf/scorecard:v5.5.0 version
```

### Explanation

These two container images are referenced by mutable version tags (`:2.17.0`, `:v5.5.0`). Container registry tags can be re-pushed at any time—a compromised registry account, a supply-chain attack on the upstream project, or a GHCR misconfiguration could substitute a malicious image under the same tag.

This is distinct from the already-known finding about the 7 downloaded binaries. The binaries are curl'd from GitHub Releases; the Docker images are pulled from GHCR—a different artifact type and a different trust boundary.

### Exploitability

- **Realistic:** Tag re-pushing on GHCR requires write access to the upstream repository's package. For ZAProxy and OSSF Scorecard, these are well-maintained projects, so the probability is low but non-zero. Past incidents (e.g., `codecov/codecov-action` compromise) demonstrate this attack class is practical.
- **Impact:** Arbitrary code execution inside the CI runner with access to the GITHUB_TOKEN (and without explicit `permissions` restrictions per Finding 1).

### Recommendation

Pin to immutable image digests:

```yaml
docker run --rm ghcr.io/zaproxy/zaproxy@sha256:<digest> zap.sh -version
docker run --rm ghcr.io/ossf/scorecard@sha256:<digest> version
```

---

## NEW Finding 3: `release.yml` workflow_dispatch skips version-alignment verification

**Severity:** Medium
**Category:** Build integrity bypass

### Affected file

`release.yml`, lines 20–26:

```yaml
- name: Verify tag and version alignment
  if: startsWith(github.ref, 'refs/tags/')
  run: |
    TAG="${GITHUB_REF_NAME#v}"
    test "$TAG" = "$(cat VERSION)"
    grep -q "version = \"$TAG\"" pyproject.toml
    grep -q "VERSION = \"$TAG\"" internet_well.py
```

### Explanation

The version-alignment check only runs when the trigger is a tag push (`refs/tags/v*`). When the workflow is invoked via `workflow_dispatch` (line 7), `github.ref` is `refs/heads/<branch>`, so `startsWith(github.ref, 'refs/tags/')` evaluates to `false` and the entire step is skipped. The remaining steps—build, smoke test, and artifact upload—still execute.

This means a `workflow_dispatch` invocation from any branch produces release artifacts (wheel, sdist) with the artifact name `internet-well-release-<branch>` and uploads them, but **without verifying that VERSION, pyproject.toml, and internet_well.py agree on the version number**.

### Exploitability

- **Prerequisite:** Requires repository write access to trigger `workflow_dispatch`.
- **Impact:** An actor with write access can build and upload release artifacts from any branch, including branches with inconsistent or experimental version strings. If downstream processes consume these artifacts by name pattern, they could pick up unvalidated builds.
- **Mitigation already in place:** The artifact name includes the ref name (e.g., `internet-well-release-main`), which distinguishes it from tag-based artifacts. However, there is no programmatic guard preventing confusion.

### Recommendation

Either remove `workflow_dispatch` from the release workflow, or make the version-alignment step unconditional (and fail gracefully when not on a tag):

```yaml
- name: Verify tag and version alignment
  run: |
    if [[ "$GITHUB_REF" == refs/tags/* ]]; then
      TAG="${GITHUB_REF_NAME#v}"
      test "$TAG" = "$(cat VERSION)"
      grep -q "version = \"$TAG\"" pyproject.toml
      grep -q "VERSION = \"$TAG\"" internet_well.py
    else
      echo "::warning::Skipping tag alignment (not a tag push). Artifact is non-release."
    fi
```

---

## NEW Finding 4: Shell trace mode (`set -x`) exposes future secrets

**Severity:** Low (latent risk)
**Category:** Secret exposure in logs

### Affected file

`verify-anchor-tranche-02.yml`, line 37:

```yaml
set -euxo pipefail
```

### Explanation

The `-x` flag enables shell trace mode, which prints every executed command to stderr before execution. This output is captured in GitHub Actions logs. Currently, the step does not reference any secrets, so no actual exposure occurs today. However, if a secret or environment variable is added to this step in the future (e.g., an API key for a security scanner), `set -x` will print it in cleartext to the public workflow log.

GitHub Actions masks secrets in logs using the `::add-mask::` mechanism, but `set -x` trace output can sometimes bypass this masking, particularly for values derived from secrets (substrings, encoded forms, or values passed through variable expansion).

### Exploitability

- **Current:** No exploitability—no secrets are present in this step.
- **Future:** If secrets are added without removing `-x`, they will be logged in cleartext.

### Recommendation

Replace `set -euxo pipefail` with `set -euo pipefail` (drop the `x` flag). If trace output is needed for debugging, use it selectively around non-sensitive commands.

---

## NEW Finding 5: PyPI and npm packages installed without hash verification

**Severity:** Medium
**Category:** Supply-chain integrity

### Affected files and lines

| File | Lines | Packages |
|------|-------|----------|
| `verify-anchor-tranche-01.yml` | 22–28 | `markitdown==0.1.6`, `semantic-kernel==1.44.0`, `langgraph==1.2.9`, `pydantic-ai==1.104.0`, `litellm==1.92.0` |
| `verify-anchor-tranche-01.yml` | 51 | `@playwright/mcp@0.0.75` (npm) |
| `verify-anchor-tranche-02.yml` | 54–55 | `semgrep==1.162.0` |

### Explanation

Version-pinned packages are installed from PyPI and npm without `--require-hashes` (pip) or `--integrity` checks (npm). Version pinning alone does not guarantee integrity: a compromised package registry account or a registry-level breach can replace the package contents behind the same version number.

For the npm install on line 51 of `verify-anchor-tranche-01.yml`, the `--ignore-scripts` flag is a useful mitigation that prevents pre/post-install script execution. However, `require('...')` of the installed module at line 55 (`./node_modules/.bin/mcp-server-playwright --help`) still executes the package's JavaScript code.

### Exploitability

- **PyPI:** Past incidents include `ctx` and `phpass` package hijacking. Packages like `litellm` and `pydantic-ai` have broad dependency trees that increase exposure.
- **npm:** The `@playwright/mcp` package is scoped (harder to typosquat) and `--ignore-scripts` blocks install-time attacks, but the package code still runs when invoked on line 55.
- **Impact:** Arbitrary code execution in the CI runner. Combined with Finding 1 (missing `permissions` block in these workflows), the attacker gains access to a GITHUB_TOKEN with default scopes.

### Recommendation

Generate lockfiles with hashes and use `--require-hashes` for pip installs:

```bash
pip install --require-hashes -r requirements-tranche-01.txt
```

For npm, use a lockfile with `npm ci` instead of `npm install`.

---

## NEW Finding 6: Security tool errors silently suppressed with `|| true`

**Severity:** Low
**Category:** Detection bypass / Integrity monitoring

### Affected file

`verify-anchor-tranche-02.yml`, lines 78, 80, 82, 83:

```yaml
grype sbom:tranche-02/syft.spdx.json -o json > tranche-02/grype.json || true
osv-scanner scan source -r tranche-02/fixture --format json > tranche-02/osv.json || true
trivy fs --scanners secret --skip-db-update --format json tranche-02/fixture > tranche-02/trivy.json || true
trufflehog filesystem tranche-02/fixture --no-verification --json > tranche-02/trufflehog.json || true
```

### Explanation

The `|| true` suffix suppresses all non-zero exit codes from these security scanning tools. While this is intentional (the tools find intentional test fixtures and would otherwise fail the build), it also masks scenarios where:

- A downloaded binary is corrupted or replaced with a no-op.
- A tool crashes due to a compatibility issue.
- An attacker replaces a tool binary with one that silently exits 0 and produces empty output.

The subsequent validation step (`python automation/verify_anchor_tranche_02.py`) may or may not check that each JSON output file is non-empty and structurally valid. If it only checks file existence, a compromised or broken tool would go undetected.

### Exploitability

- This is a defense-in-depth concern rather than a directly exploitable vulnerability. It compounds Finding 1 (missing permissions) and the already-known binary download finding.

### Recommendation

Instead of `|| true`, capture exit codes and validate that each tool produced meaningful output:

```bash
grype sbom:tranche-02/syft.spdx.json -o json > tranche-02/grype.json; echo "grype_exit=$?" >> "$GITHUB_ENV"
```

Then in the validation step, check both the exit code and the output file size.

---

## NEW Finding 7: `verify-registry.yml` scheduled run inherits default token permissions

**Severity:** Low–Medium
**Category:** Excessive GITHUB_TOKEN permissions on scheduled trigger

### Affected file

`verify-registry.yml`, lines 44–45:

```yaml
schedule:
  - cron: "0 6 * * 1"
```

### Explanation

This is an extension of the already-known finding about `verify-registry.yml`. The `schedule` trigger always runs against the default branch with the repository's default GITHUB_TOKEN permissions. Unlike `pull_request` (where GitHub restricts the token for fork PRs), `schedule` grants the full default token.

Combined with the dynamic test discovery (`python3 -m unittest discover`, line 61), a compromised test file committed to the default branch would execute weekly with whatever default token scopes the repository grants—potentially including write access to contents, issues, and packages.

### Exploitability

- **Prerequisite:** Requires an attacker to get a malicious test file merged into the default branch (e.g., via a social-engineering PR review).
- **Impact:** Weekly execution of arbitrary code with default GITHUB_TOKEN permissions.
- **Existing mitigation:** PR review process presumably catches malicious test files.

### Recommendation

Add `permissions: contents: read` to the workflow. Additionally, consider explicitly listing test files rather than relying on `unittest discover`.

---

## Summary of new findings

| # | Severity | File(s) | Issue |
|---|----------|---------|-------|
| 1 | Medium | `verification-coverage.yml`, `verify-anchor-tranche-01.yml`, `verify-anchor-tranche-02.yml` | Missing `permissions` block—GITHUB_TOKEN inherits default (potentially write) scopes |
| 2 | Medium | `verify-anchor-tranche-02.yml` (lines 68–69) | Docker images pulled with mutable tags, not pinned to digest |
| 3 | Medium | `release.yml` (lines 20–26) | `workflow_dispatch` bypasses version-alignment verification |
| 4 | Low | `verify-anchor-tranche-02.yml` (line 37) | `set -x` trace mode—latent secret exposure if secrets are ever added |
| 5 | Medium | `verify-anchor-tranche-01.yml` (lines 22–28, 51), `verify-anchor-tranche-02.yml` (lines 54–55) | PyPI/npm packages installed without hash verification |
| 6 | Low | `verify-anchor-tranche-02.yml` (lines 78, 80, 82, 83) | `|| true` silently suppresses security tool failures |
| 7 | Low–Medium | `verify-registry.yml` (lines 44–45, 61) | Scheduled trigger with default permissions and dynamic test discovery |

## Items verified as NOT vulnerable

- **No template injection:** No workflow interpolates `${{ github.event.pull_request.title }}`, `${{ github.event.pull_request.body }}`, `${{ github.head_ref }}`, or any other attacker-controlled expression context into `run:` steps. The only `${{ }}` expression in a `with:` context is `${{ github.ref_name }}` in `release.yml` line 45 (artifact name), which is safe from shell injection.
- **No `pull_request_target`:** No workflow uses `pull_request_target`, eliminating the risk of privileged checkout of untrusted PR code.
- **No secrets referenced:** No workflow uses `${{ secrets.* }}` expressions, eliminating direct secret exposure through workflow code.
- **No artifact download/consumption:** No workflow downloads artifacts from other workflows, eliminating cross-workflow artifact poisoning.
- **No self-hosted runners:** All workflows use GitHub-hosted runners (`ubuntu-latest` or `ubuntu-24.04`).
- **No `workflow_dispatch` inputs:** No workflow defines input parameters for `workflow_dispatch`, eliminating input-injection risks.
- **No unsafe caching:** No workflow uses `actions/cache` with attacker-controllable keys.
