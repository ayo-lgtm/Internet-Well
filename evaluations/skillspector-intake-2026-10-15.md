# SkillSpector intake scan — 2026-10-15

Static triage of the agent-skill candidates in `catalog/screenshot-resources.json`
(plus `morluto/rea`) using [SkillSpector](../registry/security/skillspector.md).

## Method

- Scanner: NVIDIA/SkillSpector main `240421219409dc0bafef9f618a10d80c2d7e83a3`
  (`skillspector --version` → 2.12.0), installed with `uv pip install .` in an
  isolated Python 3.12 venv.
- Command: `skillspector scan <repo-root> --no-llm -f json -o <report>.json`.
  No API keys were set and the LLM pass was not run.
- Targets: full shallow clones of each repository at the commit pinned in the
  catalog (rea at main `40f73f6`). The whole repository was scanned, not
  individual skill directories.
- OSV.dev returned HTTP 403 through this environment's egress proxy, so the
  dependency-CVE check (SC4) used SkillSpector's small bundled fallback list.
- Every scan exited 1 (findings present) and wrote a complete JSON report.

## Results

| Repository | Score | Verdict | Critical | High | Medium | Coverage |
|---|---|---|---|---|---|---|
| `stackblitz/bolt-slides` | 37 | CAUTION | 0 | 0 | 6 | 80.8% (partial) |
| `latent-spaces/brag` | 100 | DO_NOT_INSTALL | 0 | 5 | 29 | 97.2% (partial) |
| `LearnPrompt/awesome-seedance` | 100 | DO_NOT_INSTALL | 0 | 9 | 455 | 0.0% (partial) |
| `YouMind-OpenLab/ai-image-prompts-skill` | 100 | DO_NOT_INSTALL | 0 | 34 | 9 | 0.0% (partial) |
| `YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill` | 100 | DO_NOT_INSTALL | 0 | 25 | 10 | 0.0% (partial) |
| `feitangyuan/onetake` | 100 | DO_NOT_INSTALL | 0 | 96 | 0 | 15.3% (partial) |
| `Anionex/agent-vision-toolkit` | 100 | DO_NOT_INSTALL | 2 | 34 | 75 | 90.4% (partial) |
| `sergebulaev/linkedin-skills` | 100 | DO_NOT_INSTALL | 18 | 106 | 119 | 96.2% (partial) |
| `jub0t/WolfCut` | 100 | DO_NOT_INSTALL | 0 | 136 | 221 | 0.0% (partial) |
| `dmtrKovalenko/fframes` | 100 | DO_NOT_INSTALL | 0 | 428 | 14 | 0.0% (partial) |
| `calesthio/OpenMontage` | 100 | DO_NOT_INSTALL | 0 | 533 | 1261 | 0.0% (partial) |
| `scenario-labs/skills` | 100 | DO_NOT_INSTALL | 2 | 77 | 681 | 0.0% (partial) |
| `morluto/rea` | 100 | DO_NOT_INSTALL | 10 | 41 | 573 | 0.0% (partial) |

"Coverage" is SkillSpector's own `analysis_completeness`. A `partial` scan is
not a clean scan. At 0% coverage the score reflects only files that were
partly inspected before runtime, size, or executable-content limits stopped
analysis (`runtime_limit`, `total_bytes_limit`, `excluded_executable_content`).

## Manual spot-check of HIGH and CRITICAL findings

| Finding | Location | Assessment |
|---|---|---|
| AR2 Anti-Refusal, "Without warning" | awesome-seedance `references/cases.md` (horror-video prompt text) | **False positive.** Creative prompt wording, not an instruction to the agent. |
| AS1 Agent Config Directory Access, `~/.gemini/config` | brag `README.md`, `docs/other-agents.md` | **False positive in context.** Installation docs naming where a skill goes. |
| AE1 Incomplete referenced artifact analysis | YouMind skills `SKILL.md` → `scripts/setup.js` | **Coverage gap, not malice.** Matches the manual intake finding: `setup.js` runs on install and fetches unpinned files from the repo's `main` branch. |
| TT3 Tainted flow, env token → network | linkedin-skills `scripts/check_config.py` | **Expected behaviour.** The Apify token is sent to `api.apify.com` to validate it. Still a credential path that needs approval. |
| TT3 Tainted flow, env → `urlopen` | agent-vision-toolkit `vision_client.py`, `html_shot.py` | **Expected behaviour.** Calls a configured vision endpoint and a local port. It confirms the toolkit sends screenshots to an external model, which is a data-egress decision. |
| RA1 Self-Modification, "self-update" | WolfCut `ARCHITECTURE.md`, audit notes | **False positive.** Documentation text about the app's updater. |
| AST8 `exec(compile(...))` | rea `bridge/pwndbg/*.py` | **Expected behaviour.** Local launcher shims for the pwndbg debugger bridge. |
| AST8 `exec(compile(...))` | scenario-labs `scenario-maya-expert/scripts/mx_bridge_server.py`, `scenario-zbrush-expert/.../zb_bridge_server.py` | **Real risk.** These are unauthenticated servers on `127.0.0.1` that execute code they receive. The Maya file says so ("There is NO authentication"). Any local process can run code inside Maya or ZBrush while they are up. Only run them on a single-user machine, for the duration of a task, then stop them. |

## Conclusions

1. **Repository-level scores saturate.** Twelve of thirteen repositories scored
   100 / `DO_NOT_INSTALL`, including ones whose top findings were documentation
   false positives. At whole-repo scope the score does not separate risky
   skills from noisy ones. Next time, scan each skill directory (the folder
   containing `SKILL.md`), or use `--exclude` for docs and examples, and record
   a baseline.
2. **Coverage limits matter more than the score.** Eight of thirteen scans
   reached 0% full coverage. Treat any `partial` result as "not scanned".
3. **One confirmed issue changes a catalog entry.** Scenario's DCC expert skills
   (Maya, ZBrush) carry an unauthenticated local code-execution bridge, now
   recorded as a restriction.
4. **SkillSpector stays experimental.** It is useful for locating code paths
   worth reading, but it cannot gate installs automatically at this scope.

No candidate was installed or executed during this evaluation.
