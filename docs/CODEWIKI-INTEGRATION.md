# CodeWiki integration

## Purpose

Internet-Well should use CodeWiki as a documentation and onboarding layer, not as its decision authority.

Internet-Well remains responsible for:

- project assessment;
- capability-gap analysis;
- evidence status;
- resource selection;
- licensing and risk restrictions;
- human-review gates;
- implementation and verification policy.

CodeWiki may provide:

- repository-level documentation;
- architecture and sequence diagrams;
- code-linked explanations;
- searchable onboarding material;
- natural-language codebase questions;
- regenerated documentation after repository changes.

## Supported approaches

### Hosted Google Code Wiki

Use for public repositories or approved private-repository workflows where the operator accepts the provider, data-flow, access-control, and retention model.

Before connecting a private repository, document:

- repository classification;
- secrets and regulated-data exposure risk;
- provider data use and retention;
- who may query the generated wiki;
- repository revocation and deletion process;
- whether generated text may be republished.

### Open-source CodeWiki research implementation

Evaluate as a self-hosted or controlled alternative. Promotion into the validated registry requires an exact release or commit pin, license review, reproducible installation, supported-language tests, documentation-faithfulness tests, and resource-cost measurements.

## Generated documentation contract

Every generated wiki must clearly distinguish:

1. **Verified repository facts** — linked to exact files, functions, schemas, tests, and commits.
2. **Inferences** — architecture or intent inferred from code and labeled as inference.
3. **Product decisions** — sourced from ADRs, product profiles, or explicit founder instructions.
4. **Unknowns** — unresolved questions rather than invented explanations.

Generated documentation must not silently override `AGENTS.md`, ADRs, security policies, legal decisions, product exclusions, or human-reviewed registry evidence.

## Recommended user journey

1. A founder connects or uploads a repository.
2. Internet-Well assesses the product, stack, risk, and missing context.
3. CodeWiki generates the navigable technical map.
4. Internet-Well overlays risks, verified resources, implementation order, and human-review requirements.
5. The user can ask:
   - What does this system do?
   - Where is authentication enforced?
   - What handles user data?
   - Which files implement the critical journey?
   - Which recommendations are verified versus candidate-only?
   - What must be fixed before launch?
6. Changes trigger documentation regeneration and Internet-Well re-verification.

## Safety requirements

- Never expose secrets to a documentation provider.
- Never treat generated documentation as proof of runtime behavior.
- Never publish private architecture without authorization.
- Never allow generated docs to make legal, security, compliance, or launch approvals.
- Require source links for material technical claims.
- Mark stale documentation when the documented commit differs from the current repository head.

## Internet-Well integration target

A future `internet-well docs` command should emit a provider-neutral documentation manifest containing:

- repository and commit;
- entry points;
- architecture areas;
- critical journeys;
- important files;
- data stores and external services;
- security boundaries;
- unresolved questions;
- required diagrams;
- prohibited disclosures;
- refresh trigger.

Hosted or self-hosted documentation systems can consume that manifest without becoming the source of truth for Internet-Well decisions.
