# Rejected Candidates

Preserved with evidence so future agents and researchers do not
re-recommend them. **Rejection here means "fails this registry's
genuinely-free-and-open-source criterion (METHODOLOGY §6),"** not that the
software is bad — several entries below are excellent products whose
license simply disqualifies them from an open-source registry. Where noted,
limited use may still be reasonable for a founder who accepts the terms;
that is an individual commercial decision, outside this registry's scope.

All license texts below were read directly from the canonical repositories
on 2026-07-23.

---

## Terraform (HashiCorp/IBM)
- **Repo:** github.com/hashicorp/terraform
- **License:** BUSL-1.1 `[V]` — LICENSE file names "Business Source
  License 1.1", licensor IBM, for Terraform ≥1.6.0
- **Why rejected:** Not open source (fails OSD; production-use field
  limitation). The Additional Use Grant prohibits products competing with
  IBM/HashiCorp's paid offerings; each version converts to MPL-2.0 only
  after four years `[V]`.
- **Registry alternative:** OpenTofu (MPL-2.0) —
  `registry/devops/opentofu.md` — Terraform-language-compatible, Linux
  Foundation stewardship. Terraform ≤1.5.x remains MPL-2.0 but is
  unmaintained — rejected on abandonment grounds for security-relevant
  infrastructure tooling.

## Sentry (self-hosted)
- **Repo:** github.com/getsentry/sentry
- **License:** FSL-1.1-Apache-2.0 `[V]` — "Functional Source License 1.1,
  Apache 2.0 Future License"; prohibits offering the software (or
  substantially similar functionality) as a competing product/service;
  each release converts to Apache-2.0 after two years `[V]`
- **Why rejected:** Not open source at release time (competing-use field
  restriction). Note: Sentry relicensed BSD-3-Clause → BSL → FSL over its
  history — a canonical license-drift example.
- **Notes for founders:** Self-hosting Sentry for your *own* error
  tracking is permitted by the FSL and many founders reasonably do it; it
  simply cannot sit in an open-source registry. Sentry's SDKs (client
  libraries) are separately MIT-licensed `[C]` — verify per SDK if you
  adopt them. Phase 2 will validate an open-source error-tracking
  alternative (GlitchTip, Bugsink candidates).

## n8n
- **Repo:** github.com/n8n-io/n8n
- **License:** Sustainable Use License 1.0 (fair-code, not open source)
  `[V]` — internal business use only; distribution only free-of-charge and
  non-commercial `[V]`
- **Why rejected:** Fails OSD (commercial redistribution prohibited).
  Frequently mislabeled "open source" in listicles — the exact promotional
  pattern this registry exists to catch.
- **Notes:** Internal workflow automation on your own instance is within
  its terms; embedding n8n in your product is not (requires commercial
  license). Phase 2 open-source alternatives to validate: Activepieces
  (verify current license carefully — has open-core structure), Windmill
  (AGPL core, verify), Huginn (MIT).

## Invoice Ninja (v5)
- **Repo:** github.com/invoiceninja/invoiceninja
- **License:** Elastic License 2.0 `[V]` — no offering as hosted/managed
  service; license-key functionality must not be removed `[V]`
- **Why rejected:** Not open source (OSD-failing service and license-key
  restrictions).
- **Notes:** Phase 2/3 will validate open invoicing alternatives (e.g.
  Crater status check, or invoice generation via hledger + templates).

---

## Rejection pattern worth naming

Four for four above are **relicensing or fair-code events on formerly (or
nominally) open projects**. Practical rules derived:

1. Never trust a repo badge, README claim, or listicle — read LICENSE at
   the pinned version you intend to use.
2. Watch for open-core markers: `enterprise/` directories (Chatwoot,
   handled — see its record), per-file `@license` headers (Twenty,
   handled), "editions" language.
3. Re-verify licenses on every major-version upgrade; license changes ride
   majors.
