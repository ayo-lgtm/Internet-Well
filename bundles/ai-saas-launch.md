# Bundle: AI SaaS Launch

## Outcome

Prepare an AI-powered SaaS product for a controlled public launch with evidence across value, AI quality, security, privacy, accessibility, reliability, and operations.

## Required capabilities

Project intelligence, critical-journey testing, AI evaluation, prompt-injection testing, abstention and fallback, secrets detection, dependency scanning, authorization testing, privacy mapping, accessibility, observability, backups, incident response, rollback, and launch governance.

## Recommended resource set

Prefer validated registry records where present. Candidate-only resources must remain labeled unverified until promoted through `METHODOLOGY.md`.

- browser and critical journeys: Playwright;
- TypeScript tests: Vitest; Python tests: pytest;
- accessibility: axe-core;
- secrets: Gitleaks, with TruffleHog only when live-secret validation is justified and AGPL review is complete;
- dependency and container risk: Trivy and OSV-Scanner;
- AI evaluation: Inspect AI for high-assurance evaluation, Promptfoo for rapid eval and red-team workflows;
- AI observability: Langfuse, after provider and retention review;
- model routing: LiteLLM only where multi-provider fallback and cost control are required;
- startup platform: Supabase where compatible;
- infrastructure: OpenTofu where infrastructure as code is justified;
- monitoring: Prometheus or a simpler platform-native option; do not add duplicate telemetry stacks;
- backup: Restic or database-native backup with a demonstrated restore path.

## Selection rules

Apply `profiles/ai-saas.md` and detected stack guides. Prefer existing project tools when adequate. Select by capability, registry status, compatibility, license, data flow, and operational burden. Tier C and catalog-only tools remain supervised. Never select multiple overlapping observability, agent, or evaluation systems without a documented need.

## Implementation order

1. project assessment and critical journeys;
2. architecture, model providers, prompts, retrieval, and data flows;
3. deterministic tests and CI;
4. AI evaluation, red teaming, abstention, and provider-failure behavior;
5. security, authorization, privacy, and secrets controls;
6. accessibility;
7. deployment, monitoring, backup, incident response, and rollback;
8. launch-readiness verdict.

## Verification

Run critical journeys, adversarial AI evaluations, authorization and tenant tests, data-flow checks, accessibility tests, production build, preview deployment, provider failures, restore, rollback, and alert delivery. Record exact versions, fixtures, commands, failures, and unverified claims.

## Human review

Domain, security, privacy, legal, accessibility, and operations review are required for high-impact AI, regulated data, production access, material claims, and launch blockers. Candidate-only catalog entries cannot be treated as approved by an agent.
