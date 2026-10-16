---
name: REA (Reverse Engineer Anything)
category: security
subcategory: reverse-engineering
status: experimental
tier: C
human_reviewed: false
type: agent-skill
canonical_repo: https://github.com/morluto/rea
website: https://rea.tools
pinned_version: rea-agents 6.5.0 (npm, tag rea-agents-6.5.0 → commit 3b79af28e80785afce9f5998d8f03289402a1847; npm integrity sha512-C6BG7LyrAdR74mSjertM6PrxJkcNZ2bfQNOJornPo9erDEp2tyPRVYPnV5Yodr+1RqewCQla68WulXlVnveD+A==)
license: MIT (REA itself); bundled third_party submodules carry their own licenses — see THIRD_PARTY_NOTICES.md
score: null
confidence: medium
tested: false
last_verified: 2026-10-15
---

# REA — agent-driven reverse engineering MCP server and skill

## What it is
An MCP server, CLI (`rea`), and agent skill (`reverse-engineer-anything`)
that lets a coding agent inspect shipped artifacts without source: native
binaries (through Hopper, Ghidra, or IDA), JavaScript/Electron apps and ASAR
archives, Android APKs (bring-your-own JADX), .NET/NativeAOT assemblies,
firmware images (bring-your-own Binwalk/Unblob), packet and HAR/SAZ
captures, signal recordings, and live user-owned browser or Electron
sessions. Results are returned as Evidence records with stated limitations.

The repository also ships three maintainer-only skills (`rea-tool-design`,
`rea-ci-tests-audit`, `rea-changelog-update`) that are for developing REA
itself and are not relevant to Internet-Well routing.

## When to use
- Security research, malware and incident analysis, vulnerability research
  and coordinated disclosure on software the founder owns or is authorized
  to examine
- Auditing a third-party dependency, SDK, or vendor binary the founder has
  the right to analyze (interoperability, supply-chain due diligence)
- Debugging the founder's own shipped build when source and artifact may
  have diverged
- CTFs and education
- Static JavaScript/Electron inspection with
  `analyze_javascript_application` — needs no native engine

## When not to use / restrictions
- **Not default-routable.** Route to REA only when the goal explicitly
  requires analysis of a shipped artifact and the founder confirms legal
  authority over the target.
- **Do not** use it to reproduce a competitor's feature from its binary.
  Upstream's headline pitch ("see a feature you like … build a version for
  your project") conflicts with Internet-Well's design-resource rule against
  reproducing protected expression, and with license/EULA anti-reverse-
  engineering clauses. Derive principles from public documentation instead,
  and get legal review before any clean-room reconstruction.
- **Do not** use it to circumvent DRM, license checks, anti-cheat,
  authentication, bot protection, or AI-provider controls — upstream's own
  DISCLAIMER.md prohibits these uses, and so does Internet-Well.
- Runtime tools (Frida instrumentation, GDB, Electron Inspector, browser
  scenario capture) execute or attach to the target. Run them only on
  isolated hosts, against test accounts, with browser-agent controls from
  `governance/AGENT-SKILL-SUPPLY-CHAIN.md`.
- Ordinary source-repository analysis: use normal repository tools (the
  upstream skill says the same).

## Supply-chain intake (governance/AGENT-SKILL-SUPPLY-CHAIN.md)
- **Canonical source/owner:** github.com/morluto/rea (user `morluto`);
  npm package `rea-agents`; website rea.tools. Upstream warns that
  look-alike repositories exist — verify the owner before any install.
- **Exact pin:** release 6.5.0 as above. The skill file was reviewed at
  repository `main` commit 40f73f62bc3acf8b444dbafba1b8ed0aef6dd641
  (skill `metadata.version: "42"`), which is newer than the 6.5.0 tag;
  re-review the skill at the pinned tag before adoption.
- **Install method:** `npx skills add morluto/rea` (skill text only) or
  `npx rea-agents setup` (writes MCP registration into the chosen agent's
  config with backups, installs the bundled skill, and can optionally
  install Hopper). `install.sh` is a `curl | bash` installer — do not use.
