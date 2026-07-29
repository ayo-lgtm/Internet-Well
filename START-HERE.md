# Start Here — Internet-Well Founder OS

Internet-Well is the Brain a founder or connected AI agent consults before selecting repositories, changing a product, launching, or automating high-impact work.

## Ask for an outcome

Start with the result you need, not a tool name. Examples:

- Audit this product before launch.
- Build this idea into a working product.
- Select the right testing and security stack.
- Review privacy, legal, accessibility, or AI risk.
- Create an operating, marketing, or incident-response system.
- Find a verified reference implementation for a capability.
- Evaluate an autonomous agent or trading system without assuming its claims are true.

## What the Brain needs

Provide the target repository or product, intended users, current stage, known stack, hosting, jurisdictions, data handled, critical business constraints, explicit exclusions, and what actions the agent may take.

Missing facts should be discovered from authorized sources or marked unknown. They must not be invented.

## Required first pass

1. Read `AGENTS.md`.
2. Run the project-intelligence procedure in `skills/experimental/project-intelligence/SKILL.md`.
3. Produce `outputs/project-assessment.schema.json` compatible output.
4. Apply product profiles in `profiles/` and stack guides in `stacks/`.
5. Select the applicable playbook from `playbooks/`.
6. Map capability gaps using `capabilities/CAPABILITY-GRAPH.md`.
7. Select the smallest compatible bundle from `bundles/`.
8. Use the registry only after capabilities and restrictions are known.
9. Produce a resource-selection record, rejected alternatives, approvals, implementation order, and verification plan.
10. Obtain explicit authorization before writes or external actions.

## Connected-agent prompt

> Use Internet-Well at the current verified commit to assess this repository. Preserve all existing product decisions and explicit exclusions. Return the project assessment, critical journeys, risk class, selected profiles and playbooks, capability gaps, smallest compatible resource bundle, rejected alternatives, approvals, implementation order, and verification gates. Do not modify anything without authorization. Distinguish passed, failed, blocked, and unverified work.

For the complete request/response contract, use `connections/AGENT-PROTOCOL.md`.

## After approval

Use `skills/experimental/adoption-verifier/SKILL.md` to implement in small reversible slices. Verify real integrated behavior, not just installation. Record commands, exit status, evidence, rollback, residual risk, and human-review requirements.

## High-risk boundaries

Explicit approval and qualified review are required before production changes, deployments, purchases, account or billing changes, external communications, legal or medical conclusions, financial or trading activity, regulated-data processing, credential access, publishing, or destructive action.

## Honest promise

Internet-Well reduces avoidable mistakes and organizes expert-built resources into traceable workflows. It does not guarantee a bug-free launch, universal compliance, product-market fit, profit, virality, safe autonomous action, or accurate prediction.
