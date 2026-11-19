# Catalog addition — 2026-11-19

**Change:** one candidate appended to `catalog/curated-repositories.json` (153 → 154 entries). Nothing else modified. Per the catalog lifecycle, this is a **research candidate, not a registry approval** — admission still requires the METHODOLOGY.md pipeline (pinning, license/security review, sandboxed evaluation, human review).

## Added: AI Job Search

- **Entry:** `ai-job-search-dev/ai-job-search` — role `reference-implementation`, license `MIT`, readiness `production`, risk `high-employment`, recommendation `job-application-agent-reference`; capabilities: job-fit-evaluation, tailored-cv-generation, cover-letter-drafting, application-tracking, interview-preparation, prompt-injection-guarding.
- **Source of the lead:** URL supplied directly by the founder (2026-11-19).
- **Verified 2026-11-19 (primary source, read-only shallow clone):**
  - Public repository; HEAD `d2afe00bfc9b7be8ffc2ee41acc22570970b76d4` committed 2026-11-19 — actively maintained `[V]`.
  - LICENSE read directly — MIT, © 2026 Mads Lorentzen `[V]`. The README's Trendshift badge still names `MadsLorentzen/ai-job-search`, i.e. the repo was moved to the `ai-job-search-dev` org; recheck provenance if the org changes again.
  - Latest release tag `v2.0.0` (commit `745e6770dbcfb524ee245c89be0ff8df95924919`); upstream recommends tagged weekly releases over raw `master` `[V]`.
  - It is a Claude Code *template*, not a library: you fork/copy it and run slash commands (`/setup`, `/scrape`, `/apply`, `/rank`, `/interview`, `/outcome`, `/gmail-sync`, `/notion-sync`, …). Requires Claude Code (paid), Python 3.10+, LaTeX; Bun for optional portal CLIs `[V]`.
  - **Human-in-the-loop on submission:** `/apply` drafts but never submits; `/outcome` follow-ups are "draft only, never send"; `/gmail-sync` proposes changes for approval `[V]` (command files).
  - **Security posture is unusually explicit** (SECURITY.md): posting integrity gate (`tools/posting_guard.py`) against hidden text / injected instructions, no hooks shipped, deny-list for exfil-shaped commands, CI-enforced `security_guards.py`, portal manifests barred from lifecycle scripts. It openly states it is **not a sandbox** and that WebFetch is domain-unrestricted `[V]`.
- **Vendor claims, not independently audited:** author's outcome story (69 applications → 20 interviews → 1 hire) `[C]`; "never fabricates skills or experience" `[C]` — an instruction-level guarantee, not a verified property.

## Why it fits the Well

A well-documented, governance-aware reference for an agentic job-application workflow (drafter/reviewer split, deterministic PDF/ATS checks, untrusted-input handling). It pairs naturally with the FreeHire candidate (`strelov1/freehire`, which AI Job Search already supports via a `freehire-search` portal skill) and is a design reference for the first-party JobPilot fixture.

## Risk notes and when not to use

- **`high-employment`:** processes personal and employment data (CV, history, salary expectations) alongside untrusted web content. Prompt-injection risk is narrowed, not eliminated.
- **Privacy footgun:** forks of a public repo are public, and `/setup` writes personal data into tracked files — use a **private copy**, never a fork, for real searches.
- **Third-party portal CLIs** (`community-portals`, separate repo) and `install_portal_clis.py` (`bun install`) are unreviewed upstream code — review each before running; out of scope of this entry.
- Gmail/Notion connectors grant access to a mailbox/workspace; treat as new-provider data processing requiring explicit authorization.
- Not for: bulk/automated application spam, auto-submission, or misrepresenting candidate experience.

## Upstream test run — 2026-11-19 (authorized by the founder)

Tag `v2.0.0` (`745e6770dbcfb524ee245c89be0ff8df95924919`), Python 3.13.18, isolated venv with CI's pins only (`pyyaml`, `openpyxl==3.1.5`); mirrors the Python jobs in `.github/workflows/ci.yml`.

| Check | Result |
|---|---|
| `tools/lint_skills.py` | OK — 3 skills, 12 commands, settings.json |
| `tools/check_framework_version.py` | OK |
| `tools/security_guards.py` | OK — permissions/hooks allowlists, gitignore rules, package manifests, skill/command allowed-tools, agent tools |
| `python -m unittest discover -s tests -t .` | **957 tests, OK, 1 skipped** (`test_refuses_out_inside_repo_spelled_in_another_case`: needs a case-insensitive filesystem) |

Working tree unchanged after the run. **Not run:** the Bun/TypeScript CI jobs (portal typecheck), the Windows leg, and any end-to-end `/setup`/`/scrape`/`/apply` session — those need Claude Code, LaTeX, network access and personal data. A passing unit suite is not evidence that the agent workflow is correct or that its prompt-injection defenses hold against real postings.

## Not done

No portal CLIs or `bun install`; no registry record, bundle, or capability-graph node was created.
