# Agent Skill Supply-Chain Governance

## Purpose

Agent skills are executable procedural dependencies. A Markdown file can influence tools, filesystem access, network calls, browser sessions, credentials, deployment behavior, and user decisions. Internet-Well therefore evaluates skills with controls comparable to code dependencies and automation workflows.

## Trust classes

1. **Official verified** — published by the platform or standards owner, exact source pinned, permissions reviewed, fixture-tested.
2. **Verified community** — independent source with confirmed license, stable maintenance, bounded permissions, reproducible benefit, and human review.
3. **Experimental** — promising but incomplete evidence, unstable behavior, or limited testing.
4. **Restricted** — useful only under specific containment, license, data, or human-review conditions.
5. **Rejected** — malicious, deceptive, legally unsuitable, unverifiable, abandoned without safe pinning, or materially worse than baseline.

Popularity, stars, install counts, testimonials, and marketplace rank do not determine trust class.

## Mandatory intake

Before installation or recommendation, record:

- canonical source and owner;
- exact commit or release;
- license for every included file;
- installation method and remote-download behavior;
- scripts, binaries, hooks, and dependencies;
- allowed tools and requested permissions;
- network access and telemetry;
- data read, written, transmitted, or retained;
- supported agents and version assumptions;
- update and rollback method;
- known security reports and maintenance status.

## Prohibited defaults

Internet-Well must not recommend by default any skill that:

- disables permission prompts or sandboxing;
- performs state-changing external actions without approval;
- reads credentials unrelated to its stated capability;
- installs unpinned remote code during execution;
- sends private code, documents, prompts, or results to an undisclosed service;
- impersonates a person or conceals material authorship where disclosure is required;
- copies protected designs, brands, or content;
- modifies production, financial, legal, medical, employment, or identity systems without qualified review.

## Evaluation method

Each skill evaluation must include a matched baseline:

1. Define a fixture repository and acceptance criteria.
2. Run the agent without the skill.
3. Run the same agent and model with the skill.
4. Compare correctness, completion, regressions, token use, time, and cost.
5. Inspect every state-changing action.
6. Test prompt-injection and malicious repository-content resistance.
7. Test compatibility against supported agent versions.
8. Record whether the skill provided a material benefit.

A skill that produces no measurable benefit should not be included merely because it is popular.

## Browser-agent controls

Browser skills and runtimes require:

- isolated profiles;
- hostname allowlists;
- test accounts where possible;
- secret and cookie protection;
- download quarantine;
- approval before submitting forms, sending messages, accepting terms, purchasing, publishing, deleting, applying, or changing accounts;
- auditable action logs;
- session termination and cleanup.

## Design-resource controls

Design skills and inspiration providers must:

- derive principles rather than reproduce distinctive protected expression;
- preserve project brand decisions;
- test accessibility, keyboard use, reduced motion, contrast, performance, mobile behavior, and low-end devices;
- document third-party asset rights;
- avoid dark patterns and deceptive interaction design.

## Writing-skill controls

Writing skills must preserve meaning and factual responsibility. They must not be used to fabricate personal experience, invent a person's voice without authorization, conceal plagiarism, evade required AI disclosure, or replace qualified legal or professional review.

## Reverification

Reverification is required after:

- upstream ownership or license changes;
- significant releases;
- new scripts, binaries, permissions, or network destinations;
- agent-platform changes;
- security reports;
- material fixture regressions;
- twelve months, whichever occurs first.
