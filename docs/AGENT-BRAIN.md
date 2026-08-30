# Internet-Well v0.4 Agent Brain

Internet-Well v0.4 turns the repository from a collection of governed resources into a decision layer that agents can query directly.

## What the Agent Brain does

The Agent Brain accepts a goal or capability request and returns:

- the best-matching governed bundle;
- required capabilities;
- preferred repositories, skills, APIs, runtimes, or MCP resources;
- evidence-weighted ranking;
- restrictions and approval boundaries;
- verification requirements;
- a reversible implementation plan.

It does **not** silently install dependencies, deploy code, call third-party APIs, place trades, use leaked credentials, or assign Tier A approval.

## CLI

```bash
internet-well-brain find-capability "persistent autonomous agent"
internet-well-brain recommend-stack "build an autonomous research agent"
internet-well-brain find-api "currency exchange data"
internet-well-brain get-skill "Apple motion and accessibility"
internet-well-brain plan "build a production legal AI intake app"
internet-well-brain evaluate
```

## MCP / stdio connection

Run:

```bash
internet-well-brain serve
```

The server implements dependency-free JSON-RPC over stdio for the MCP methods used by Internet-Well:

- `initialize`
- `tools/list`
- `tools/call`
- `ping`

Exposed tools:

- `find_capability`
- `recommend_stack`
- `find_api`
- `get_skill`
- `plan_implementation`
- `evaluate_bundle`

The transport descriptor is in `integrations/agent-brain/mcp.json`.

### Example client configuration

Conceptually, clients should launch:

```json
{
  "command": "internet-well-brain",
  "args": ["serve"]
}
```

Exact configuration syntax differs across Codex, Claude, Cursor, OpenHands, Grok-compatible clients, and other MCP hosts. Internet-Well intentionally keeps the server provider-neutral.

## Capability graph

`integrations/agent-brain/capability-graph.json` is the unified machine-readable graph. Every node declares:

- resource identity and kind;
- capabilities;
- restrictions;
- source/pin where applicable;
- evidence dimensions.

Ranking weights cover provenance, maintenance, documentation, license clarity, security posture, interoperability, runtime evidence, and reversibility. Popularity alone receives no ranking weight.

## Router

The router maps natural-language goals to composed bundles in `bundles/agent-brain-bundles.json`.

Current bundles include:

- autonomous agent;
- autonomous trading research;
- production web app;
- brand/design system;
- native iOS;
- legal AI;
- UAT/product testing;
- research agent;
- memory/persistence;
- browser automation.

If no exact bundle matches, the router falls back to capability ranking rather than inventing a stack.

### Brand/design-system boundary

The `brand-design-system` bundle composes brand.yml, the stable DTCG token
format, Style Dictionary, Lucide, Fontsource, Color.js, SVGO, and Storybook.
It covers the full implementation surface but does not establish originality,
trademark availability, font or asset rights, accessibility conformance, or
production approval. Follow [`BRAND-SYSTEM.md`](BRAND-SYSTEM.md), replace all
starter values, test generated outputs and production manifests, and retain a
named human approver.

## Evaluation laboratory

`internet-well-brain evaluate` performs structural checks over every bundle:

- all referenced resources resolve;
- restricted resources are excluded from default bundles;
- verification requirements exist;
- required capabilities exist;
- evidence scores are present.

This proves graph/bundle integrity only. Product-specific runtime claims still require fixtures, staging, or production-equivalent testing.

## Evidence ranking

Resource ranking uses a weighted evidence score plus query/capability matching. The score is a prioritization aid, not a certification.

Tier A remains human-controlled. High-impact legal, financial, regulated, production-write, credential-bearing, or irreversible actions require explicit authorization and appropriate qualified review.

## Upstream verification

Use:

```bash
internet-well-upstreams
internet-well-upstreams --network --output upstream-report.json
```

The weekly workflow generates an upstream report. Internet-Well never silently changes immutable pins. A changed upstream becomes an **upgrade candidate**, which must pass provenance, license, security, compatibility, fixture, and rollback review before adoption.

## Autonomous trading boundary

The `autonomous-trading-research` bundle is intentionally research/simulation/paper-trading by default. Internet-Well does not grant broker access or live execution authority. Live trading requires a separate deployment decision, broker authorization, risk limits, monitoring, auditability, kill switches, and any applicable compliance review.

## Restricted resources

Restricted references such as `qwen38-uncensored` are excluded from default ranking and default bundles. They remain reference-only for authorized adversarial/safety evaluation and cannot be automatically installed or executed by Internet-Well.
