# Start Here

Internet-Well helps a founder or AI agent move from **a goal** to **a verified implementation plan**.

Do not begin by searching for a tool. Begin by stating the outcome.

## Common starting requests

- Build a new product.
- Review an existing product.
- Prepare a product for launch.
- Improve security, privacy, accessibility, reliability, or compliance.
- Select the right stack or infrastructure.
- Add testing, monitoring, backups, documentation, marketing, or operations.
- Investigate a failure or incident.
- Simulate how stakeholders may react to a decision.
- Find a proven open-source reference implementation for a capability.

## For founders

Tell the agent:

1. what you are building or changing;
2. the target repository or product;
3. the desired outcome;
4. known stack and hosting;
5. current stage: idea, prototype, beta, pre-launch, live, or scaling;
6. users and jurisdictions;
7. sensitive data or high-risk decisions involved;
8. whether the agent may only recommend or may also implement.

A minimal request can be:

> Use Internet-Well to audit this repository for launch. Select the appropriate playbook and resources, explain your choices, implement only after authorization, and verify every change.

## For AI agents

Read in this order:

1. `AGENTS.md`
2. `FOUNDER-OS.md`
3. the applicable file under `commands/`
4. the applicable playbook under `playbooks/`
5. `capabilities/CAPABILITY-GRAPH.md`
6. relevant product profiles and stack guides
7. registry records for candidate resources

Do not start with `registry/INDEX.md` unless the goal and capability gaps are already defined.

## Operating modes

### Recommend
Analyze and produce a selection and adoption plan. Do not modify a target repository.

### Implement
After authorization, make scoped changes, run checks, and return verification evidence.

### Audit
Inspect without changing the target. Produce findings prioritized by impact and confidence.

### Monitor
Recheck time-sensitive evidence, dependencies, incidents, releases, or external conditions on an approved cadence.

## What a good result contains

- concise project profile;
- selected playbook and why;
- capability gaps;
- recommended bundle, not an unstructured tool list;
- compatibility and license analysis;
- implementation sequence;
- verification results;
- unresolved risks and required human review.

## Current maturity

The verified registry and evidence system are operational. The Founder OS execution layer is being expanded incrementally. Treat skills marked experimental as supervised procedures, not autonomous production authority.
