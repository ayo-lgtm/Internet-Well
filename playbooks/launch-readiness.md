# Playbook: Launch Readiness

## Goal

Decide whether a product is ready to release and what must be completed before launch.

## Required inputs

Project assessment, release scope, target users, jurisdictions, critical journeys, deployment plan, support plan, business model, and acceptable risk.

## Minimum capability gates

- product value and scope clarity;
- critical-path testing;
- accessibility;
- security and secrets controls;
- privacy and data-flow review;
- legal-compliance triage;
- authentication and authorization where applicable;
- backups, monitoring, incident response, and rollback;
- documentation and ownership;
- AI evaluation and abstention controls where applicable.

## Procedure

1. Define launch acceptance criteria and non-goals.
2. Identify the critical user journeys and failure consequences.
3. Map required capabilities using the capability graph.
4. Select the smallest compatible resource bundle.
5. Inspect and test each launch gate using real integrated behavior.
6. Separate blockers, conditions, post-launch improvements, and optional polish.
7. Confirm rollback, support, monitoring, and incident ownership.
8. Produce a verdict: ready, conditional ready, hold, or stop.

## Required outputs

Launch verdict, blocker list, conditions, evidence by gate, selected resources, unresolved risks, rollback readiness, responsible owner, and retest plan.

## Stop conditions

A launch cannot be marked ready from documentation alone. High-risk legal, privacy, security, financial, medical, or safety conclusions require qualified review.
