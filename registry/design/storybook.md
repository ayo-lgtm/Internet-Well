---
name: Storybook
category: design
subcategory: component-documentation
status: approved
tier: B
human_reviewed: false
type: framework
canonical_repo: https://github.com/storybookjs/storybook
website: https://storybook.js.org
pinned_version: v10.5.10 (published 2026-08-20)
license: MIT
score: 88
confidence: medium
tested: false
last_verified: 2026-08-30
---

# Storybook — component workshop, documentation, and testing surface

## What it does
Builds, documents, and tests UI components and pages in isolation, including
hard-to-reach states; official documentation covers stories, Autodocs/MDX,
interaction testing, visual testing integrations, and accessibility tooling
`[V]`.

## When to use
- For reusable component documentation and reviewable state coverage
- To expose token usage, content rules, responsive examples, and edge cases
- With application-level end-to-end and accessibility tests

## When not to use
- As proof that the production app uses the documented component version
- As a substitute for real navigation, data, auth, performance, or device
  testing
- To publish private designs, customer data, secrets, or internal endpoints

## Evidence
- Official repository is active and MIT licensed `[V]`
- Stable release v10.5.10 published 2026-08-20 `[V]`
- Official documentation describes isolated component development, testing,
  and documentation `[V]`

## Validation results
Release, license, and documentation inspected. Framework-specific
installation was not executed because the target product stack is unknown.

## Security findings
Stories and static deployments can expose test data, internal component
states, API assumptions, source maps, or environment values. Use synthetic
fixtures, scan the built output, and apply appropriate access controls.

## Legal / licensing findings
MIT permits commercial use, modification, and redistribution subject to
notice conditions. Addons and embedded assets may have separate terms.

## Installation
Use the official initializer for the target framework only after reviewing
the proposed dependency changes, or pin the required Storybook packages to
10.5.10.

## Agent integration
Agents may generate stories for approved components and required states,
but must not invent expected business behavior. Link every automated check
to a requirement and keep production end-to-end verification separate.

## Required human review
Component API, content and visual decisions, exposed data, accessibility,
addon selection, and production parity.

## Score notes
Functional 20/20 · Security 15/20 · Maintenance 15/15 · Docs 10/10 ·
License 10/10 · Reproducibility 8/10 · Provenance 7/10 · Integration 3/5
→ **88**.
