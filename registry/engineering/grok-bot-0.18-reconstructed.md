---
name: Grok Bot 0.18 Reconstructed
category: engineering
subcategory: agent-orchestration-reference
status: experimental
tier: C
human_reviewed: false
type: reference-implementation
canonical_repo: https://github.com/b-nnett/grok-bot-0.18-reconstructed
website: null
pinned_version: main snapshot observed 2026-08-29; repository archived
license: NOASSERTION (repository exposes no license)
score: 72
confidence: high
tested: false
last_verified: 2026-08-29
---

# Grok Bot 0.18 Reconstructed — agent orchestration and runtime reference

## What it is
An unofficial, source-oriented reconstruction and extension of the publicly
shipped Grok Bot 0.18.0 macOS application. The repository contains readable
TypeScript implementations spanning Electron, host, coordinator, local
execution, protocol, model-routing, tool/MCP, and renderer boundaries.

It is **not** Anysphere's original monorepo and is not an official Grok Bot
release. The upstream repository is archived and GitHub reports no repository
license. Treat it as a research artifact and architecture reference, not as a
production dependency or a source of code to copy into Internet Well.

## Why Internet Well cares
This repository is a high-value reference for the architectural layer Internet
Well is building around autonomous agents. Relevant patterns include:

- coordinator/host separation for long-running agent work;
- provider-independent inference routing;
- Cursor, Claude Code, Codex, and OpenRouter adapters;
- a shared tool/MCP execution loop across providers;
- local usage accounting and provider activity tracking;
- optional Docker-isolated execution;
- explicit desktop RPC/protocol boundaries;
- settings, secrets, authentication, plugin lifecycle, and sandbox ownership;
- deterministic packaging and verification of a complex agent runtime.

These patterns map naturally to Internet Well primitives such as
`Coordinator`, `AgentRuntime`, `ModelRouter`, `ProviderAdapter`, `ToolRegistry`,
`Sandbox`, `TaskGraph`, `Checkpoint`, and `Evaluator`.

## When to use
- Designing Internet Well's agent-runtime and orchestration architecture.
- Comparing provider-routing abstractions and tool-execution loops.
- Studying coordinator/host boundaries for autonomous coding agents.
- Designing sandbox ownership, local execution, MCP routing, and provider
  fallback behavior.
- Creating clean-room specifications, tests, interfaces, and architectural
  decision records derived from observed behavior and public documentation.

## When not to use
- Do not vendor, fork, redistribute, or copy reconstructed source into a
  commercial product without independent rights review.
- Do not treat inferred module names or boundaries as authoritative upstream
  implementation facts.
- Do not use the packaged shipped renderer or preserved installer artifacts as
  Internet Well dependencies.
- Do not treat the repository as maintained software; it was archived by its
  owner shortly after publication.

## Evidence
- GitHub repository metadata identifies the project as an unofficial
  reconstruction of Grok Bot 0.18.0 and reports `license: null` `[V]`.
- Repository README describes readable Electron, host, coordinator,
  local-execution, protocol, and renderer boundaries `[V]`.
- README documents inference routing for Cursor, Claude Code, Codex, and
  OpenRouter, while preserving Grok Bot MCP/tool execution `[V]`.
- README documents an optional local Docker sandbox and loopback-bound local
  execution path `[V]`.
- README expressly states that this is a hacking/research project rather than
  Anysphere's original monorepo and that inferred names/boundaries may differ
  from upstream source `[V]`.
- GitHub metadata observed 2026-08-29 reports the repository archived `[V]`.

## Security findings
- The project deals directly with authenticated provider sessions, secrets,
  local execution, plugins, MCP tools, and Docker; adopting code from it would
  create a large trust and supply-chain surface `[I]`.
- Provider adapters and tool loops are valuable to study, but Internet Well
  should preserve its own permission model, secret isolation, allowlists,
  sandbox boundaries, audit logging, and human-approval gates `[I]`.
- Never inherit upstream authentication/session assumptions without a fresh
  threat model and end-to-end security review `[I]`.

## Legal / licensing findings
- GitHub exposes no repository license. Absence of a license means no general
  permission should be assumed to copy, modify, redistribute, or incorporate
  the repository's code into Internet Well `[I]`.
- The project itself states that it reconstructs behavior and boundaries from
  a publicly shipped application and preserves upstream installers/rendered
  assets as research inputs. Those facts materially increase provenance and
  intellectual-property risk for downstream code reuse `[V/I]`.
- Internet Well should therefore use a **clean-room pattern-extraction rule**:
  study architecture, interfaces, behavior, tests, and public descriptions;
  write independent specifications; then implement original code without
  copying reconstructed implementation text or bundled upstream artifacts.
- Any decision to redistribute or incorporate source from this repository
  requires separate legal review.

## Internet Well adoption policy
**Research-only architectural reference.** Do not install or import as a runtime
dependency. Do not mirror its source tree. Do not ingest preserved installers
or proprietary renderer artifacts into Internet Well.

Approved extraction targets:

1. Coordinator ↔ host responsibility boundaries.
2. Provider-independent model-routing interface design.
3. Shared MCP/tool execution contracts.
4. Sandbox lifecycle and execution isolation concepts.
5. Task-state, transcript, streaming, and reaction/event abstractions.
6. Usage/cost telemetry interfaces.
7. Provider adapter conformance tests.
8. Deterministic verification and packaging concepts.

All extracted mechanisms should be documented as independently implemented
Internet Well primitives with source provenance retained in architectural notes.

## Required human review
Any use beyond architecture study, including copying source, adapting a
specific implementation, redistributing artifacts, or shipping code derived
from this repository.

## Score notes
Architecture/reference value 19/20 · Documentation 9/10 · Reproducibility 8/10 ·
Security posture 12/20 · Maintenance 2/15 · License 0/10 · Provenance 8/10 ·
Integration value 14/15 → **72/100**, experimental/research-only due to absent
license, reconstructed provenance, and archived status.
