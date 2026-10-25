---
name: Conway Automaton
category: engineering
subcategory: sovereign-agent-runtime-reference
status: experimental
tier: C
human_reviewed: false
type: reference-implementation
canonical_repo: https://github.com/Conway-Research/automaton
website: https://conway.tech
pinned_version: d8f816881fd24b6f5e3d616e59edec387a447667 (2026-08-26; package 0.2.1)
license: MIT
score: 53
confidence: medium
tested: true
last_verified: 2026-10-25
---

# Conway Automaton

## What it does
TypeScript runtime for a continuously running agent that holds its own crypto wallet, pays for its own compute and inference, edits its own code, and spawns funded child agents [M]. The README describes it as needing "no human operator" [V]. Internet-Well catalogs it only as a **reference** for persistent-agent design patterns: a policy engine, spend limits, survival tiers, heartbeat scheduling, injection defense, state versioning and lineage tracking [I]. It is not a deployable founder dependency.

## When to use
Read-only study, or an authorized offline safety evaluation, of how a long-running agent constrains spending, self-modification and replication. Useful when designing guardrails for the persistent-agent and execution-orchestration work already in this repository [I]. For governed long-running work, prefer the existing Agent Brain orchestration bundles. They keep human authorization in the loop.

## When not to use
- Any default routing, bundle, or unattended deployment. It is designed to remove the human operator, which conflicts with the authorization boundaries in AGENTS.md [I].
- With real funds, real wallets, mainnet transactions, domain purchases or production accounts. Default treasury limits allow up to $50 per transfer and $250 per day without human action [V].
- Where self-replication or self-modification is unacceptable. Children get their own wallets and sandboxes, capped by `maxChildren` (default 3) [V]. Cumulative descendant spend and a lineage-wide kill switch were not verified [U].
- Where you cannot accept vendor lock-in. Compute, inference, credits, domains and x402 payments go through Conway Cloud and `conway.tech` by default [V].
- Do not treat the bundled "constitution" as an enforcement mechanism. It is prompt text plus file protection, not a verified control [I].
- Not for the `autonomous-trading-research` bundle. On-chain transfer ability does not create trading authority.

