# Internet-Well — The Founder OS Agent Brain

> **Developer Preview v0.4.0.** Internet-Well is a privacy-first, evidence-backed decision layer for founders and connected AI agents. It performs local assessment, governed capability selection, implementation planning, structural evaluation, and supervised integration. It is not a penetration test, legal opinion, compliance certification, production approval, or autonomous authority to take high-impact actions.

Internet-Well answers a higher-level question than a normal repository catalog: **given the outcome I want, what capability do I need, which governed resource is the best fit, why, under what restrictions, and how should it be verified?**

## v0.4 Agent Brain

The v0.4 architecture adds a universal agent-facing brain over Internet-Well's existing repositories, skills, APIs, runtimes, and governance records.

```text
Founder / Agent Goal
        ↓
Intent + capability decomposition
        ↓
Unified capability graph
        ↓
Evidence ranking + policy restrictions
        ↓
Repo / Skill / API / MCP / Runtime selection
        ↓
Composed bundle
        ↓
Implementation plan
        ↓
Evaluation + runtime verification
        ↓
Human approval where required
```

The machine-readable graph is `integrations/agent-brain/capability-graph.json`. Composed architectures are in `bundles/agent-brain-bundles.json`.

## Install

Use a tagged release or an explicitly reviewed commit:

```bash
python3 -m pip install .
internet-well --version
internet-well-brain list-tools
```

## Connect an AI agent

Internet-Well exposes a provider-neutral stdio server:

```bash
internet-well-brain serve
```

It supports MCP-style JSON-RPC methods for `initialize`, `tools/list`, `tools/call`, and `ping`. The server exposes:

- `find_capability`
- `recommend_stack`
- `find_api`
- `get_skill`
- `plan_implementation`
- `evaluate_bundle`

A client launches it conceptually as:

```json
{
  "command": "internet-well-brain",
  "args": ["serve"]
}
```

See [`docs/AGENT-BRAIN.md`](docs/AGENT-BRAIN.md) and [`integrations/agent-brain/mcp.json`](integrations/agent-brain/mcp.json).

## Use the Brain directly

```bash
internet-well-brain find-capability "persistent autonomous agent"
internet-well-brain recommend-stack "build a production legal AI intake app"
internet-well-brain find-api "currency exchange data"
internet-well-brain get-skill "Apple motion and accessibility"
internet-well-brain plan "build an autonomous research agent"
internet-well-brain evaluate
```

The router selects outcomes and capabilities before tools. If no exact composed bundle matches, it falls back to ranked capability candidates rather than inventing a stack.

## Evidence ranking

Every Agent Brain resource can carry evidence dimensions for:

- provenance;
- maintenance;
- documentation;
- license clarity;
- security posture;
- interoperability;
- runtime evidence;
- reversibility.

Popularity, star count, marketplace position, and social-media attention are not approval criteria. Tier A remains human-controlled.

## Composed bundles

Internet-Well now includes governed bundles for:

- autonomous agents;
- autonomous trading research;
- production web apps;
- native iOS;
- legal AI;
- UAT/product testing;
- research agents;
- memory/persistence;
- browser automation.

The autonomous-trading bundle is research/simulation/paper-trading by default. Internet-Well does not grant broker credentials or live trading authority.

## Evaluation laboratory

Run:

```bash
internet-well-brain evaluate
```

The structural lab verifies that bundle resources resolve, restricted references are excluded from default bundles, evidence is present, and verification criteria exist. Product-specific runtime claims still require fixtures, staging, or production-equivalent testing.

## Continuous upstream verification

Internet-Well never silently changes immutable pins.

```bash
internet-well-upstreams
internet-well-upstreams --network --output upstream-verification.json
```

A scheduled GitHub Actions workflow checks upstream reachability and produces an upgrade-candidate report. Any material upstream change still requires provenance, license, security, compatibility, fixture, and rollback review.

## API discovery

The governed `public-apis/public-apis` integration lets agents search for external capability providers without treating directory membership as permission or proof of free/unlimited access.

```bash
internet-well-api-discovery show
internet-well-api-discovery install-source --approve
internet-well-api-discovery find "currency"
internet-well-api-discovery plan-use "Frankfurter"
```

Before adoption, verify provider identity, pricing/free tier, quotas, rate limits, authentication, TLS, terms, privacy, CORS, availability, and data quality. **Never use leaked, copied, or third-party credentials to avoid charges or limits.**

## Autonomous agent systems

