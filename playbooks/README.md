# Playbooks

Playbooks are end-to-end professional workflows. Select them only after project assessment and capability analysis.

## Product and delivery

- `full-product-build.md` — idea through verified launch and operations.
- `existing-product-audit.md` — assess core value, critical journeys, safety, and sustainability.
- `launch-readiness.md` — make an evidence-backed release decision.
- `product-market-fit.md` — test problem, segment, value, activation, and retention.
- `architecture-review.md` — assess system structure, decisions, resilience, and evolution.

## Trust, risk, and quality

- `security-review.md` — threat model, test, remediate, and retest.
- `privacy-data-governance.md` — map and govern personal and sensitive data.
- `ai-quality-safety.md` — evaluate AI usefulness, grounding, robustness, and boundaries.
- `legal-compliance-readiness.md` — identify obligations, gaps, and counsel questions.
- `accessibility-review.md` — verify critical journeys with assistive technologies.
- `autonomous-agent-readiness.md` — bound and evaluate agents before external action.
- `trading-system-research.md` — reproduce and stress-test trading research before any live use.

## Operations and growth

- `incident-response.md` — contain, investigate, recover, communicate, and learn.
- `operations-monitoring.md` — establish ownership, SLOs, observability, runbooks, and recovery.
- `cost-infrastructure-optimization.md` — reduce cost without hidden reliability or security loss.
- `marketing-system.md` — ethical positioning, distribution, conversion, and learning.
- `open-source-adoption.md` — adopt verified upstream resources with licensing and rollback controls.
- `decision-simulation.md` — supervised stakeholder and scenario analysis, not prediction.

## Playbook contract

Every playbook must define:

- purpose or triggering goal;
- required inputs;
- capability and resource-selection logic;
- ordered workflow;
- outputs;
- verification evidence;
- stop conditions;
- authorization and human-review gates.

`automation/verify_founder_os.py` enforces the structural contract and safety language in CI.
