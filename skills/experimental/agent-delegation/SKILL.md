# Agent Delegation Skill

## Purpose

Delegate work between specialist agents without creating unbounded authority, hidden tool use, circular delegation, or unverifiable completion claims.

## Inputs

- authorized target system;
- parent-agent objective;
- specialist-agent capabilities;
- tool and data permissions;
- acceptance criteria;
- selected Internet-Well reference implementations.

## Procedure

1. Decompose the objective only where specialist delegation improves quality, parallelism, or verification.
2. Define each delegated task with explicit scope, inputs, outputs, non-goals, deadline or stopping rule, and acceptance criteria.
3. Pass the minimum data and permissions required. Do not inherit all parent-agent credentials or tools by default.
4. Require every handoff to identify the delegating agent, receiving agent, task, allowed tools, and expected artifact or evidence.
5. Prevent recursive or circular delegation unless explicitly bounded by depth and budget.
6. Require receiving agents to return evidence, status, uncertainty, and blocked conditions rather than a bare success signal.
7. Verify delegated outputs at the parent or reviewer layer before treating the overall task as complete.
8. Keep state-changing actions human-gated when the target project requires approval.
9. Log delegation decisions and rejected agent choices so routing can be audited.
10. Test unavailable specialists, conflicting outputs, timeout, partial completion, tool denial, malicious delegated content, and circular delegation.
11. When `patchy631/ai-engineering-hub/agent2agent-demo` is selected, use it as a reference implementation only and independently review protocol assumptions, authentication, transport, tool permissions, and failure handling.

## Outputs

Delegation plan, agent-role map, permission matrix, handoff records, verification results, unresolved conflicts, completion evidence, and residual risks.

## Permission boundary

Delegation never expands authority. A child agent cannot perform an action that the parent agent was not authorized to perform, and delegation does not replace required human approval.

## Human review

Human review is required for production mutations, privileged-data access, external communications, financial actions, legal submissions, destructive operations, security-sensitive changes, or other high-consequence actions.

## Evaluation

Pass when delegated tasks are bounded, traceable, least-privileged, independently verifiable, and fail safely when agents or tools are unavailable. Fail when delegation obscures responsibility, silently expands permissions, loops indefinitely, or accepts unsupported completion claims.
