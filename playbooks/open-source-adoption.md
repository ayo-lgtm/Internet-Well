# Playbook: Open-Source Adoption

## Purpose

Decide whether and how to adopt an open-source resource while preserving security, licensing, maintainability, compatibility, and reversibility.

## Inputs

Project assessment, required capability, candidate registry records, intended role, deployment model, commercial model, data flows, maintenance capacity, and alternatives.

## Workflow

1. Confirm the capability and whether adoption is necessary.
2. Verify canonical source, release or commit, license, maintainers, activity, releases, advisories, dependencies, telemetry, and documentation.
3. Classify the intended role using `REFERENCE-TYPES.md`.
4. Review compatibility, overlap, operational burden, data exposure, open-core boundaries, trademarks, and network-copyleft implications.
5. Reproduce installation and a representative task in isolation.
6. Compare alternatives and no-adoption option.
7. Define pin, update cadence, SBOM, rollback, ownership, and exit plan.
8. Seek approval before integration and verify the integrated result.

## Outputs

Adoption decision, evidence, intended role, pin, license obligations, security findings, selected alternative, rejected options, integration plan, update policy, rollback, and human-review gates.

## Verification

Re-run the isolated task at the pin; scan dependencies and licenses; inspect network behavior and telemetry; verify uninstall and rollback; test the real integration after authorization.

## Stop conditions

Stop on missing or unsuitable license, suspicious behavior, unresolved critical vulnerabilities, irreproducible installation, false central claims, or an integration that requires copying code contrary to the chosen legal boundary.

## Human review

Open-source counsel, security, architecture, privacy, and domain reviewers must assess high-risk dependencies, copyleft, open-core, production infrastructure, regulated data, and material vendor reliance.
