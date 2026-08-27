# Internet-Well Agent Operating Contract

Internet-Well is the evidence-backed Founder OS Agent Brain for software founders and connected AI agents. It is not a random directory of repositories, and a recommendation or evidence score is never permission to install or execute a resource.

## Mission

Convert a founder's goal into a defensible capability plan, route to the smallest compatible governed resource bundle, implement only with authorization, and verify the result with fresh evidence.

## Required operating sequence

1. Identify the intended outcome, success criteria, constraints, data classification, and non-goals.
2. Inspect the target project's stack, stage, users, jurisdictions, deployment environment, data sensitivity, and risk level when a project is in scope.
3. Route the goal through the Agent Brain before browsing individual resources: `internet-well-brain recommend-stack "<goal>"`.
4. Use `integrations/agent-brain/capability-graph.json` to select capabilities before tools and `bundles/agent-brain-bundles.json` for composed architectures.
5. Select the applicable playbook in `playbooks/` and create a project profile using `outputs/project-assessment.schema.json` where applicable.
6. Consult registry and integration records as evidence-backed candidates, not automatic install instructions.
7. Apply provenance, compatibility, maintenance, security, privacy, license, cost, interoperability, runtime-evidence, reversibility, and human-review constraints.
8. Produce a resource-selection record with selected and rejected alternatives before changing another repository or system.
9. Run the Agent Brain structural evaluation and any resource-specific fixture/baseline tests before adoption.
10. Ask for explicit authorization before writes, installations, deployments, purchases, account changes, external communications, credential use, production actions, or destructive operations.
11. Implement in small, reversible slices with stop conditions and rollback.
12. Verify the integrated result and report completed, blocked, failed, and unverified work separately.
13. Record exact pins, evidence, known limitations, upstream-monitoring plan, and required human review.

## Agent Brain and MCP rules

- `internet-well-brain serve` is a planning and governed-selection interface. Its MCP-style tools do not grant production authority.
- `find_capability`, `recommend_stack`, `find_api`, `get_skill`, `plan_implementation`, and `evaluate_bundle` are read/plan/evaluate operations.
- A client must separately obtain authorization before invoking any state-changing adapter or external system.
- If no exact bundle matches, prefer ranked capability candidates over inventing a stack.
- Restricted references are excluded from default routing.
- Do not expand a user's requested scope merely because more tools are available.

## Selection and ranking rules

- Prefer outcomes and capabilities over popularity.
- Never choose a resource solely because it has the highest evidence score, star count, marketplace rank, or social-media attention.
- Evidence scores are prioritization aids, not certifications.
- Tier A requires qualified, conflict-disclosed human review and cannot be assigned by automation.
- Tier B may be used with documented limitations. Tier C requires supervision and must not be represented as production-proven.
- Recheck any record older than 90 days or affected by material upstream change.
- Respect `required_human_review`, license obligations, provider terms, restrictions, and `when not to use` guidance.
- Select the smallest compatible bundle that covers the required outcome.
- Do not silently replace a founder's chosen stack, product decision, or risk tolerance.

## Upstream and supply-chain rules

- Never silently update an immutable upstream pin.
- Use `internet-well-upstreams` to generate an upstream review report.
- A changed upstream is an upgrade candidate, not an automatic update.
- Before upgrading, review provenance, license changes, security advisories, release notes, breaking changes, compatibility, fixture results, rollback, and better alternatives.
- Never execute unreviewed upstream installers, hooks, scripts, or binaries merely because a resource is cataloged.
- Never use leaked, copied, exposed, or third-party credentials to avoid pricing, quotas, authentication, or provider controls.
- Public API directory membership does not establish authorization, reliability, free usage, or unlimited usage.

## Safety and authority boundaries

Agents may read, analyze, compare, rank, route, draft, evaluate structurally, and recommend without additional authority. Agents must receive explicit authorization before they:

- modify a product repository;
- install dependencies or execute upstream installers;
- change infrastructure, databases, authentication, permissions, billing, domains, or production systems;
- use credentials or connect a new external provider;
- send messages, submit forms, publish, merge, deploy, sign, purchase, delete, or perform other state-changing actions;
- process confidential, privileged, regulated, or personal data through a new provider;
- place trades or grant a trading agent live brokerage authority.

The `autonomous-trading-research` bundle is research, simulation, and paper-trading by default. Live trading requires separate broker authorization, explicit deployment approval, bounded position/loss limits, auditability, monitoring, kill switches, and applicable compliance/risk review.

## Restricted and adversarial resources

Resources classified as `restricted-reference`, including `qwen38-uncensored`, are reference-only for authorized adversarial or safety evaluation. Internet-Well must not automatically install, execute, route normal workloads to, or grant credentials to such resources.

## Verification requirements

Structural Agent Brain evaluation is necessary but not sufficient. Use `internet-well-brain evaluate` to verify graph/bundle integrity, then run product-specific tests appropriate to the selected bundle, including as applicable:

- unit and integration tests;
- end-to-end/runtime tests;
- restart/recovery tests for persistent agents;
- authorization and access-control tests;
- security and privacy checks;
- accessibility and reduced-motion checks;
- performance and resource-consumption checks;
- rollback/kill-switch tests;
- baseline comparisons;
- paper/simulation evaluation before any financial deployment.

Do not convert a structural pass into a claim of real-world production correctness.

## Required outputs

Every substantial run should produce, as applicable:

- project assessment;
- selected playbook or Agent Brain bundle;
- capability gaps;
- resource selection with evidence and rejected alternatives;
- implementation/adoption plan;
- exact pins and provider requirements;
- verification evidence and baseline comparison;
- remaining risks, stop conditions, rollback, and human-review requirements.

Use the schemas in `outputs/` when machine-readable output is useful.

## Repository map

- `START-HERE.md`: founder and agent entry point.
- `FOUNDER-OS.md`: architecture and operating model.
- `integrations/agent-brain/capability-graph.json`: unified capability graph and ranking evidence.
- `integrations/agent-brain/mcp.json`: universal agent connection descriptor.
- `bundles/agent-brain-bundles.json`: composed governed architectures.
- `docs/AGENT-BRAIN.md`: v0.4 routing, MCP, evaluation, and governance documentation.
- `commands/`: task-oriented procedures.
- `playbooks/`: end-to-end professional workflows.
- `capabilities/`: legacy and explanatory outcome-to-capability guidance.
- `profiles/`: product-type guidance.
- `stacks/`: technology-specific guidance.
- `skills/`: packaged agent capabilities and lifecycle.
- `registry/`: verified resources and restrictions.
- `integrations/`: executable or governed adapters.
- `evaluations/`, `evidence/`, `licenses/`: proof and governance.
- `.github/rulesets/main-protection.json`: declarative intended main-branch protection policy; GitHub repository settings remain the enforcement authority.

## Anti-patterns

Do not browse the registry without first defining the goal. Do not recommend a long undifferentiated list. Do not equate evidence ranking with approval. Do not claim a tool guarantees security, compliance, virality, profitability, accurate prediction, successful trading, or a bug-free launch. Do not copy upstream repositories into Internet-Well merely to make the catalog larger. Do not confuse a reference implementation with an approved production dependency. Do not let persistent loops become unbounded, privilege-escalating, or impossible to stop.
