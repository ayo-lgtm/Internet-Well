# Internet-Well v0.4.0 — Agent Brain

## Release summary

v0.4.0 moves Internet-Well from a governed collection of resources into a provider-neutral Agent Brain that can route goals to capabilities, rank resources using evidence, compose governed architectures, expose planning tools over an MCP-style stdio server, run structural evaluations, and monitor upstream resources without silently changing pins.

## Major additions

### Universal agent connection layer

`internet-well-brain serve` exposes a dependency-free stdio JSON-RPC interface with tools for capability discovery, stack recommendation, API discovery routing, skill discovery, implementation planning, and bundle evaluation.

### Unified capability graph

`integrations/agent-brain/capability-graph.json` unifies repositories, skills, API discovery sources, browser runtimes, MCP resources, workflow systems, and restricted references. Ranking uses provenance, maintenance, documentation, license clarity, security posture, interoperability, runtime evidence, and reversibility.

### Automatic router

Natural-language goals route to governed bundles. If no exact bundle matches, Internet-Well returns ranked capability candidates instead of inventing an architecture.

### Composed bundles

v0.4.0 ships bundles for autonomous agents, autonomous trading research, production web apps, native iOS, legal AI, UAT/product testing, research agents, memory/persistence, and browser automation.

### Evaluation laboratory

`internet-well-brain evaluate` validates graph and bundle integrity. It verifies that resources resolve, restricted references are excluded from default bundles, evidence is present, and bundle verification criteria exist. Runtime claims still require product-specific fixtures or staging evidence.

### Continuous upstream verification

`internet-well-upstreams` generates an upstream review report. The scheduled `Verify upstream resources` workflow checks public sources and produces artifacts. Internet-Well never silently changes immutable pins; upstream changes become reviewable upgrade candidates.

### Governance hardening

- Agent operating rules now route through the Agent Brain before resource selection.
- Restricted references remain excluded from default routing and execution.
- Public API discovery explicitly prohibits use of leaked or third-party credentials.
- Autonomous-trading architecture is research/simulation/paper-trading by default.
- `.github/rulesets/main-protection.json` records the intended server-side `main` protection policy.

## Upgrade from v0.3.0

Install from the reviewed v0.4.0 source/tag and verify:

```bash
internet-well --version
internet-well-brain list-tools
internet-well-brain evaluate
```

Existing v0.3 commands remain available. New commands are:

```bash
internet-well-brain
internet-well-upstreams
```

## Compatibility and authority

v0.4.0 does not give connected agents automatic production-write authority. Installations, deployments, credentials, account changes, purchases, live trading, external communications, destructive operations, and other state-changing actions remain separately permissioned.

Tier A remains human-controlled. Evidence scores are prioritization aids, not certifications.

## Release verification

Before publishing the tag, the release candidate must pass the full Internet-Well workflow matrix, including `Verify Agent Brain`, `Verify API discovery`, core repository verification, public-repository hygiene, public launch, productization, identity/authorization, governed agent systems, and integration checks.
