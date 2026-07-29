# Bundle: Security Baseline

## Outcome

Establish a small, evidence-backed security and software-supply-chain baseline that detects exposed secrets, vulnerable dependencies, unsafe source patterns, artifact tampering, and deploy-time web risks without pretending that scanner output proves security.

## Required capabilities

Secret detection, dependency and container vulnerability scanning, SBOM generation, source analysis, release provenance verification, repository-security health signals, authorized dynamic testing, triage, suppression governance, and recurring re-verification.

## Selection rules

1. Start with repository type, deployment model, languages, package managers, container use, and release process.
2. Prefer validated registry records over catalog-only candidates.
3. Select the smallest compatible set; overlapping tools need an explicit reason.
4. Use Gitleaks as the default repository secret scanner.
5. Add TruffleHog only when verified-secret investigation is justified; keep provider verification disabled unless explicitly authorized and account for AGPL-3.0 obligations.
6. Use OSV-Scanner for lockfile and ecosystem dependency evidence.
7. Use Trivy for broad filesystem, container, IaC, secret, and misconfiguration coverage.
8. Use Syft plus Grype when an explicit SBOM-centered workflow, artifact inventory, or downstream attestation is required.
9. Use Semgrep CE for source-pattern analysis; do not treat rules as proof of exploitability or complete coverage.
10. Use Cosign when the project publishes or consumes signed images or attestations.
11. Use OWASP ZAP only against systems the operator owns or is explicitly authorized to test.
12. Use OpenSSF Scorecard as a repository-health signal, never as a security verdict.
13. Findings must preserve evidence, confidence, affected component, remediation owner, due date, suppression rationale, and review status.

## Recommended resources

### Default for every maintained repository

- `registry/security/gitleaks.md` — read-only secret detection in pre-commit and CI.
- `registry/security/osv-scanner.md` — dependency and lockfile vulnerability evidence.
- `registry/security/openssf-scorecard.md` — upstream repository-health heuristics.

### Applications, containers, and infrastructure

- `registry/security/trivy.md` — broad vulnerability, container, filesystem, IaC, secret, and misconfiguration scanning.
- `registry/security/syft.md` — explicit SBOM creation.
- `registry/security/grype.md` — SBOM and artifact vulnerability analysis.

### Source-code review

- `registry/security/semgrep.md` — custom and maintained static-analysis rules.

### Release integrity

- `registry/security/cosign.md` — signature and attestation verification.

### Restricted or situational tools

- `registry/security/trufflehog.md` — high-confidence secret investigation; network verification and licensing require review.
- `registry/security/owasp-zap.md` — authorized DAST in an isolated test environment.

## Implementation order

1. Inventory repositories, languages, lockfiles, images, IaC, deployment targets, and release artifacts.
2. Add Gitleaks and OSV-Scanner with pinned versions and machine-readable reports.
3. Add Trivy for applications, containers, and IaC.
4. Add Syft and Grype only where the SBOM is consumed, retained, compared, signed, or supplied downstream.
5. Add Semgrep rules for the project’s languages and material risk classes.
6. Add Cosign verification to artifact publication and consumption boundaries.
7. Add Scorecard monitoring for critical upstream dependencies.
8. Add ZAP only after a safe target, authorization, scan policy, rate limit, and rollback plan exist.
9. Add TruffleHog verification only after explicit authorization and credential-provider impact review.
10. Establish triage SLAs, suppression expiry, ownership, metrics, and recurring re-verification.

## Verification

- Confirm every tool reports the exact approved pin.
- Run harmless seeded fixtures proving expected detections and known non-detections.
- Preserve JSON, SARIF, SBOM, version, checksum, and signature evidence as CI artifacts.
- Confirm scanners do not upload proprietary source or secrets by default.
- Confirm network-dependent databases and provider checks are documented and controlled.
- Verify exit codes block only the intended severity and confidence thresholds.
- Test false-positive suppression, expiry, ownership, and audit history.
- Verify ZAP targets only an authorized preview or isolated environment.
- Verify Cosign against the exact digest, identity, issuer, and policy expected by the project.
- Re-run after dependency, image, rule, database, or tool-version changes.

## Human review

A competent security reviewer must approve severity thresholds, suppressions, credential rotation, provider verification, active scanning, signing identities, trust policies, production exceptions, and claims made from scanner output. No clean result may be described as proof that a system is secure, compliant, vulnerability-free, or safe to launch.
