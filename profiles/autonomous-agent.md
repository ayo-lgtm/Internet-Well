# Autonomous Agent Product Profile

## Applies to

Agents that plan, call tools, browse, write code, operate accounts, schedule work, communicate, transact, or pursue long-running goals.

## Required capabilities

Tool authorization, scoped credentials, action budgets, planning limits, sandboxing, prompt-injection resistance, memory governance, audit logs, human approvals, rollback, idempotency, monitoring, evaluation, and emergency stop.

## Risk model

Primary risks are unauthorized action, goal drift, prompt injection, data exfiltration, runaway cost, destructive retries, fabricated completion, unsafe financial or trading actions, spam, and irrecoverable external effects.

## Completion evidence

Every tool has a declared permission boundary; irreversible actions require approval; secrets are isolated; actions are logged; retries are bounded; failure recovery is tested; adversarial evaluations pass; and the agent accurately reports blocked and unverified work.

## Human review

Competent human review is mandatory before agents access production, finances, trading, legal matters, healthcare, employment, customer communications, credentials, personal data, purchases, publishing, or destructive tools.
