---
name: Places To Post Your Startup
category: marketing
subcategory: launch-distribution
status: approved-with-restrictions
tier: B
human_reviewed: false
type: reference-implementation
canonical_repo: https://github.com/mmccaff/PlacesToPostYourStartup
website: https://www.placestopostyourstartup.com
pinned_version: 1941a95f344d90ea5ffe2e0b4c25ffa92dfd3d73 (2026-08-29)
license: CC0-1.0
score: 79
confidence: medium
tested: not-applicable
last_verified: 2026-09-19
---

# Places To Post Your Startup — launch-channel seed directory

## What it does
A maintained public directory of startup-launch and discovery destinations, including relevant subreddits and websites. Internet-Well uses it as a **candidate source for channel discovery**, not as proof that every listed destination is active, appropriate, free, effective, or safe.

## When to use
- Building a launch/distribution shortlist for a new product, feature, beta, open-source project, or founder announcement.
- Expanding beyond a single launch platform by discovering directories, communities, review sites, startup databases, and product-discovery channels.
- Seeding a structured channel inventory that an agent will subsequently verify and rank against the product's audience and launch objective.

## When not to use / restrictions
- Do not bulk-post, spam, scrape behind authentication, evade moderation, or automate submissions contrary to platform rules.
- Do not treat inclusion in the upstream list as a recommendation, endorsement, active listing, or evidence of channel quality.
- Verify each destination's current URL, submission rules, pricing, geographic scope, content requirements, account requirements, moderation rules, and data practices before use.
- Community promotion must match the destination's rules and disclosure requirements; do not disguise advertising as organic participation.
- Never submit confidential, privileged, embargoed, or unreleased information without authorization.

## Evidence
- Upstream repository is public and not archived as of 2026-09-19 `[V]`.
- The upstream README organizes destinations into Reddit communities and websites and states that the GitHub repository is mirrored to placestopostyourstartup.com `[V]`.
- The repository's root LICENSE is CC0 1.0 Universal `[V]`.
- Verified upstream commit: `1941a95f344d90ea5ffe2e0b4c25ffa92dfd3d73`, dated 2026-08-29 `[V]`.
- The upstream list contains heterogeneous third-party destinations; their availability, terms, prices, and suitability can change independently of the directory `[I]`.

## Validation results
The source identity, pin, license, repository status, and README structure were inspected. Individual third-party destinations were **not** exhaustively revalidated in this pass; destination-level verification is required at planning time.

## Security findings
The source is data/reference content rather than executable software. Primary risks arise from following third-party links, account creation, credential handling, uploads, and automated posting on destination platforms.

## Legal / licensing findings
The upstream list is released under CC0-1.0. Third-party destination names, trademarks, terms, submission content, and hosted services retain their own rights and rules. CC0 on the directory does not grant permission to violate a destination's terms or intellectual-property rights.

## Installation
No runtime installation is required. Internet-Well may inspect the pinned repository or materialize a normalized local channel inventory after approval. Do not treat the upstream README as a live API.

## Agent integration
Use with `skills/experimental/launch-distribution/SKILL.md`. The agent should:
1. derive the target audience and launch objective;
2. identify candidate destinations from the pinned source;
3. verify each candidate against current primary-source rules;
4. classify each candidate by channel type, audience, submission mechanism, cost, moderation risk, geography, and expected effort;
5. produce a human-reviewable launch plan before any external posting.

## Required human review
A person must approve the final destination shortlist and every external submission or account action. Legal/brand review is required for regulated claims, endorsements, contests, comparative advertising, or use of protected marks.

## Score notes
Functional quality 16/20 · Security posture 17/20 · Maintenance health 12/15 · Documentation/usability 8/10 · License suitability 10/10 · Reproducibility/testing 8/10 · Professional provenance 4/10 · Integration readiness 4/5 → **79**
