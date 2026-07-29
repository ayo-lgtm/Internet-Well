# Command: Assess Project

## Use when

The agent does not yet have a reliable project profile, or the founder asks what the product needs.

## Inputs

- target repository or product description;
- desired outcome;
- current stage;
- stack and hosting;
- users and jurisdictions;
- sensitive data and high-impact decisions;
- known constraints;
- authorized operating mode.

## Procedure

1. Inspect repository entry points, manifests, deployment configuration, tests, CI, documentation, data stores, authentication, and external services.
2. Identify the product type and matching profile under `profiles/`.
3. Identify stack guides under `stacks/`.
4. Record critical user journeys and failure consequences.
5. Classify data sensitivity and risk.
6. Identify missing evidence rather than guessing.
7. Produce `outputs/project-assessment.schema.json` compatible output.
8. Recommend the next command and applicable playbook.

## Stop conditions

Stop before modifying the target. Stop and surface missing authority when access, credentials, production data, or destructive operations would be required.

## Required result

A concise project profile, confidence level, evidence gaps, risk class, and next recommended workflow.
