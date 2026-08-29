# Execution Orchestration v0.6

Execution Orchestration connects Internet-Well's Agent Brain, structured knowledge layer, host adapters, Reliability Layer, approvals, durable task state, and bounded recovery into one closed-loop lifecycle:

`goal -> plan/discover -> queue -> approve -> host execute -> record evidence -> recover if needed -> independently verify -> release`

The orchestrator does **not** silently call cloud providers or obtain credentials. It produces governed action requests for a host/runtime that already has the user's authorized connector context.

## Core guarantees

- Planning and discovery never imply execution authority.
- Task state is local JSON by default (`~/.local/share/internet-well/tasks`) and can be relocated with `INTERNET_WELL_TASK_STATE`.
- Task state is sanitized before persistence; passwords, API keys, tokens, secrets, private keys, and similar credential material are rejected from persisted action payloads.
- Read-only and state-changing adapter actions are declared separately.
- State-changing actions do not enter a dispatch manifest until a specific approval is recorded.
- A dispatch manifest is an execution request, not an execution engine. The host must invoke the matching connected adapter.
- Execution results require observable evidence.
- Failed actions enter a bounded recovery loop. State-changing retries require fresh approval; retry budgets prevent unbounded autonomous loops.
- Completion comes from the independent Reliability Layer rather than an agent's self-report.
- Tier A/consequential work can end in `HUMAN_REVIEW`; a separate human release approval is then required to mark the task complete.

## Host adapters

v0.6 defines governed contracts for GitHub, Vercel, Railway, Supabase, browser automation, Ollama, MCP tools, and design/UI/UX tooling. Each contract declares discovery keywords, capabilities, read-only actions, state-changing actions, host boundary, credential boundary, and execution constraints.

The core package never claims that an adapter is connected merely because its contract exists. The runtime must supply the actual connected tool and authorization.

## CLI

The packaged command is `internet-well-orchestrator` (with `internet-well-orchestrate` retained as an alias).

```bash
# Start and persist a task. Agent Brain + knowledge routing run automatically.
internet-well-orchestrator --state-dir /tmp/iw-tasks start \
  "make this repository production-ready"

# Ask what the task should do next.
internet-well-orchestrator --state-dir /tmp/iw-tasks next TASK_ID

# Queue a state-changing operation. This remains blocked on approval.
internet-well-orchestrator --state-dir /tmp/iw-tasks request-action \
  TASK_ID github write-file --payload '{"path":"README.md"}'

internet-well-orchestrator --state-dir /tmp/iw-tasks approve \
  TASK_ID ACTION_ID --by release-owner

# Produce host-executable requests. This does not invoke GitHub itself.
internet-well-orchestrator --state-dir /tmp/iw-tasks dispatch-manifest TASK_ID

# After the host executes it, record observable evidence.
internet-well-orchestrator --state-dir /tmp/iw-tasks record-result \
  TASK_ID ACTION_ID --success --evidence ci-green --evidence commit-created

# Run independent completion verification.
internet-well-orchestrator --state-dir /tmp/iw-tasks verify TASK_ID

# View every local task as a compact operational control plane.
internet-well-orchestrator --state-dir /tmp/iw-tasks control-plane
```

## Recovery

`recover TASK_ID ACTION_ID` creates a bounded retry proposal for a failed action. `materialize-recovery` turns an approved proposal into a fresh action. Read-only work can be eligible for automatic retry by a supervising host, but the core package still only creates the proposal/action; it does not bypass the host boundary. State-changing retries always return to the approval gate.

Failures connected to policy violations, unauthorized writes, secret exposure, or fabricated verification are not candidates for automatic retry.

## Operational control plane

`control-plane` aggregates local task status, risk tier, checkpoint, action count, approvals waiting, failures, cost, latency, verification result, and last update time. It is intentionally local/private by default.

## Design and UI/UX execution

Design is a first-class adapter, not a cosmetic afterthought. Internet-Well already has multiple governed design/UI/UX resources that can be used before implementation and again during verification:

- **Open Design** for agentic design workflow, UI/UX workflow, design systems, prototypes, artifact generation, and design-to-code handoff.
- **Apple Design Skills** for platform-aware design reasoning, visual foundations, interaction, motion, HIG-oriented guidance, accessibility, responsive layout, and brand distinctiveness.
- **Playwright MCP / screenshot resources** for browser-based UI inspection, accessibility snapshots, persistent-context testing, and visual/runtime validation.
- The Reliability Layer includes an **agentic design handoff** benchmark so a design workflow can be evaluated rather than merely generated.

The design adapter references these resources directly. A generated design or design-to-code proposal still follows the same repository approval, accessibility, runtime-testing, and independent-verification gates as other implementation work.
