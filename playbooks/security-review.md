# Playbook: Security Review

## Purpose

Identify exploitable weaknesses in the target product and produce an evidence-backed remediation and verification plan proportionate to its risk.

## Inputs

Project assessment, architecture, data classes, trust boundaries, deployment model, authentication, dependencies, infrastructure, incident history, and authorized test scope.

## Workflow

1. Model assets, actors, entry points, trust boundaries, and abuse cases.
2. Review identity, sessions, authorization, tenant isolation, secrets, input handling, file processing, dependencies, supply chain, infrastructure, logging, and recovery.
3. Select registry resources for secrets detection, SAST, dependency/container scanning, DAST, SBOMs, and threat modeling only where applicable.
4. Run non-destructive checks within scope.
5. Validate high-severity findings manually and remove false positives.
6. Rank by exploitability, impact, exposure, and remediation cost.
7. Define compensating controls, rollback, owners, and retest criteria.

## Outputs

Threat model, tested attack surfaces, verified findings, false positives, severity rationale, selected security bundle, remediation order, evidence, and residual risk.

## Verification

Reproduce each material finding safely; rerun focused checks after fixes; test authorization and tenant boundaries through real interfaces; verify secrets are absent from history and artifacts; and document checks that could not run.

## Stop conditions

Stop before destructive exploitation, persistence, credential use beyond scope, denial of service, production data access, or changes to live security controls.

## Human review

A competent security reviewer must validate critical findings, production exposure, authentication and authorization changes, regulated-data controls, and any claim of security readiness.
