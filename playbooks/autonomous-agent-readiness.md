# Playbook: Autonomous Agent Readiness

## Purpose

Determine whether an agent can safely plan and act with the proposed tools, data, budget, duration, and human supervision.

## Inputs

Agent goal, model, prompts, tools, credentials, memory, environment, action budget, users, external systems, failure history, and evaluation evidence.

## Workflow

1. Convert the goal into bounded tasks, prohibited outcomes, budgets, deadlines, and stop rules.
2. Classify every tool by read, write, external effect, reversibility, and sensitivity.
3. Apply least privilege, sandboxing, scoped credentials, approvals, audit logs, idempotency, retries, and rollback.
4. Test prompt injection, goal drift, fabricated completion, tool failure, data leakage, runaway loops, and recovery.
5. Measure task success, harmful action rate, intervention rate, cost, latency, and truthful status reporting.
6. Select agent runtime, evaluation, sandbox, observability, and workflow resources according to evidence.
7. Stage autonomy from read-only to simulated, supervised, and narrowly authorized actions.

## Outputs

Authority map, tool risk register, evaluation suite, selected resources, action and budget limits, approval gates, incident plan, and readiness verdict.

## Verification

Run adversarial and failure scenarios in isolation; inspect complete action logs; confirm secrets and production access are unavailable; verify stop, rollback, timeout, and approval behavior.

## Stop conditions

Stop before granting unsupervised access to production, money, trading, publishing, communications, credentials, legal, health, employment, personal data, or destructive tools without competent approval.

## Human review

Security, domain, legal, privacy, operations, and business owners must review high-impact agents and all autonomous external actions.
