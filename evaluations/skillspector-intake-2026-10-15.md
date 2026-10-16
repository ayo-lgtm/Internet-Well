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

## Follow-up: per-skill scans

Conclusion 1 above recommended scanning each skill directory instead of whole
repositories. This section reports that re-run.

### Method

- Same scanner build and flags (`--no-llm`, JSON). One scan per directory
  containing a `SKILL.md`, including hidden `.agents/`, `.claude/`, and `.bolt/`
  skill folders, with a 600-second timeout per scan.
- Directories whose `SKILL.md` is byte-identical to one already scanned were
  skipped. `morluto/rea` was limited to its public `reverse-engineer-anything`
  skill; its three maintainer-only skills were excluded.
- 274 skill directories were scanned in total.

### Results

| Repository | Skills scanned | SAFE | CAUTION | DO_NOT_INSTALL | Complete scans | Critical | High |
|---|---|---|---|---|---|---|---|
| `Anionex/agent-vision-toolkit` | 1 | 0 | 0 | 1 | 0/1 | 1 | 4 |
| `calesthio/OpenMontage` | 92 | 10 | 63 | 19 | 12/92 | 3 | 222 |
| `dmtrKovalenko/fframes` | 1 | 0 | 1 | 0 | 0/1 | 0 | 0 |
| `jub0t/WolfCut` | 1 | 0 | 1 | 0 | 0/1 | 0 | 0 |
| `latent-spaces/brag` | 2 | 0 | 2 | 0 | 0/2 | 0 | 0 |
| `LearnPrompt/awesome-seedance` | 15 | 12 | 3 | 0 | 12/15 | 0 | 2 |
| `morluto/rea` | 1 | 0 | 1 | 0 | 0/1 | 0 | 0 |
| `scenario-labs/skills` | 144 | 47 | 48 | 49 | 49/144 | 2 | 169 |
| `sergebulaev/linkedin-skills` | 12 | 10 | 1 | 1 | 10/12 | 5 | 2 |
| `stackblitz/bolt-slides` | 1 | 0 | 1 | 0 | 0/1 | 0 | 0 |

Not in the table:

- `feitangyuan/onetake` keeps its single skill at the repository root, so the
  whole-repository result above already is its per-skill result
  (`DO_NOT_INSTALL`, 96 HIGH, 15.3% coverage).
- `sergebulaev/linkedin-skills` also has a root-level `SKILL.md`. Its root scan
  is the whole-repository result above.
- Both YouMind skills (`ai-image-prompts-skill`,
  `nano-banana-pro-prompts-recommend-skill`) timed out at 600 seconds. Treat
  them as **not scanned**.

### Spot-check of the new HIGH and CRITICAL findings

| Finding | Location | Assessment |
|---|---|---|
| YR1 YARA `agent_skill_credential_exfiltration_webhook` (CRITICAL ×3) | OpenMontage `heygen`, `create-video`, `avatar-video` skills, `references/webhooks.md` | **False positive.** The file documents registering a webhook with HeyGen's own API, using the user's `HEYGEN_API_KEY`, and an ngrok tunnel for local testing. The rule matched the keyword mix (`process.env`, `fetch(`, `curl -X POST`, `ngrok.io`), not a key sent to a third party. |
| P2 Hidden Instructions (85) | OpenMontage `hyperframes-animation` example HTML | **False positive.** Ordinary HTML comments describing animation timing. |
| AE1 analysis-evasion (95 OpenMontage, 68 Scenario) | Referenced scripts and assets the scanner did not fully parse | **Coverage gap.** These mark files that were skipped or partly inspected. They are not evidence of evasion. |
| MP3 Memory Manipulation (29) | Scenario Maya skills, e.g. `references/gui-paths.md` | **False positive.** "Delete history" is a Maya modelling command. |
| TT3 Tainted flow (CRITICAL ×5) | linkedin-skills `check_config.py` copies | **Expected behaviour**, as in the whole-repo scan: the Apify token is sent to `api.apify.com`. |

### Conclusions from the per-skill run

1. **Per-skill scope makes the scores usable.** Whole-repository scans
   returned `DO_NOT_INSTALL` for 12 of 13 repositories. Per skill, most
   awesome-seedance and linkedin-skills skills return `SAFE` with complete
   coverage, and Scenario and OpenMontage spread across all three verdicts.
2. **Coverage is still the weak point.** Only 83 of 270 scans in the table
   completed fully. Skills that ship scripts or many reference files still hit
   runtime and size limits. A partial scan is still not a clean scan.
3. **No new confirmed issue.** Every spot-checked HIGH and CRITICAL finding
   from this run was a false positive, a coverage gap, or expected behaviour.
   The only confirmed issue remains Scenario's unauthenticated localhost
   code-execution bridges.
4. **Recommended use:** run SkillSpector per skill, read only HIGH and
   CRITICAL findings, check coverage first, and keep human review as the gate.
