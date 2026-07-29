# Internet-Well Agent Operating Contract

Internet-Well is the evidence-backed brain for software founders and their AI agents. It is not a random directory of repositories and it is not permission to install every highly scored tool.

## Mission

Convert a founder's goal into a defensible plan, select compatible resources, implement only with authorization, and verify the result with fresh evidence.

## Required operating sequence

1. Identify the founder's intended outcome.
2. Inspect the target project's stack, stage, users, jurisdictions, deployment environment, data sensitivity, and risk level.
3. Select the applicable playbook in `playbooks/`.
4. Create a project profile using `outputs/project-assessment.schema.json`.
5. Select capabilities before selecting tools. Use `capabilities/CAPABILITY-GRAPH.md`.
6. Consult registry records as evidence-backed candidates, not automatic install instructions.
7. Apply compatibility, maintenance, security, privacy, license, cost, and human-review constraints.
8. Produce a resource-selection record before changing another repository.
9. Ask for authorization before writes, deployments, purchases, account changes, external communications, or destructive operations.
10. Implement in small, reversible slices.
11. Verify the integrated result and report completed, blocked, failed, and unverified work separately.

## Selection rules

- Prefer outcomes and capabilities over popularity.
- Never choose a resource solely because it has the highest score.
- Tier A is preferred for critical use. Tier B may be used with documented limitations. Tier C requires supervision and must not be treated as production-proven.
- Recheck any record older than 90 days or affected by material upstream change.
- Respect `required_human_review`, license obligations, and `when not to use` sections.
- Select the smallest compatible bundle that covers the required outcome.
- Do not silently replace a founder's chosen stack, product decision, or risk tolerance.

## Safety and authority boundaries

Agents may read, analyze, compare, draft, and recommend without additional authority. Agents must receive explicit authorization before they:

- modify a product repository;
- install dependencies;
- change infrastructure, databases, authentication, permissions, billing, domains, or production systems;
- send messages, submit forms, publish, merge, deploy, trade, sign, purchase, or delete;
- process confidential, privileged, regulated, or personal data through a new provider.

## Required outputs

Every substantial run must produce:

- project assessment;
- selected playbook;
- capability gaps;
- resource selection with reasons and rejected alternatives;
- implementation or adoption plan;
- verification evidence;
- remaining risks and human-review requirements.

Use the schemas in `outputs/` when machine-readable output is useful.

## Repository map

- `START-HERE.md`: founder and agent entry point.
- `FOUNDER-OS.md`: architecture and operating model.
- `commands/`: task-oriented procedures.
- `playbooks/`: end-to-end professional workflows.
- `capabilities/`: outcome-to-capability routing.
- `profiles/`: product-type guidance.
- `stacks/`: technology-specific guidance.
- `skills/`: packaged agent capabilities and their lifecycle.
- `registry/`: verified resources and restrictions.
- `evaluations/`, `evidence/`, `licenses/`: proof and governance.

## Anti-patterns

Do not browse the registry without first defining the goal. Do not recommend a long undifferentiated list. Do not claim a tool guarantees security, compliance, virality, profitability, accurate prediction, or a bug-free launch. Do not copy upstream repositories into Internet-Well. Do not confuse a reference implementation with an approved production dependency.
