# Execution Orchestration v0.6

Execution Orchestration connects Internet-Well's Agent Brain, structured knowledge, adapters, reliability verifier, and durable task state into one closed-loop lifecycle:

`goal -> plan -> select -> authorize -> execute -> verify -> recover -> complete`

## Guarantees

- Planning never implies execution authority.
- State-changing adapters require explicit scopes and, for Tier A work, recorded human approval.
- Every task has a checkpoint hash and can be resumed only after integrity verification.
- Execution is adapter-based. GitHub, Vercel, Railway, Supabase, browser, Ollama, MCP, and design are represented as governed capability surfaces; credentials remain external.
- The independent Reliability Layer decides completion from observable evidence rather than agent self-report.
- Failed verification can enter bounded recovery only when the failure is reversible and is not a policy/authorization/secret-exposure failure.
- A task cannot transition to `completed` unless the verifier returns `PASS`.

## Operational control plane

`internet-well-orchestrate control-plane task.json` returns task ID, goal, risk tier, lifecycle stage, status, attempts, selected adapters, authorization scopes, approval count, verification result, trajectory metrics, and checkpoint identity.

## Durable task example

```bash
internet-well-orchestrate new "make this repository production-ready" --risk A --criterion tests_green --criterion security_review_passed --out task.json
internet-well-orchestrate select task.json github vercel --out task.json
internet-well-orchestrate authorize task.json --scope repository:feature-branch --scope preview-deploy --approval release-owner-approved --out task.json
internet-well-orchestrate control-plane task.json
```

Actual adapter handlers are supplied by the host/runtime that has the user's authorized connector or credential context. The core package deliberately does not embed cloud secrets or silently obtain broader permissions.

## Design/UI/UX execution

The `design` adapter is a first-class orchestration surface. It can route a task to Internet-Well's Apple Design Skills, screenshot/UI-analysis resources, Open Design knowledge source, and other governed visual/design resources before implementation and visual validation. Design recommendations remain evidence-backed inputs; they do not override accessibility, target-platform, product, or repository requirements.
