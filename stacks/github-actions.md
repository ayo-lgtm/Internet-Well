# GitHub Actions Stack Guide

## Detection

Look for workflow YAML under `.github/workflows`, reusable workflows, action pins, repository secrets, environments, artifacts, deployment jobs, and scheduled runs.

## Required controls

Least-privilege permissions, immutable action pins, secret isolation, protected environments, untrusted pull-request boundaries, artifact retention, dependency provenance, concurrency controls, timeouts, failure reporting, and deployment approvals.

## Compatible capabilities

CI validation, supply-chain security, secrets detection, dependency scanning, test orchestration, release provenance, deployment verification, scheduled rechecks, and evidence artifact generation.

## Verification

Lint workflow syntax; inspect permissions and event triggers; verify third-party action pins; test representative pull-request and protected-branch paths; confirm secrets are unavailable to untrusted forks; review artifacts, timeouts, and failure behavior.

## Human review

Workflows with write tokens, package publishing, deployments, secrets, cloud credentials, production access, or destructive automation require explicit authorization and security review.
