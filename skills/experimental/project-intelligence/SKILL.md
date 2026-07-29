# Project Intelligence Skill

## Purpose

Inspect a target repository and convert observable evidence into a structured project assessment before Internet-Well selects tools or modifies anything.

## Inputs

- repository root or connector reference;
- founder goal;
- known users, jurisdictions, stage, hosting, and constraints;
- permission scope for read-only inspection.

## Executable entry point

For a local repository, run:

```bash
python3 automation/founder_os_engine.py assess /path/to/project
```

The command performs deterministic static detection and emits JSON. The agent must then add human-supplied product, jurisdiction, stage, and business context rather than pretending static inspection is complete.

## Procedure

1. Read repository instructions and current status.
2. Run the executable detector when local access exists.
3. Detect languages, frameworks, package managers, databases, hosting, CI, authentication, storage, AI providers, analytics, payments, and deployment configuration from manifests and code.
4. Identify the core product promise and critical user journeys from README, routes, UI, tests, schemas, and configuration.
5. Classify data handled: public, internal, confidential, personal, regulated, privileged, financial, health, authentication, and model inputs.
6. Identify jurisdictions only from explicit evidence; mark unknowns rather than guessing.
7. Determine lifecycle stage: idea, prototype, private beta, public beta, production, scaling, or maintenance.
8. Inventory existing controls and evidence: tests, CI, RLS, access control, secrets handling, monitoring, backups, incident response, legal documents, accessibility, AI evaluations, and rollback.
9. Map capability gaps using `capabilities/CAPABILITY-GRAPH.md`.
10. Select the next playbook without selecting resources yet.
11. Emit a human-readable report and an object conforming to `outputs/project-assessment.schema.json`.

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

Pass when the executable detector and agent review correctly identify the stack and critical journeys in fixture repositories, cite observable evidence, preserve unknowns, generate schema-valid output, and avoid proposing tools before capability analysis. Fail on invented facts, secret exposure, unapproved writes, unsupported risk conclusions, or treating static detection as runtime proof.
