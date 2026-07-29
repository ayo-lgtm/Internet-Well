# Bundle: Autonomous Agent

## Outcome

Create a narrowly bounded agent that can complete defined work with scoped tools, truthful status reporting, containment, approvals, and recoverable failure.

## Required capabilities

Task decomposition, tool authorization, sandboxing, scoped credentials, prompt-injection defense, memory governance, action budgets, idempotency, retries, approvals, audit logs, evaluation, monitoring, rollback, and emergency stop.

## Recommended resource set

- orchestration: LangGraph for durable stateful workflows or PydanticAI for typed Python agents;
- enterprise alternative: Semantic Kernel where its plugin and enterprise ecosystem are a better fit;
- tool protocol: MCP Python SDK and reviewed MCP reference servers;
- browser access: Playwright first; Playwright MCP only with explicit browser-session and credential boundaries;
- coding-agent reference: OpenHands and Aider as architectural references or supervised tools, not proof of arbitrary completion;
- browser-agent reference: Browser Use only in sandboxed, allow-listed environments;
- evaluation: Inspect AI for high-assurance agent evaluation, Promptfoo for rapid regression and adversarial cases;
- observability: Langfuse where prompt, trace, retention, and provider-data review are complete;
- policy: deterministic allow lists and approval gates first; OPA only when policy complexity justifies it;
- simulation: MiroFish and its CLI fork are reference implementations for scenario structure only, not validated prediction engines;
- legacy reference: AutoGen remains useful for migration and architecture study but should not be the greenfield default while in maintenance mode.

## Selection rules

Apply `profiles/autonomous-agent.md`. Treat claims of arbitrary task completion, profit, virality, self-funding, or guaranteed outcomes as unverified until independently reproduced. Prefer deterministic workflows for high-impact actions. Select one primary orchestration framework and one evaluation path unless evidence requires more.

## Implementation order

1. define goal, exclusions, success criteria, budget, and stop rules;
2. classify every tool, credential, data source, and external effect;
3. implement read-only simulation and deterministic dry runs;
4. evaluate injection, drift, false-completion, tool-failure, and runaway behavior;
5. add narrowly scoped supervised writes with idempotency and approval;
6. establish audit logs, monitoring, rollback, and incident procedures;
7. consider additional autonomy only after measured evidence.

## Verification

Run prompt injection, goal drift, tool failure, stale data, duplicate action, runaway loop, false completion, secret exposure, timeout, stop, rollback, and permission-escalation tests in isolation. Inspect complete action logs and verify no unapproved external effect occurred.

## Human review

Security, legal, privacy, operations, finance, and domain owners must review any production, financial, trading, publishing, communication, employment, health, legal, personal-data, credential, purchase, or destructive action. Agent-runtime catalog entries remain supervised until promoted through evaluated skills and registry evidence.
