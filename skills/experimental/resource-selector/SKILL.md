# Resource Selector Skill

## Purpose

Choose the smallest defensible bundle of verified resources for a completed project assessment and capability gap set.

## Inputs

- schema-valid project assessment;
- selected playbook;
- required capabilities;
- founder constraints and preferences;
- current registry, evidence debt, licenses, and evaluations.

## Procedure

1. Search by capability and product/stack compatibility, not popularity.
2. Eliminate rejected, stale, incompatible, commercially unsuitable, or materially unverified candidates.
3. Apply tier, license, privacy, security, maintenance, cost, and human-review constraints.
4. Distinguish dependency, framework, standard, template, reference implementation, agent runtime, and autonomous system.
5. Prefer the smallest bundle that covers every mandatory capability.
6. Detect overlap, conflicts, provider duplication, and operational burden.
7. Record rejected alternatives and why they lost.
8. Order adoption by dependency and risk.
9. Define verification evidence for every selected resource.
10. Emit `outputs/resource-selection.schema.json` plus a founder-readable explanation.

## Outputs

Selected resources, roles, registry paths, restrictions, rejected alternatives, conflicts, implementation order, verification plan, human-review gates, confidence, and unresolved evidence debt.

## Permission boundary

Selection is read-only. This skill cannot install, fork, copy, deploy, buy, connect accounts, change billing, or modify a target repository.

## Human review

Human approval is required before adopting any resource that affects production, authentication, security, privacy, legal compliance, finances, trading, regulated data, or external communications.

## Evaluation

Pass on fixture assessments when all mandatory capabilities are covered, no rejected resource is selected, Tier C limits remain visible, conflicts are detected, and output validates. Fail on popularity-only selection, unexplained lists, hidden licensing obligations, or missing rejected alternatives.
