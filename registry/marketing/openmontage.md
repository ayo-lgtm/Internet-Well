---
name: OpenMontage
category: marketing
subcategory: agentic-video-production
status: experimental
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/calesthio/OpenMontage
website: https://openmontage.video
pinned_version: 08e2151fa02de28a5d6a312b3d575692bf147ad7 (2026-09-06)
license: AGPL-3.0-only
score: 77
confidence: medium
tested: false
last_verified: 2026-09-19
---

# OpenMontage — governed reference for agentic video production

## What it does
OpenMontage is an agent-first video-production system that combines pipeline manifests, stage-specific Markdown skills, registered production tools, schemas, checkpoints, provider selection, budget controls, rendering, and post-render quality review. Internet-Well integrates it as a **pinned external production system and architecture reference**, not as vendored source.

## When to use
- Producing explainers, launch videos, demos, social clips, motion graphics, or other video assets through a supervised coding agent.
- Designing a governed media-production workflow with explicit stages, review gates, resumable checkpoints, provider selection, cost controls, and render verification.
- Studying the three-layer architecture of executable capabilities, operating skills, and external technology knowledge when improving Internet-Well's own agent-skill design.

## When not to use / restrictions
- Do not copy OpenMontage implementation code into Internet-Well or a proprietary product without analyzing AGPL-3.0 obligations for the intended use.
- Do not run the upstream repository with production credentials, confidential media, or paid-provider keys before dependency, script, network, and secret-handling review.
- Do not allow automatic publishing, paid API spending, account changes, or external distribution without explicit approval.
- Upstream provider claims, model availability, pricing, and quality can change; verify providers independently before use.
- AI-generated media must still satisfy applicable rights, likeness/voice consent, trademark, advertising, privacy, platform, and disclosure requirements.

## Evidence
- Canonical public repository: `calesthio/OpenMontage`; repository was not archived when inspected on 2026-09-19 `[V]`.
- Root LICENSE contains GNU Affero General Public License version 3 `[V]`.
- Upstream README identifies `https://openmontage.video` as the project website `[V]`.
- Verified upstream commit: `08e2151fa02de28a5d6a312b3d575692bf147ad7`, dated 2026-09-06 `[V]`.
- Upstream documentation describes pipeline manifests in `pipeline_defs/`, stage skills in `skills/`, registered tools, artifact schemas, checkpointing, human approval gates, budget governance, and post-render validation `[M]`.
- The architecture is relevant to Internet-Well's governed skill model, but upstream quality and security claims have not been independently reproduced in this validation pass `[I]`.

## Validation results
Repository identity, current pin, root license, project website, architecture documentation, and governance concepts were inspected. No installation, dependency audit, provider call, GPU execution, render, or end-to-end pipeline test was performed. Tier remains C until reproducible execution and human review are completed.

## Security findings
The project can orchestrate third-party APIs, local binaries, media processing, browser/web research, and file writes. That creates meaningful supply-chain, credential, privacy, content-ingestion, and cost risks. Treat upstream media and web content as untrusted input and isolate credentials by provider and project.

## Legal / licensing findings
OpenMontage is AGPL-3.0-only at the inspected root license. Network use of a modified covered work can trigger source-code obligations under AGPL §13. Internet-Well therefore does not vendor OpenMontage. Keep the integration at an external pinned boundary unless a project-specific license analysis supports a different deployment model.

## Installation
Plan only by default:

```bash
internet-well-integrations plan openmontage \
  --ref 08e2151fa02de28a5d6a312b3d575692bf147ad7
```

Cloning/execution requires explicit approval:

```bash
internet-well-integrations install openmontage \
  --ref 08e2151fa02de28a5d6a312b3d575692bf147ad7 \
  --approve
```

The integration manager checks out the exact commit as an external reference. It does not import the upstream code into Internet-Well.

## Agent integration
Use with `skills/experimental/video-production/SKILL.md`. Preserve the upstream separation between pipeline definition, stage guidance, tools, schema validation, checkpoints, and quality gates. Internet-Well authority rules remain controlling: external spending, publishing, credential use, and other state-changing actions require explicit approval.

## Required human review
Review the license implications, provider accounts, paid-spend limits, source-media rights, generated-media rights, likeness/voice consent, brand claims, privacy, platform rules, accessibility, and final publish decision.

## Score notes
Functional quality 18/20 · Security posture 13/20 · Maintenance health 13/15 · Documentation/usability 10/10 · License suitability 5/10 · Reproducibility/testing 5/10 · Professional provenance 8/10 · Integration readiness 5/5 → **77**