- **Scripts/hooks:** `package.json` defines `prepare` and `prepack` scripts;
  third-party code arrives as git submodules (jadx-headless-mcp, binwalk,
  unblob, ghidra-nativeaot, wakaru). Native bridges launch Ghidra/Hopper/IDA
  and Java processes.
- **Remote code at execution time:** the skill instructs agents to run
  `npx -y rea-agents@latest …` for diagnostics, setup, and CLI fallbacks.
  That is unpinned remote code — a prohibited default. Internet-Well use
  must replace `@latest` with `@6.5.0` (or a later reviewed pin).
- **Permissions:** setup writes agent configuration (Claude Code, Codex,
  Cursor, Gemini CLI, and others); analysis reads arbitrary local paths
  the caller supplies; firmware extraction writes to a caller-chosen
  directory; runtime tools attach to processes and browsers.
- **Network/telemetry:** analysis is documented as local. A source grep at
  the reviewed commit found no telemetry SDK `[M]` — not verified at
  runtime. `npx` contacts the npm registry.
- **Data handling:** target binaries and Evidence stay local per upstream;
  the connected agent's model provider still receives whatever tool output
  the agent reads — treat proprietary or regulated targets accordingly.
- **Bridge security:** Hopper/Ghidra bridges use per-session random
  capability tokens over current-user Unix sockets (Windows: authenticated
  loopback TCP with a restricted DACL) `[C]` — SECURITY.md.
- **Update/rollback:** pin the npm version; setup keeps configuration
  backups and an `uninstall` command exists; remove the skill directory to
  roll back a skill-only install.
- **Maintenance:** very active — 6.3.0 → 6.5.0 tags and a 2026-10-14 npm
  publish observed; release-please changelog. Rapid churn means the
  skill and tool list will drift from this record quickly.

## Evidence
- MIT license `[V]` — LICENSE file at reviewed commit
- npm `rea-agents@6.5.0`, modified 2026-10-14, integrity above `[V]` —
  `npm view` on 2026-10-15
- Tag `rea-agents-6.5.0` → `3b79af2…` `[V]` — `git ls-remote` on 2026-10-15
- Skill content, routing table, and setup/approval guidance `[V]` — read
  `.agents/skills/reverse-engineer-anything/SKILL.md` at `40f73f6`
- Responsible-use restrictions `[V]` — DISCLAIMER.md at `40f73f6`
- Runtime behavior, output quality, and baseline benefit `[U]` — not
  executed

## Validation results
Not execution-tested. Nothing from the upstream repository was installed,
built, or run during intake: the repository was cloned shallowly into an
isolated scratch directory and read only. `npx skills add` and
`npx rea-agents setup` were deliberately not run.

Before promotion beyond experimental, run the matched-baseline evaluation
from the supply-chain governance doc: a fixture Electron app and a small
fixture native binary the evaluator owns, agent with vs. without REA,
pinned `rea-agents@6.5.0`, network egress observed, and every state-
changing action inspected.

## Legal / licensing findings
- REA code is MIT. Bundled submodules have separate licenses; check each one
  in THIRD_PARTY_NOTICES.md before redistribution. Hopper and IDA are commercial products with their own
  terms; Ghidra is Apache-2.0.
- The legality of reverse engineering depends on jurisdiction and on the
  target's license/EULA. That is the founder's responsibility and needs
  legal review for any target the founder does not own.

## Installation (only after explicit authorization)
Skill text only, pinned to a reviewed commit:
`npx skills add morluto/rea` — then confirm the installed `SKILL.md`
matches the reviewed commit.

MCP server: run `npx -y rea-agents@6.5.0 setup --client claude_code --dry-run --json`
first, review the proposed paths and backups, then apply the same scope
only after approval. Do not pass `--install-hopper` unless that separate
purchase/installation was approved.

## Required human review
Legal authority and license/EULA review for every target the founder does
not own; approval before any setup that writes agent configuration; approval
before runtime instrumentation or browser actions; review before any
reconstruction work informed by analysis output.

## Score notes
Not scored: the record is unexecuted, so functional and reproducibility
dimensions have no evidence. Provisional observations — Provenance strong
(official owner, tagged releases, npm integrity hash), License
clean for REA itself, Security pending the `@latest` remote-execution
default and the dual-use runtime surface.
