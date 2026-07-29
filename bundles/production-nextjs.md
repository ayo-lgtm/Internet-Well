# Bundle: Production Next.js

## Outcome

Prepare a Next.js application for reliable production operation with secure server boundaries, tested critical journeys, accessible UI, observable failures, and reversible deployment.

## Required capabilities

Type and build validation, unit and browser testing, accessibility, authentication and authorization testing, input validation, secrets and dependency scanning, headers and caching review, observability, deployment previews, rollback, and incident response.

## Recommended resource set

- browser and critical journeys: Playwright;
- unit and component testing: Vitest plus React Testing Library where component behavior needs direct coverage;
- accessibility: axe-core integrated into Playwright and focused manual keyboard/screen-reader review;
- authentication: Auth.js when it fits the identity model; Keycloak only for enterprise identity needs;
- authorization: application-native checks first, OpenFGA or SpiceDB only for genuinely complex relationship authorization;
- secrets: Gitleaks;
- dependencies: OSV-Scanner and Trivy where containers or broader filesystem scanning are present;
- telemetry: OpenTelemetry or platform-native observability, not both by default;
- uptime: Uptime Kuma for a lightweight founder-run baseline;
- AI features: Promptfoo or Inspect AI plus Langfuse only when the application actually uses AI.

## Selection rules

Apply `stacks/nextjs.md` and deployment-stack guidance. Reuse adequate existing systems. Prefer validated registry entries over catalog candidates and choose the smallest compatible set. Do not add an enterprise identity, policy, or observability platform to a simple product without a demonstrated requirement.

## Implementation order

1. identify routes, server actions, APIs, middleware, data, and critical journeys;
2. establish clean install, type, lint, build, and unit checks;
3. add browser and accessibility coverage;
4. verify authentication, authorization, secrets, dependencies, headers, caching, and error boundaries;
5. validate preview deployment, telemetry, alerting, rollback, and incident ownership.

## Verification

Run clean install, type, lint, production build, API tests, authenticated browser journeys, keyboard and accessibility checks, secret and dependency scans, header inspection, preview tests, provider failures, and rollback. Verify server-only secrets never enter client bundles.

## Human review

Security, accessibility, privacy, domain, and operations reviewers must approve production authentication, sensitive data, material claims, infrastructure, and unresolved launch risk. Catalog-only entries require promotion or explicit supervised exception before adoption.
