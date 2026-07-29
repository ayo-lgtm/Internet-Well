# Bundle: Production Next.js

## Outcome

Prepare a Next.js application for reliable production operation with secure server boundaries, tested critical journeys, accessible UI, observable failures, and reversible deployment.

## Required capabilities

Type and build validation, unit and browser testing, accessibility, authentication and authorization testing, input validation, secrets and dependency scanning, headers and caching review, observability, deployment previews, rollback, and incident response.

## Selection rules

Apply `stacks/nextjs.md` and deployment-stack guidance. Reuse adequate existing test and monitoring systems. Select the smallest compatible registry bundle and avoid adding tools that duplicate framework or platform capabilities without evidence.

## Implementation order

1. identify routes, server actions, APIs, data, and critical journeys;
2. establish type, lint, build, and unit checks;
3. add browser and accessibility coverage;
4. verify auth, secrets, dependencies, headers, caching, and errors;
5. validate preview deployment, monitoring, rollback, and incidents.

## Verification

Run clean install, type, lint, production build, API tests, authenticated browser journeys, keyboard and accessibility checks, secret and dependency scans, header inspection, preview tests, provider failure, and rollback.

## Human review

Security, accessibility, privacy, domain, and operations reviewers must approve production authentication, sensitive data, material claims, infrastructure, and unresolved launch risk.