## Evidence
- [Immutable source pin](https://github.com/Conway-Research/automaton/commit/d8f816881fd24b6f5e3d616e59edec387a447667) dated 2026-08-26. That commit only edits the README. The last substantive code commits are from 2026-04 to 05 [V].
- The README says development "has continued across Conway's internal RL environments", so the public repository may lag the actual runtime [V].
- [LICENSE](https://github.com/Conway-Research/automaton/blob/d8f816881fd24b6f5e3d616e59edec387a447667/LICENSE) is MIT, © 2026 Conway [V].
- [package.json](https://github.com/Conway-Research/automaton/blob/d8f816881fd24b6f5e3d616e59edec387a447667/package.json) declares `@conway/automaton` 0.2.1 on Node ≥20. Dependencies include `viem`, `@solana/web3.js`, `siwe`, `tweetnacl`, `better-sqlite3`, `openai` and `simple-git`. Most use caret ranges, with pnpm lockfile pinning [V].
- The README documents wallet generation on first boot, API-key provisioning by Sign-In With Ethereum, ERC-8004 identity registration on Base, self-modification of its own code, tool installation and child spawning [V].
- [Default treasury policy](https://github.com/Conway-Research/automaton/blob/d8f816881fd24b6f5e3d616e59edec387a447667/src/types.ts) sets these limits [V]:
  - transfers: $50 single, $100 hourly, $250 daily;
  - x402 payments: $1 maximum, allowlist `conway.tech`;
  - inference: $500 per day;
  - human confirmation: only above $10.
- Policy rules cover authority, command safety, financial limits, path protection, rate limits and validation (`src/agent/policy-rules/`) [V]. The tests include security, injection, financial and replication suites. CI runs typecheck and tests on Node 20/22 [V]. A CI step exits 0 when vitest hangs (exit code 124), so a green CI run is weaker evidence than it looks [V]. The local run confirmed that this masks a real hang (see Validation results) [V].
- The creator CLI has `status`, `logs`, `fund` and `send` commands. No dedicated stop, kill or lineage-termination command was found [V]. Other shutdown paths were not verified [U].
- `scripts/automaton.sh` is a `curl | sh` installer. It clones the repository into `/opt/automaton` when run as root, or into `~/.automaton/runtime` otherwise [V].
- Contributor concentration: most of the recent shallow history is by a single maintainer [V]. The full history, release signing, SBOM, advisories and npm publication were not audited [U].

## Validation results
On 2026-10-25 I read the README, constitution, package metadata, installer script, CI workflow, default treasury policy, replication spawn limit, policy-rule inventory and creator CLI command list from a shallow clone.

The same day, with the user's authorization, I built and tested the pin in a disposable cloud container (transcript row 23 in `evaluations/README.md`):
- Dependencies installed with `pnpm install --frozen-lockfile` on Node 22.22.0. Only the `better-sqlite3` and `esbuild` build scripts ran; pnpm blocked the optional `bufferutil` and `utf-8-validate` scripts.
- `pnpm run typecheck` and `pnpm run build` both exited 0. `automaton --version` and `--help` and the creator CLI usage screen printed and exited.
- Each of the 64 vitest files was run separately with a 300-second cap. 63 files passed: 1,614 tests, 0 failed. They cover the policy engine, financial limits, spend tracking, injection defense, path protection, replication, the agent loop and the wallet [V].
- `context-hardening.test.ts` does not finish. Its "summarizes old turns", "preserves most recent turns" and "does not summarize when only one turn exists" tests feed 50,000–500,000-character letter-only strings to `estimateTokens`. That function calls `js-tiktoken` `cl100k_base`, which is quadratic on such input: 2k chars took 0.37 s, 8k took 5.8 s and 16k took 20.7 s. Prose, base64, hex and minified code of the same length took 40 ms or less [V].
- Run as one suite, vitest never exits. Upstream CI turns that timeout into a pass, so the CI result neither confirms nor reports this file's outcome [V].
- Tests wrote only orchestration workspace files to the scratch `HOME` (`~/.automaton/workspace`). No wallet or key files were created [V].

Not run: `--run`, `--init`, `--provision`, `--setup` or `--configure`, the `curl | sh` installer, any Conway API, inference, chain RPC or inbox network call, or any real or test wallet. Passing unit tests run against mocks and do not establish a safety, financial-loss, containment or production-readiness property. Runtime confidence stays capped at medium.

## Security findings
The runtime combines several risks:
- a self-held private key;
- autonomous payments;
- shell execution and port exposure;
- domain management;
- self-modification of code and tools;
- spawning funded children;
- agent-to-agent inbox messages, which carry untrusted content.

Any one of these needs explicit authorization under AGENTS.md. Together they create privilege-escalation and runaway-cost risk [I].

Before any evaluation, review:
- how the policy engine handles tool calls made by self-modified code;
- whether protected-file rules hold after an in-place code edit;
- where wallet keys are stored, and their file permissions;
- whether inbox messages can steer financial or replication tools;
- whether the operator can terminate every descendant.

Treat on-chain and x402 actions as irreversible.

Context building can be stalled by untrusted text. `estimateTokens` runs the quadratic tokenizer on turn inputs, thinking and tool results. A web page, file or inbox message containing a long letter-only run could stall a turn for minutes to hours. The measured cost is about 16 s for 16k characters, growing roughly 4× per doubling [V]. I did not check whether every untrusted input is truncated before it is estimated [U]. A length cap or a linear fallback estimate before tokenizing would bound this [I].

No security audit was performed.

## Legal/licensing findings
The source license is MIT [V]: commercial use is permitted if the copyright and permission notice are preserved. Conway Cloud, inference providers, domain registrars, Base/Solana networks and stablecoins each carry separate terms, fees and possibly regulatory obligations. An agent holding and moving funds may raise money-transmission, tax, sanctions and consumer-protection questions. These require qualified review and are not resolved here [I]. The "inspired by Anthropic's Claude Constitution" framing does not imply endorsement [I].

## Installation
This entry adds the record to the catalog only. It does not authorize cloning for execution, running `npm install`/`pnpm install`, piping `automaton.sh` to a shell, generating wallets, provisioning API keys, funding, or registering on-chain. If a human approves an evaluation, use:
- a disposable, network-restricted VM;
- testnet or zero-value wallets only;
- no `conway.tech` credentials;
- treasury limits set to zero, or confirmation required for every payment;
- `maxChildren` set to 0.

Inspect the installer and lockfile at the exact pin first.

## Agent integration
Reference only: no adapter, capability-graph node or bundle is enabled, and Agent Brain must not route workloads to it.
1. Define what you are evaluating (for example, spend-limit enforcement or replication caps) and observable pass/fail criteria.
2. Get explicit human approval for any execution. The scope must exclude real funds, mainnet and production systems.
3. Stub the Conway API, inference, chain RPC and inbox with local fixtures. Block outbound network access by default.
4. Test hostile inputs against the policy engine: oversized transfers, self-edits to policy files, injected inbox instructions, and attempts to replicate past the cap.
5. Show that the operator can stop the process and every descendant, and can revoke its credentials, before running any loop longer than one turn.
6. Record findings as design lessons for Internet-Well's own orchestration. Do not use the findings as grounds for adopting the runtime.
7. Recheck upstream before changing the pin. To roll back, remove this record and regenerate INDEX.md.

## Required human review
Execution of any kind needs explicit human approval: wallet creation, funding, network access, replication and self-modification. Legal and compliance review is required before anything touches real value. Promotion from tier C needs reproduced containment and spend-limit evidence plus a verified kill path for all descendants. Upstream claims alone do not justify promotion.

## Score notes
Provisional evidence score: 53/100. Reproducibility rose from 4 to 6 after the clean build and 1,614 passing tests. The hanging test file and CI's masking of the timeout keep it from going higher.

| Criterion | Score |
|---|---|
| Functional quality | 12/20 |
| Security posture | 5/20 |
| Maintenance health | 7/15 |
| Documentation/usability | 8/10 |
| License suitability | 9/10 |
| Reproducibility/testing | 6/10 |
| Professional provenance | 5/10 |
| Integration readiness | 1/5 |

Explicit policy and test scaffolding help. The score is held down by:
- an autonomy model that removes the human operator;
- default autonomous spending;
- replication;
- dependency on a single vendor's infrastructure;
- a public tree that the README says lags internal development.
