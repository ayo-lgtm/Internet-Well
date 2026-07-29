# Bundle: Autonomous Agent

## Outcome

Create a narrowly bounded agent that can complete defined work with scoped tools, truthful status reporting, containment, approvals, and recoverable failure.

## Required capabilities

Task decomposition, tool authorization, sandboxing, scoped credentials, prompt-injection defense, memory governance, action budgets, idempotency, retries, approvals, audit logs, evaluation, monitoring, rollback, and emergency stop.

## Selection rules

Apply `profiles/autonomous-agent.md`. Treat claims of arbitrary task completion, profit, virality, or self-funding as unverified until independently reproduced. Prefer deterministic workflows for high-impact actions and keep experimental runtimes supervised.

## Implementation order

1. define goal, exclusions, success, budget, and stop rules;
2. classify tools and data;
3. implement read-only simulation;
4. evaluate adversarial and failure behavior;
5. add narrowly scoped supervised writes;
6. establish audit, monitoring, rollback, and incidents;
7. consider additional autonomy only from evidence.

## Verification

Run injection, goal-drift, tool-failure, stale-data, duplicate-action, runaway-loop, false-completion, secret-exposure, timeout, stop, and rollback tests in isolation; inspect full action logs.

## Human review

Security, legal, privacy, operations, finance, and domain owners must review any production, financial, trading, publishing, communication, employment, health, legal, personal-data, credential, purchase, or destructive action.
