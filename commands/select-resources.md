# Command: Select Resources

## Purpose

Choose a defensible tool, standard, framework, template, reference implementation, service, runtime, or skill only after the project and capability gaps are understood.

## Inputs

- schema-valid project assessment;
- selected playbook;
- required capabilities and acceptance criteria;
- product and stack profiles;
- founder constraints, preferences, budget, and hosting model;
- current registry, evidence debt, licenses, and evaluations.

## Procedure

1. Define the outcome and acceptance criteria.
2. Map the outcome to capabilities in `capabilities/CAPABILITY-GRAPH.md`.
3. Search only relevant registry categories and bundles.
4. Classify each candidate's intended role using `REFERENCE-TYPES.md`.
5. Evaluate fit, tier, freshness, testing, maintenance, license, security, privacy, cost, hosting, data flows, and stack compatibility.
6. Exclude rejected, stale, incompatible, legally unsuitable, duplicative, or materially unverified candidates.
7. Select the smallest adequate bundle.
8. Document alternatives and why they were rejected.
9. State implementation order, required human review, adoption risks, verification, rollback, and open evidence debt.
10. Produce `outputs/resource-selection.schema.json` compatible output.

## Selection precedence

1. mandatory compatibility and safety;
2. evidence and maintenance quality;
3. license and data suitability;
4. integration effort, operating burden, and reversibility;
5. score, popularity, and reputation.

A high score, expert reputation, or working demonstration never overrides incompatibility or restrictions.

## Output

Selected capability bundle, selected resources and registry paths, intended roles, reason for each choice, rejected alternatives, restrictions, implementation order, verification plan, approvals, confidence, and unresolved evidence.
