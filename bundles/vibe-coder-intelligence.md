# Vibe Coder Intelligence Bundle

## Outcome

Help founders and AI coding agents discover and use high-value skills, design resources, browser tools, and workflow systems without blindly installing popular community artifacts.

## Required inputs

- target repository and stack;
- intended outcome;
- agent runtime;
- whether the task is local, hosted, or production-facing;
- privacy and data sensitivity;
- authorization boundaries;
- accessibility and performance requirements;
- budget and provider-lock-in tolerance.

## Required capabilities

- agent-skill discovery and authoring;
- skill supply-chain review;
- browser automation;
- long-running agent planning;
- frontend design and component selection;
- web animation and motion design;
- editorial assistance;
- hosted generator and provider review;
- accessibility, performance, privacy, license, and permission governance.

## Selection rules

1. Define the outcome before browsing a marketplace.
2. Prefer official or already verified skills.
3. Identify the minimum capability needed.
4. Inspect every skill file, script, dependency, and allowed tool.
5. Pin the source and exact version or commit.
6. Run in an isolated fixture before using a private or production repository.
7. Compare results with and without the skill.
8. Measure token cost, runtime cost, false positives, and regressions.
9. Require approval before browser actions, external communications, purchases, deployments, or account changes.
10. Record evidence and rollback instructions.

## Recommended selections

### Skill standards and discovery

- `anthropics/skills` for official examples and skill-authoring patterns.
- `vercel-labs/skills` and skills.sh for discovery only; marketplace rank is not approval.

### Browser automation

- Prefer `vercel-labs/agent-browser` when a contained CLI and compact accessibility snapshots fit the task.
- Prefer validated Playwright for deterministic end-to-end testing.
- Use Playwright MCP only under its existing high-risk browser-agent restrictions.
- Never give any browser agent unrestricted access to production credentials or financial, legal, medical, or employment accounts.

### Long-running development workflow

- Evaluate `gsd-build/get-shit-done` as a supervised planning and context-engineering system.
- Never require `--dangerously-skip-permissions` or any equivalent permission bypass.
- Internet-Well authority and evidence rules override third-party workflow instructions.

### Frontend and design

- Use `Leonxlnx/taste-skill` as an experimental design skill, not a design-quality guarantee.
- Use React Bits selectively after license, accessibility, reduced-motion, and performance review.
- Use Anime.js when a dedicated animation engine is justified.
- Use Shader Gradient and Jitter for prototypes only after provider and asset-rights review.
- Use Refero to derive general principles; do not copy exact protected branding, assets, or distinctive visual expression.

### Writing

- Use `blader/humanizer` as an editorial review aid.
- Preserve meaning, attribution, authorship, and professional responsibility.
- Never use it to fabricate a person's voice, evade disclosure obligations, or misrepresent authorship.

### Hosted generators

- Treat 10x App Builder and similar services as providers, not trusted repositories.
- Verify source-code ownership, exportability, privacy, security, app-store compliance, recurring cost, and deletion rights before use.

## Implementation order

1. Assess the target project and identify the exact capability gap.
2. Select one candidate resource, not an overlapping collection.
3. Complete provenance, license, permission, privacy, and script review.
4. Pin the exact source and create a rollback point.
5. Run a no-skill baseline against a controlled fixture.
6. Run the candidate against the same fixture and acceptance criteria.
7. Compare quality, correctness, time, cost, tokens, accessibility, and regressions.
8. Obtain required human approval.
9. Adopt in one reversible project slice.
10. Re-run integrated tests and record the evidence.

## Automatic rejection conditions

Reject or quarantine a resource when it:

- asks the user to disable permission controls;
- contains unreviewed executable scripts or remote downloads;
- requests broad filesystem, browser, credential, or network access without necessity;
- lacks a usable license or ownership terms;
- encourages copying protected designs or content;
- uploads private code or documents without clear consent;
- claims guaranteed quality, completion, virality, profit, security, or compliance;
- cannot be pinned or reproduced;
- produces no measurable improvement in a controlled comparison.

## Verification

For each selected resource, capture:

- exact source, commit, release, or provider version;
- license and commercial-use terms;
- files and scripts inspected;
- tool permissions;
- network destinations;
- fixture task and acceptance criteria;
- baseline result without the resource;
- result with the resource;
- token, time, and cost difference;
- accessibility and performance checks where relevant;
- observed failures;
- rollback procedure;
- human-review decision.

## Human review

Human review is mandatory for:

- browser sessions with authenticated accounts;
- legal, financial, medical, employment, immigration, or regulatory outputs;
- hosted providers receiving private source code or proprietary designs;
- license ambiguity;
- production deployment;
- public claims based on generated findings;
- any resource with state-changing tools.

## Completion criteria

This bundle is complete only when the selected resource is pinned, sandbox-tested, measurably useful, permission-bounded, legally usable, documented, and independently reviewable. Installation alone is not completion.
