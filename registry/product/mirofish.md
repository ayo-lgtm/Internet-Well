---
name: MiroFish
category: product
subcategory: multi-agent-decision-simulation
status: experimental
tier: C
human_reviewed: false
type: reference-implementation
canonical_repo: https://github.com/666ghj/MiroFish
website: https://mirofish.ai
pinned_version: v0.1.2 (released 2026-03-07)
license: AGPL-3.0-only
score: 62
confidence: medium
tested: false
last_verified: 2026-07-29
---

# MiroFish — multi-agent simulation reference implementation

## What it does

MiroFish is a multi-agent simulation system that turns uploaded seed material
and a natural-language prediction question into a simulated environment and a
structured report. Its documented workflow includes graph construction,
entity and relationship extraction, persona generation, simulation, report
generation, and post-simulation interaction. `[V]`

The project presents itself as a general prediction engine. Internet-Well does
**not** validate that claim. The defensible use is narrower: MiroFish is a
reference implementation for scenario rehearsal, stakeholder modeling, and
multi-agent decision simulation. `[I]`

## When to use

- Study an end-to-end architecture for evidence ingestion, entity graphs,
  stakeholder personas, agent memory, simulation rounds, and report synthesis.
- Run supervised experiments where outputs are treated as hypotheses rather
  than forecasts.
- Design an independent, smaller decision-simulation capability with clear
  evidence boundaries and uncertainty labels.
- Explore how policy, product, communications, or operational decisions could
  affect different modeled stakeholders.

## When not to use (and restrictions)

- Do not treat simulation output as a reliable prediction of legal, political,
  financial, safety, regulatory, or market outcomes.
- Do not deploy as a closed-source hosted service without specialist review of
  AGPL obligations and directly integrated dependency licenses.
- Do not ingest confidential, privileged, regulated, or personal data until the
  complete data flow, model-provider terms, Zep configuration, retention, and
  deletion behavior have been reviewed.
- Do not rely on generated personas as evidence about real people or groups.
- Do not copy MiroFish source or prompts into proprietary projects merely to
  avoid designing an independent implementation.

## Evidence

- `[V]` Official repository README at the pinned release describes graph
  building, environment setup, simulation, report generation, and interactive
  exploration.
- `[V]` The official repository identifies OASIS as the simulation engine and
  requires an OpenAI-compatible LLM endpoint plus Zep configuration for the
  documented setup.
- `[V]` The root `LICENSE` at `v0.1.2` is GNU Affero General Public License v3.
- `[V]` GitHub releases identify `v0.1.2`, released 2026-03-07, as the latest
  tagged release verified for this record.
- `[C]` The repository is active and widely adopted on GitHub, but popularity
  does not validate prediction accuracy, security, or production readiness.
- `[R]` Open project discussions identify concerns around grounding, production
  execution, and licensing boundaries. These require independent verification.

Primary sources:

- https://github.com/666ghj/MiroFish
- https://github.com/666ghj/MiroFish/releases/tag/v0.1.2
- https://github.com/666ghj/MiroFish/blob/v0.1.2/LICENSE

## Validation results

Metadata, release, README workflow, and root-license checks completed on
2026-07-29. No installation or simulation run was performed. The documented
runtime requires external model access and Zep configuration, and simulation
cost and behavior vary with the selected provider and round count.

Status remains `experimental`, Tier C, until a pinned, isolated execution test
and output-quality evaluation are documented.

## Security findings

- Uploaded source material and generated graph/persona data may pass through
  external model and memory services depending on configuration.
- Seed documents are untrusted inputs. Any derived agent skill must neutralize
  prompt instructions embedded in uploaded documents before those documents are
  used for persona, configuration, or report generation.
- Generated profiles and reports can appear authoritative even when several
  layers are model-generated.
- This review does not verify authentication, authorization, tenancy, deletion,
  encryption, rate limiting, dependency vulnerabilities, or deployment defaults.

## Legal/licensing findings

MiroFish is licensed under `AGPL-3.0-only` at the pinned release. Network use of
modified AGPL-covered software can trigger source-offer obligations. MiroFish
also identifies OASIS as an integrated simulation engine; dependency and
combined-work obligations must be reviewed before commercial deployment.

For a proprietary Founder OS, the preferred approach is to study general
architectural ideas and independently implement original schemas, prompts,
orchestration, and interfaces. This record is not a legal opinion and does not
resolve whether a particular integration forms a covered combined work.

## Installation

Documented upstream prerequisites include Node.js 18+, Python 3.11–3.12, `uv`,
an OpenAI-compatible LLM endpoint, and Zep configuration. Upstream documents
source and Docker startup paths. Installation has not been reproduced by
Internet-Well at this pin.

## Agent integration

Treat MiroFish as a reference architecture, not an install-on-demand agent
skill. A future Internet-Well decision-simulation skill should be independently
written and should:

1. separate sourced facts from generated assumptions;
2. constrain the number and authority of simulated stakeholders;
3. record evidence provenance for every material premise;
4. run adversarial and uncertainty reviews;
5. label results as scenario analysis, not prediction;
6. require human approval before external actions; and
7. avoid confidential inputs unless the complete data path is approved.

## Required human review

- Open-source counsel review before hosted or proprietary commercial use.
- Security and privacy review before processing real organizational data.
- Domain-expert review of every high-impact simulation conclusion.
- Human confirmation that generated personas do not misrepresent actual people
  or protected groups.

## Score notes

- Functional quality: 14/20 — coherent architecture; prediction validity unproven.
- Security posture: 8/20 — substantial unverified deployment and data-flow risk.
- Maintenance health: 13/15 — active repository and recent tagged releases.
- Documentation and usability: 8/10 — substantial setup and workflow documentation.
- License suitability: 4/10 — valid OSS license with strong network-copyleft obligations.
- Reproducibility and testing: 3/10 — no Internet-Well execution test at the pin.
- Professional provenance: 9/10 — public project with organizational support and named upstream engine.
- Integration readiness: 3/5 — usable as a reference, unsuitable for blind integration.
- **Total: 62/100**
