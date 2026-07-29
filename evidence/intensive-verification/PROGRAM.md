# Internet-Well Intensive Verification Program

## Goal

Move every repository discovered by the deep-research program through a visible, evidence-backed lifecycle. Nothing is silently treated as approved, and nothing disappears into an untracked list.

## Lifecycle

```text
research-candidate
  -> identity-and-license-verified
  -> exact-pin-selected
  -> security-and-maintenance-reviewed
  -> sandbox-tested
  -> registry-promoted-or-rejected
  -> bundle-wired
  -> regression-tested
  -> periodically-reverified
```

## Final-stage definition

Internet-Well is not "final" because every candidate was copied into the registry. It reaches a release-ready stage when:

1. every catalog entry has an explicit disposition: promoted, restricted, experimental, rejected, superseded, or fixture-only;
2. every promoted executable resource has an exact pin, license finding, security finding, reproducible test evidence, limitations, and human-review gate;
3. every high-risk capability has a bundle, playbook, product fixture, and regression test;
4. the selector prefers validated registry records and discloses candidate-only recommendations;
5. no local link, schema, registry reference, safety gate, generated index, or verification workflow is stale or broken;
6. every unresolved evidence gap appears in a machine-readable completion report;
7. Tier A remains impossible without competent human review.

## Workstreams

### Completed foundation

- Founder OS operating contract, project assessment, capability routing, adoption planning, and verification architecture.
- Candidate catalog and executable project/resource selector.
- Product, stack, playbook, bundle, skill, schema, and fixture foundations.
- Tranche 01: document ingestion and agent frameworks.
- Tranche 02: security and software-supply-chain baseline.

### Active

- Promote all passing Tranche 02 resources into registry records.
- Wire the definitive security baseline bundle and selector preference.
- Produce catalog-to-registry completion reporting.

### Planned verification tranches

1. **Identity and authorization:** Supabase Auth, Auth.js, Better Auth, Keycloak, OpenFGA, SpiceDB, Ory Kratos, Ory Hydra, Zitadel, Casbin.
2. **Observability and reliability:** OpenTelemetry, Prometheus, Grafana, Langfuse, Phoenix, Uptime Kuma, Sentry-compatible options, Restic, pgBackRest.
3. **AI evaluation and safety:** Inspect AI, Promptfoo, Ragas, DeepEval or alternatives, guardrail and prompt-injection systems.
4. **Infrastructure and deployment:** OpenTofu, Pulumi, Ansible, Helm, Argo CD, Coolify, Docker, Cloudflare, AWS, Vercel, Railway.
5. **Browser and agent automation:** Playwright, Playwright MCP, Browser Use, OpenHands, Aider, MCP SDKs and reference servers.
6. **Data, search, and document systems:** Supabase/Postgres, Qdrant, MarkItDown, Unstructured, local-model and serving systems.
7. **Legal, compliance, accessibility, and privacy:** Presidio, ScanCode, ORT, axe-core, docassemble, CourtListener, eyecite, Catala, relevant standards.
8. **Trading and financial research:** LEAN, Freqtrade, Hummingbot, NautilusTrader, paper-trading and backtest validation controls.
9. **Complete reference applications:** Appsmith, NocoDB, Cal.com, Activepieces, MiroFish, OpenHands, and other full-system references.
10. **Founder functions:** product discovery, marketing, support, finance, operations, incident response, cost control, and launch governance.

## Promotion rules

- Exact pin and primary evidence are mandatory.
- `tested: true` requires a recorded execution test at that pin.
- A passing install is not sufficient for containment-sensitive tools.
- Source-available licenses that are not OSI-approved are rejected from the open-source registry and may be documented separately as restricted alternatives.
- Overlapping scanners, agent frameworks, auth systems, observability stacks, and deployment systems must have explicit selection criteria.
- Every promoted record must state when not to use it.
- Every high-risk record must name required human review.

## Release gates

Before the Founder OS v2 PR is ready for review:

- main registry and Founder OS CI are green;
- all verification-tranche workflows referenced by promoted records are green;
- generated registry index is current;
- completion report has no structurally invalid entries;
- candidate-only resources are never represented as approved;
- draft PR body accurately states verified, pending, and unverified scope.
