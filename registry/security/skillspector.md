---
name: SkillSpector
category: security
subcategory: agent-skill-security-scanning
status: experimental
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/NVIDIA/SkillSpector
website: https://docs.nvidia.com/skills/scanning-agent-skills
pinned_version: v2.12.0 (tag commit c7958a3268d9498644b22edb75d0f051bbc8cbfc); evaluated build is main 240421219409dc0bafef9f618a10d80c2d7e83a3, which reports itself as 2.12.0
license: Apache-2.0
score: null
confidence: medium
tested: true
last_verified: 2026-10-15
---

# SkillSpector — pre-install security scanner for agent skills

## What it does
Scans an agent skill (directory, zip, single `SKILL.md`, URL, or Git repo)
before installation and returns findings, a 0–100 risk score, a severity,
and a recommendation (e.g. `CAUTION`). It has two stages: static analysis
(71 patterns in 17 categories, including prompt injection, data exfiltration,
privilege escalation, supply chain, MCP rug-pull and tool poisoning, AST
dangerous-code checks, taint tracking, and YARA signatures) and an optional
LLM semantic pass. Outputs: terminal, JSON, Markdown, SARIF.

Published by NVIDIA as part of its Verified Skills pipeline.

## Why Internet-Well cares
`governance/AGENT-SKILL-SUPPLY-CHAIN.md` requires every skill to be reviewed
for scripts, hooks, permissions, network access, and prompt-injection
resistance before recommendation. SkillSpector automates the first pass of
that intake. It is the intended pre-adoption gate for every skill candidate
in `catalog/screenshot-resources.json`.

## When to use
- Before installing or recommending any third-party agent skill or MCP server
- In CI, with `--format sarif` and `--fail-on-findings`, on repositories
  that vendor skills
- To produce a baseline so later re-scans surface only new findings

## When not to use / restrictions
- **A clean or low score is not approval.** It is a static triage signal;
  human review of the skill's instructions and scripts is still required.
- Run with `--no-llm` by default. The optional LLM pass sends skill content
  to the configured OpenAI-compatible endpoint (NVIDIA's build.nvidia.com
  by default) and needs an API key — that is a new external provider and
  needs explicit authorization, especially for private skills.
- The SC4 dependency check sends dependency names and versions (not file
  contents) to OSV.dev even with `--no-llm`. If OSV.dev is unreachable it
  silently falls back to a small bundled list, so CVE coverage drops.
- Leave optional LangSmith tracing (`LANGCHAIN_TRACING_V2`) off.
- Upstream classifies the project as Development Status 3 – Alpha.

## Validation results (sandboxed run, 2026-10-15)
- Installed from a shallow clone at main `2404212` into an isolated
  Python 3.12 venv with `uv pip install .`; `skillspector --version` →
  `SkillSpector v2.12.0`. No upstream installer scripts were used.
- All scans ran `skillspector scan <dir> --no-llm -f json`, with no API keys
  set. OSV.dev returned 403 through this environment's egress proxy, so SC4
  used the bundled fallback list; dependency-CVE results are therefore
  incomplete.
- Scanned 13 skill candidates; results and spot-checks are in
  [evaluations/skillspector-intake-2026-10-15.md](../../evaluations/skillspector-intake-2026-10-15.md).
  Repository-level scans saturated: 12 of 13 scored 100 / `DO_NOT_INSTALL`,
  8 of 13 reached 0% full coverage because of runtime, size, and
  executable-content limits, and spot-checked HIGH findings were mostly
  documentation or prompt-text false positives. It did surface one real
  issue (unauthenticated localhost code-exec bridges in Scenario's DCC
  skills). Scan individual skill directories rather than whole repositories.
- Per-skill follow-up (274 skill directories, same flags): scores become
  usable (most awesome-seedance and linkedin-skills skills return `SAFE` with
  complete coverage), but only 83 of 270 tabulated scans completed fully, two
  skills timed out at 600 s, and every new HIGH/CRITICAL finding spot-checked
  was a false positive, a coverage gap, or expected behaviour.
- Not yet done: matched-baseline comparison against manual review, false-
  positive rate measurement, and LLM-pass evaluation.

## Security findings
- Large dependency surface (LangChain/LangGraph, OpenAI, boto3, google-auth,
  yara-python); pin and scan the scanner's own dependencies before CI use.
- Vulnerability reports go to NVIDIA PSIRT, not public GitHub issues
  (SECURITY.md).

## Legal / licensing findings
Apache-2.0. Upstream notes that installation pulls third-party open-source
dependencies whose licenses must be reviewed.

## Installation
`uv tool install 'git+https://github.com/NVIDIA/SkillSpector.git@v2.12.0'`
or, from a reviewed clone, `uv venv && uv pip install .`. Add the `[mcp]`
extra only if `skillspector mcp` is needed.

## Agent integration
`skillspector scan <path> --no-llm -f json -o report.json`, then read
`risk_assessment`, `analysis_completeness` (check `coverage_percent` and
`status` — a partial scan is not a clean scan), and `issues`.

## Required human review
Every finding at HIGH or CRITICAL; any decision to enable the LLM pass;
suppression baselines.

## Score notes
Not scored yet: execution-tested for function, but false-positive rate and
benefit over manual review are unmeasured. Provisional: provenance strong
(NVIDIA org, tagged releases), license clean, OSV/LLM egress documented.
