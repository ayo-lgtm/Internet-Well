---
name: OWASP Threat Dragon
category: security
subcategory: threat-modeling
status: approved
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/OWASP/threat-dragon
website: https://owasp.org/www-project-threat-dragon/
pinned_version: v2.6.2 (2026-05-10)
license: Apache-2.0
score: 75
confidence: medium
tested: false
last_verified: 2026-07-23
---

# OWASP Threat Dragon — threat modeling diagrams and threat catalogs

## What it does
Draws data-flow diagrams and records threats/mitigations per element using
STRIDE and similar methodologies. Available as a web app (with GitHub/GitLab/
Bitbucket storage integration) and desktop builds (Windows/macOS/Linux).

## When to use
- A solo founder's first structured threat model before launch, and reviews
  after architecture changes
- Storing threat models as JSON in the product repo, versioned with code

## When not to use
- Automated threat generation at scale (it is a documentation/diagramming
  aid, not an analyzer — the threat quality is only as good as your input)
- Teams needing enterprise workflow/reporting (out of scope)

## Evidence
- License Apache-2.0 `[V]` — repository license indicator (2026-07-23)
- Latest release v2.6.2, 2026-05-10 `[V]` — repository releases
- OWASP "Production" project status `[M]` — OWASP project page claim
- Version 2.x (Vue.js) active; 1.x explicitly maintenance-mode `[V]` — repo
  README
- Maintainer base is small relative to the scanners in this tranche `[I]` —
  from visible contributor activity; treat bus-factor as moderate risk

## Validation results
- Not execution-tested this pass (desktop/web app; Phase 2 candidate).
  Versioned desktop installers and a Dockerized web app are documented `[V]`

## Security findings
- Web-app mode stores models in your repo via OAuth to your git provider —
  review token scopes before use `[I]`
- Local desktop mode keeps all data local `[M]`
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- Apache-2.0 — commercial use permitted. OWASP trademark rules apply to
  implying endorsement.

## Installation
Desktop installers from GitHub releases (pin v2.6.2) or Docker image for
the web app.

## Agent integration
Threat model files are JSON — an agent can read/update them in-repo and
propose new threats for human review. Model content decisions are human.

## Required human review
All threat identification and risk-acceptance decisions; this tool
documents thinking, it does not do the thinking.

## Score notes
Functional 14/20 (documentation aid, limited automation) · Security 15/20 ·
Maintenance 11/15 (small maintainer base) · Docs 8/10 · License 10/10 ·
Reproducibility 7/10 · Provenance 8/10 (OWASP production status) ·
Integration 2/5 → **75**
