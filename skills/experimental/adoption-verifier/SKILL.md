# Adoption and Verification Skill

## Purpose

Integrate an approved resource into a target project in reversible slices and prove that the resulting system works through real interfaces.

## Inputs

Approved resource-selection record, target repository, explicit write scope, acceptance criteria, rollback plan, and required human approvals.

## Procedure

1. Inspect repository instructions, status, dependency policy, CI, and existing user changes.
2. Re-verify the selected resource pin and restrictions if material facts changed.
3. Establish a focused failing check or deterministic baseline where practical.
4. Make the smallest coherent integration change.
5. Run focused tests, then proportionate lint, type, build, integration, security, and end-to-end checks.
6. Verify through public behavior rather than installation success alone.
7. Inspect the diff for secrets, unrelated changes, new network paths, licensing files, telemetry, and rollback safety.
8. Record exact commands, exit status, evidence, failures, blocked checks, and residual risk.
9. Stop before deployment, merge, account changes, purchases, or destructive operations unless separately authorized.

## Outputs

Integrated changes, verification transcript, acceptance-criteria mapping, rollback instructions, remaining risks, failed or unverified checks, and updated adoption decision.

## Permission boundary

This skill may write only within the explicitly authorized repository and file scope. It cannot deploy, merge, purchase, send, sign, trade, delete data, rotate credentials, or modify live systems without separate explicit authorization.

## Human review

High-risk integrations require competent review before production use, especially authentication, authorization, infrastructure, security, privacy, legal, finance, trading, health, and AI systems that materially affect people.

## Evaluation

Pass when fixture integrations are minimal, reversible, test-backed, free of unrelated edits, and accurately report failed or blocked checks. Fail when installation is treated as proof, user work is overwritten, or authority boundaries are crossed.
