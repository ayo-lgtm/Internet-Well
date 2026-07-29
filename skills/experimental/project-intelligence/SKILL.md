# Project Intelligence Skill

## Purpose

Inspect a target repository and convert observable evidence into a structured project assessment before Internet-Well selects tools or modifies anything.

## Inputs

- repository root or connector reference;
- founder goal;
- known users, jurisdictions, stage, hosting, and constraints;
- permission scope for read-only inspection.

## Procedure

1. Read repository instructions and current status.
2. Detect languages, frameworks, package managers, databases, hosting, CI, authentication, storage, AI providers, analytics, payments, and deployment configuration from manifests and code.
3. Identify the core product promise and critical user journeys from README, routes, UI, tests, schemas, and configuration.
4. Classify data handled: public, internal, confidential, personal, regulated, privileged, financial, health, authentication, and model inputs.
5. Identify jurisdictions only from explicit evidence; mark unknowns rather than guessing.
6. Determine lifecycle stage: idea, prototype, private beta, public beta, production, scaling, or maintenance.
7. Inventory existing controls and evidence: tests, CI, RLS, access control, secrets handling, monitoring, backups, incident response, legal documents, accessibility, AI evaluations, and rollback.
8. Map capability gaps using `capabilities/CAPABILITY-GRAPH.md`.
9. Select the next playbook without selecting resources yet.
10. Emit a human-readable report and an object conforming to `outputs/project-assessment.schema.json`.

## Outputs

- product and stack classification;
- evidence-backed critical journeys;
- current controls;
- data and risk classification;
- capability gaps;
- unknowns and evidence gaps;
- recommended playbook;
- confidence per material conclusion.

## Permission boundary

This skill is read-only. It must not install packages, change files, access production secrets, query production data, deploy, purchase, send messages, or alter accounts. It may inspect only sources the user has authorized.

## Human review

A human must confirm jurisdictions, regulated-data classifications, business-critical journeys, and any conclusion affecting legal, financial, employment, healthcare, safety, or production decisions.

## Evaluation

Pass when the skill correctly identifies the stack and critical journeys in fixture repositories, cites observable evidence, preserves unknowns, generates schema-valid output, and avoids proposing tools before capability analysis. Fail on invented facts, secret exposure, unapproved writes, or unsupported risk conclusions.
