# Autonomous Engineering System

Internet Well's Autonomous Engineering System turns a product or engineering goal into a small, dynamically assembled specialist team rather than a fixed swarm of personas.

```text
Goal
  ↓
Chief of Staff / Coordinator
  ↓
Product + UX + Engineer (as needed)
  ↓
Security / Compliance / QA / Release reviewers (as needed)
  ↓
Independent Verifier
  ↓
Human release approval for Tier A work
```

The implementation lives in `automation/autonomous_engineering.py` and wraps the existing governed `execution_orchestrator`. It does not add a second authorization system and does not execute external services by itself.

## Guarantees

- A minimum team always includes coordinator, implementer, QA, and an independent verifier.
- Additional roles are selected from the goal instead of being spawned by default.
- The verifier is explicitly independent from the engineer and chief-of-staff roles.
- Production, deployment, security, legal/compliance, credential-bearing, and other consequential work remains Tier A under the existing orchestrator.
- External calls stay behind host adapters; credentials never enter task state.
- State-changing actions still require explicit approval through `execution_orchestrator`.
- Provider routing is advisory and provider-neutral. A host may substitute a provider without weakening permissions, approvals, or reviewer independence.
- Provider failure uses ranked fallback rather than collapsing the task.
- Completion depends on observable evidence and independent verification, not an implementer's `done` message.

## Roles

`chief-of-staff` owns decomposition and sequencing. `product` defines observable product/user acceptance criteria. `ux` owns flow quality, visual/interaction states, and accessibility. `engineer` implements. `security` threat-models and reviews auth, secrets, dependencies, and abuse. `compliance` reviews licensing, privacy, legal/compliance, and provenance. `qa` owns independent critical-journey and regression testing. `release` validates deployment, rollback, observability, and release evidence. `verifier` independently decides whether the evidence proves completion.

## Model router

The first clean-room router policy ranks currently modeled providers (`codex`, `claude`, `gemini`, `grok`, `groq`) by role/task capability overlap and then by lower nominal cost/latency. These are routing hints rather than provider endorsements or hard dependencies. The host is responsible for actual provider availability, model selection, authentication, data handling, and pricing.

## CLI

```bash
# Assemble and persist a governed team around a goal.
internet-well-engineering team \
  "make this product production-ready" \
  --state-dir /tmp/iw-tasks

# Inspect only the role/task graph.
internet-well-engineering graph \
  "launch an accessible app with authentication"

# Inspect provider fallbacks by role.
internet-well-engineering route \
  "fix and test the repository"
```

The generated team object contains the underlying orchestrator task id, risk tier, scenario, selected host adapters, role definitions, dependency graph, provider routes, and governance boundaries.

## Grok Bot clean-room extraction

The Grok Bot 0.18 reconstruction is used only as an architectural research input. Internet Well independently implements the reusable concepts: coordinator/host separation, provider routing, shared tool contracts, checkpointed task graphs, sandbox boundaries, and independent evaluation. Reconstructed Grok Bot source or bundled application artifacts are not imported into this runtime.

## FingerprintJS

FingerprintJS is separately registered as an `approved-with-restrictions` security resource. It may be proposed for narrowly scoped abuse/fraud controls, but browser fingerprinting must not be silently introduced as generic analytics. Production activation requires explicit security/product/privacy review and the existing state-change approval boundary.
