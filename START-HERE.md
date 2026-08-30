# Start Here — Internet-Well Founder OS Agent Brain

Internet-Well is the Brain a founder or connected AI agent consults before selecting repositories, APIs, skills, models, runtimes, changing a product, launching, or automating high-impact work.

## Start with the outcome

Do not begin by browsing folders or choosing a repository. Describe the result you need.

Examples:

- Audit this product before launch.
- Build this idea into a working product.
- Build a persistent agent that keeps working until the goal is complete.
- Select an autonomous trading research architecture for paper testing.
- Find the right API for a missing capability.
- Select the right testing and security stack.
- Review privacy, legal, accessibility, or AI risk.
- Create a UAT or production-testing system.
- Create a complete brand system with logo, app icons, color, typography,
  design tokens, and component documentation.
- Find a verified reference implementation for a capability.

## Fastest path: ask the Agent Brain

After installation:

```bash
internet-well-brain recommend-stack "<your goal>"
internet-well-brain plan "<your goal>"
internet-well-brain evaluate
```

For a specific capability:

```bash
internet-well-brain find-capability "persistent agent memory"
internet-well-brain find-api "currency exchange data"
internet-well-brain get-skill "Apple motion accessibility"
internet-well-brain recommend-stack "build a brand identity and design system"
```

Connected agents can launch the stdio server:

```bash
internet-well-brain serve
```

The server exposes governed planning tools for capability discovery, stack recommendation, API discovery routing, skill discovery, implementation planning, and bundle evaluation. It does not grant itself permission to install, deploy, trade, use credentials, or modify external systems.

## What the Brain needs

Provide the target repository or product when relevant, intended users, current stage, known stack, hosting, jurisdictions, data handled, critical business constraints, explicit exclusions, success criteria, and what actions the agent may take.

Missing facts should be discovered from authorized sources or marked unknown. They must not be invented.

## Required first pass

1. Read `AGENTS.md`.
2. Define the desired outcome, success criteria, constraints, and non-goals.
3. Run `internet-well-brain recommend-stack "<goal>"` to map the goal to capabilities and a governed bundle.
4. Inspect `integrations/agent-brain/capability-graph.json` and `bundles/agent-brain-bundles.json` when deeper machine-readable evidence is needed.
5. Run the project-intelligence procedure in `skills/experimental/project-intelligence/SKILL.md` when a target repository is in scope.
6. Produce `outputs/project-assessment.schema.json` compatible output where applicable.
7. Apply product profiles in `profiles/` and stack guides in `stacks/`.
8. Select the applicable playbook from `playbooks/`.
9. Use the registry and integration manifests only after capabilities and restrictions are known.
10. Produce a resource-selection record, rejected alternatives, approvals, implementation order, rollback, and verification plan.
11. Run `internet-well-brain evaluate` plus product-specific fixture/runtime tests.
12. Obtain explicit authorization before writes or external state-changing actions.

## Connected-agent prompt

> Use Internet-Well's Agent Brain at the current verified commit. Start from my outcome rather than a tool name. Route the goal to required capabilities and the smallest compatible governed bundle; inspect the target project when relevant; preserve existing product decisions and explicit exclusions; return evidence-ranked resources, rejected alternatives, restrictions, implementation order, rollback, and verification gates. Do not install, modify, deploy, trade, use credentials, or take external actions without explicit authorization. Distinguish passed, failed, blocked, and unverified work. Never treat popularity, public availability, or an exposed credential as authorization.

For the complete request/response contract, use `connections/AGENT-PROTOCOL.md`. For v0.4 specifics, use `docs/AGENT-BRAIN.md`.

## After approval

Use `skills/experimental/adoption-verifier/SKILL.md` and the applicable governed adapter to implement in small reversible slices. Verify real integrated behavior, not just installation. Record exact pins, commands, exit status, evidence, baseline comparison, rollback, residual risk, and human-review requirements.

## Upstream changes

Use:

```bash
internet-well-upstreams --network --output upstream-verification.json
```

Internet-Well does not silently update immutable pins. New releases or changed upstream heads are upgrade candidates that require review before adoption.

## High-risk boundaries

Explicit approval and qualified review are required before production changes, deployments, purchases, account or billing changes, external communications, legal or medical conclusions, financial or live-trading activity, regulated-data processing, credential access, publishing, or destructive action.

The autonomous-trading bundle is research/simulation/paper-trading by default. Restricted adversarial resources are reference-only and excluded from normal routing.

## Honest promise

Internet-Well reduces avoidable mistakes and organizes expert-built resources into traceable, agent-readable workflows. It does not guarantee a bug-free launch, universal compliance, product-market fit, profit, virality, safe autonomous action, successful trading, or accurate prediction.
