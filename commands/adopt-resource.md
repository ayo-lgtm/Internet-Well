# Command: Adopt Resource

## Purpose

Integrate an already selected and authorized resource into a target project in the smallest reversible slice and verify the real result.

## Inputs

- completed project assessment;
- documented resource selection and intended role;
- explicit implementation authorization;
- exact resource pin;
- target repository and allowed file scope;
- acceptance criteria;
- license, privacy, cost, infrastructure, and data-flow implications;
- rollback conditions and required human approvals.

## Procedure

1. Read the selected registry record and upstream guidance at the pin.
2. Recheck material upstream changes and open evidence debt.
3. Inspect target conventions, current status, tests, CI, and dependency boundaries.
4. Establish a focused baseline or failing check where practical.
5. Implement the smallest coherent integration.
6. Add only necessary configuration, documentation, and tests.
7. Verify through the target system's real interfaces.
8. Inspect the diff for secrets, unrelated work, permission changes, telemetry, network paths, and licensing files.
9. Record exact versions, commands, exit status, files changed, evidence, failures, blocked checks, rollback, and residual risk.
10. Stop before deployment, merge, purchase, account change, communication, or destructive action unless separately authorized.

## Output

Produce `outputs/adoption-plan.schema.json` compatible output containing the selected pin, intended role, scope, configuration decisions, permission changes, data flows, costs, license obligations, implementation steps, verification results, rollback, status, remaining risks, and human review.
