# Agent Skills

Packaged agent skills (prompt + procedure + tool bindings) that operate on
this registry or implement its workflows. Skills follow the same lifecycle
as registry records:

- [`approved/`](approved/) — validated skills safe for routine agent use
- [`experimental/`](experimental/) — under evaluation; human supervision
  required on every run
- [`deprecated/`](deprecated/) — superseded or failed skills, kept with
  reasons (mirror of the rejected-records principle)

## Bar for approval

A skill entry requires everything a registry record requires (evidence,
license of any embedded third-party content, `last_verified`) **plus**:

1. **Prompt-injection review** — the skill must state which untrusted
   inputs it touches (web content, issue text, README text) and how
   instructions embedded in them are neutralized.
2. **Permission boundary** — explicit list of tools/credentials the skill
   may use; anything mutating (sending, deleting, deploying, signing)
   requires human approval in the loop.
3. **Reproducible evaluation** — at least one documented eval run
   (see `../evaluations/`) demonstrating the skill does what it claims.

## Current state (honest)

**No skills are approved yet.** The registry's workflows
(`../workflows/`) are the human-readable precursors; packaging them as
skills, with evals, is future work. Nothing will be listed here without
meeting the bar above.
