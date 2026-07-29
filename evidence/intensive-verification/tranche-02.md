# Intensive Verification — Tranche 02

Verification date: 2026-07-29

This tranche evaluates the core security and software-supply-chain baseline. Catalog presence is not approval. Exact releases, licenses, release provenance, safe execution boundaries, and reproducible CLI behavior are required before registry promotion.

## Summary

| Candidate | Exact pin evaluated | Proposed disposition | Principal restriction |
|---|---|---|---|
| Trivy | `v0.70.0` | approved / Tier B after smoke test | findings require triage; remote databases and broad filesystem access must be controlled |
| Gitleaks | `v8.30.1` | approved / Tier B after smoke test | detections are not proof of active credentials; reports may themselves contain sensitive fragments |
| OSV-Scanner | `v2.3.8` | approved / Tier B after smoke test | ecosystem and lockfile coverage varies; reachable vulnerability does not equal exploitability |
| Syft | `v1.44.0` | approved / Tier B after smoke test | SBOM completeness depends on artifact visibility and cataloger support |
| Grype | `v0.112.0` | approved / Tier B after smoke test | vulnerability matches require version, distro, exploitability, and fix-state review |
| Cosign | `v3.0.6` | approved-with-restrictions / Tier B after smoke test | trust-root, identity, transparency-log, key, and bundle policy must be explicit |
| Semgrep CE | `v1.162.0` | approved-with-restrictions / Tier B after smoke test | CE and Pro capabilities must not be conflated; rules produce false positives and false negatives |
| TruffleHog | `v3.95.2` | approved-with-restrictions / Tier B after smoke test | AGPL-3.0 obligations and live-secret verification network calls require explicit approval |
| OWASP ZAP | `v2.17.0` | approved-with-restrictions / Tier B after container smoke test | active scanning is potentially disruptive and must target authorized non-production systems |
| OpenSSF Scorecard | `v5.5.0` | approved-with-restrictions / Tier B after smoke test | heuristic signals are not a security verdict; API and token scope affect results |

## Release evidence

- Trivy `v0.70.0` is an immutable, signed GitHub release with checksums, SBOM, Sigstore metadata, and release attestation.
- Gitleaks `v8.30.1` publishes checksums and versioned release assets.
- OSV-Scanner `v2.3.8` is a signed release and includes fixes for secure path handling and installation conflicts.
- Syft `v1.44.0` and Grype `v0.112.0` are immutable signed releases with checksums and signature material.
- Cosign `v3.0.6` is signed; v3 changes bundle and trust configuration semantics and therefore requires migration-aware verification.
- Semgrep `v1.162.0` is the evaluated release. Internet-Well must distinguish the open-source engine and rules from paid Pro features and hosted services.
- TruffleHog `v3.95.2` is a signed release. Its credential verification functionality can contact external providers.
- ZAP `v2.17.0` is the latest core release identified for this tranche.
- Scorecard `v5.5.0` is a signed release; official images moved to GitHub Container Registry starting with this version.

## Tool-specific findings

### Trivy

Use for vulnerability, secret, misconfiguration, image, filesystem, repository, and SBOM scanning where its supported analyzers match the target. Do not describe a clean Trivy result as proof of security. Cache its databases deliberately, pin the scanner and database-update policy, exclude confidential paths, and prevent untrusted repositories from controlling scanner configuration without review.

### Gitleaks

Use as the default fast secret-detection baseline for source and history. Scan results can expose portions of secrets, so artifacts, SARIF, logs, and PR annotations require restricted retention. Baselines and allowlists need code review because they can suppress real findings. Detection alone does not establish whether a credential is valid, revoked, synthetic, or exploitable.

### OSV-Scanner

Use for dependency vulnerability matching from supported manifests, lockfiles, SBOMs, containers, and package inventories. It is strongest when exact resolved versions are available. Treat transitive-resolution, call-analysis, and reachability features as evidence with documented limits, not as a guarantee that unmatched vulnerabilities are absent.

### Syft and Grype

Use Syft to produce a pinned SBOM and Grype to evaluate that SBOM or artifact. Keeping generation and vulnerability matching separate improves evidence traceability. Neither tool can identify components hidden from its catalogers or inaccessible inside encrypted, remote, runtime-generated, or proprietary systems. Preserve the SBOM format, scanner database timestamp, artifact digest, configuration, and suppressions.

### Cosign

Use for artifact-signature and attestation verification only with an explicit policy defining acceptable identities, issuers, roots, transparency-log behavior, timestamp requirements, offline bundles, and failure handling. A cryptographically valid signature proves only the configured statement and identity relationship; it does not prove the artifact is safe or appropriate.

### Semgrep CE

Use for source-pattern and data-flow checks supported by the open-source engine and selected rule packs. Internet-Well must record the exact ruleset revision separately from the Semgrep binary. Hosted registry rules, Pro interfile analysis, supply-chain features, and organizational policy capabilities may have separate terms and behavior. Findings require developer and security review.

### TruffleHog

Use when verified-secret detection materially adds value beyond Gitleaks. Network verification can transmit candidate credentials or metadata to third-party services and must not run automatically on sensitive repositories without approval. AGPL-3.0 network-copyleft obligations require license review for modified or network-served deployments.

### OWASP ZAP

Use passive and baseline scans first. Active scan, spidering, authentication scripts, and fuzzing require written authorization, scope controls, rate limits, safe test accounts, and non-production targets. DAST cannot prove absence of vulnerabilities and has limited visibility into authorization design, business logic, source-only weaknesses, and unexercised routes.

### OpenSSF Scorecard

Use individual checks and structured results as supply-chain evidence. Do not use aggregate score thresholds alone. The project explicitly describes its checks as opinionated heuristics with false positives and false negatives. Token permissions, repository visibility, forge support, API limits, and inaccessible settings affect results. Scorecard's Signed-Releases check detects signature-like assets but does not itself verify their cryptographic validity.

## Reproducibility gates

The tranche workflow must:

1. run exact-version CLI surfaces in isolated containers or package environments;
2. preserve `--version` and `--help` output;
3. run harmless fixture checks for secret detection, SBOM generation, vulnerability scanning, static analysis, and signature tooling without production credentials;
4. avoid active ZAP scanning, live TruffleHog verification, remote repository modification, or signing real artifacts;
5. retain dependency or image digests where available;
6. fail if a requested exact pin cannot be installed or reports a different version.

## Promotion policy

- No Tier A status is permitted without competent human review.
- TruffleHog, Semgrep CE, ZAP, Cosign, and Scorecard require restrictions even after successful installation.
- Scanner overlap must be purposeful: Gitleaks is the default secret baseline; TruffleHog is an optional verified-secret layer. Trivy provides broad baseline coverage; Syft plus Grype provide a more explicit SBOM-centered supply-chain path. OSV-Scanner is preferred for ecosystem-native dependency evidence.
- A scanner's failure, timeout, stale database, skipped target, unsupported format, or partial scan must never be reported as a clean result.