Governed agent-system integrations include persistent loops, event-driven execution, adaptive reward selection, memory, orchestration, and related research resources. Use:

```bash
internet-well-agent-systems list
internet-well-agent-systems show autonomous-loop
internet-well-agent-systems plan flywheel
internet-well-agent-systems install memory --approve
```

Restricted adversarial references such as `qwen38-uncensored` are reference-only and are excluded from default Agent Brain routing.

## Vibe Coder Intelligence

Internet-Well also includes governed integrations for Anthropic Agent Skills, skills.sh, Agent Browser, Get Shit Done, Taste Skill, Humanizer, Storyscope, React Bits, Anime.js, Shader Gradient, Jitter, Refero, 10x App Builder, Ponytail, ComposioHQ Awesome Claude Skills, Microsoft Playwright MCP, and Apple Design Skills.

Examples:

```bash
internet-well-integrations list
internet-well-ponytail show
internet-well-apple-design list-skills
internet-well-apple-design plan
```

Apple Design Skills are a community interpretation layer. Current official Apple Human Interface Guidelines and platform documentation outrank community guidance when they conflict.

## Privacy-first local assessment

Internet-Well's original assessment functions remain available and operate locally by default:

```bash
mkdir -p "$HOME/.internet-well/reports"

internet-well assess /path/to/project \
  --classification private \
  --format markdown \
  --output "$HOME/.internet-well/reports/assessment.md"

internet-well plan /path/to/project \
  --goal "prepare a safe public launch" \
  --classification private \
  --format markdown \
  --output "$HOME/.internet-well/reports/plan.md"
```

Private reports should remain outside public repositories. Read [`docs/PRIVACY-AND-DATA-HANDLING.md`](docs/PRIVACY-AND-DATA-HANDLING.md) before assessing proprietary, regulated, privileged, or personal data.

## Authority boundaries

Internet-Well can read, analyze, compare, rank, route, evaluate, and plan without granting itself authority to change external systems. Explicit authorization is required before installation, repository writes, deployments, infrastructure changes, credential use, purchases, account changes, external communications, destructive actions, live trading, or other state-changing operations. Qualified human review remains required where the risk, law, policy, or evidence tier demands it.

## Repository map

- [`START-HERE.md`](START-HERE.md) — founder and agent entry point.
- [`AGENTS.md`](AGENTS.md) — mandatory agent operating contract.
- [`FOUNDER-OS.md`](FOUNDER-OS.md) — architecture and operating model.
- [`integrations/agent-brain/capability-graph.json`](integrations/agent-brain/capability-graph.json) — unified capability graph.
- [`integrations/agent-brain/mcp.json`](integrations/agent-brain/mcp.json) — agent connection descriptor.
- [`bundles/agent-brain-bundles.json`](bundles/agent-brain-bundles.json) — composed architectures.
- [`docs/AGENT-BRAIN.md`](docs/AGENT-BRAIN.md) — Agent Brain usage and governance.
- [`integrations/api-discovery/public-apis.json`](integrations/api-discovery/public-apis.json) — governed API-discovery source.
- [`integrations/agent-systems/wassim-agent-systems.json`](integrations/agent-systems/wassim-agent-systems.json) — governed autonomous-agent systems.
- [`integrations/vibe/`](integrations/vibe/) — governed skill/design/runtime integrations.
- [`registry/`](registry/) — verified resources, limitations, licenses, and evidence.
- [`governance/`](governance/) — human-review and supply-chain controls.
- [`.github/rulesets/main-protection.json`](.github/rulesets/main-protection.json) — declarative intended `main` protection policy; GitHub repository settings remain the enforcement authority.

## What Internet-Well does not guarantee

Internet-Well cannot guarantee a bug-free launch, universal compliance, secure deployment under every configuration, profitability, virality, accurate market prediction, successful trading, or correct real-world outcomes. Static and structural evaluation cannot replace runtime testing, qualified professional review, or monitoring.

## Public release posture

Version `0.4.0` is intended for supervised public developer use, governed capability routing, agent/MCP planning integrations, local repository assessment, and evidence-backed third-party resource selection. It is not autonomous production modification authority or a professional certification service.

## License

Internet-Well uses a split licensing model:

- **Software code and executable configuration:** Apache License 2.0. See [`LICENSE`](LICENSE).
- **Original documentation and governance prose previously published under CC-BY-4.0:** those permissions are not revoked; file-specific notices control where present.
- **Third-party resources:** retain their own upstream licenses and terms. Cataloging or integrating a resource does not relicense it.
