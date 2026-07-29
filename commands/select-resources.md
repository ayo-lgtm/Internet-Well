# Command: Select Resources

## Use when

A project profile exists and the founder needs a defensible tool, standard, framework, template, reference implementation, or skill selection.

## Procedure

1. Define the outcome and acceptance criteria.
2. Map the outcome to capabilities in `capabilities/CAPABILITY-GRAPH.md`.
3. Search only relevant registry categories.
4. Evaluate each candidate for fit, tier, freshness, testing, maintenance, license, security, privacy, cost, hosting model, and stack compatibility.
5. Exclude candidates that violate hard constraints.
6. Select the smallest adequate bundle.
7. Document alternatives and why they were rejected.
8. State required human review and adoption risks.
9. Produce `outputs/resource-selection.schema.json` compatible output.

## Selection precedence

1. mandatory compatibility and safety;
2. evidence and maintenance quality;
3. license suitability;
4. integration effort and operational burden;
5. score and popularity.

A high score never overrides incompatibility or restrictions.

## Required result

- selected capability bundle;
- selected resources and exact registry paths;
- reason for each selection;
- rejected alternatives;
- implementation order;
- verification plan;
- confidence and unresolved evidence.
