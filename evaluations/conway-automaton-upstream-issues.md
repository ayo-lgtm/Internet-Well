# Conway Automaton — draft upstream issues

Status: **drafts, not posted.** Posting to `Conway-Research/automaton` is an external communication and needs explicit approval per AGENTS.md. Evidence: [offline run report](conway-automaton-offline-2026-10-26.md) and execution-test row 23 in [README.md](README.md). All references are to `d8f816881fd24b6f5e3d616e59edec387a447667`.

---

## 1. `maxChildren` config is ignored; spawn cap is always 3

**Where:** `src/replication/spawn.ts:71`

```ts
const maxChildren = (db as any).config?.maxChildren ?? 3;
```

The database object has no `config` property, so this always evaluates to 3. `config.maxChildren` from `automaton.json` is never read here.

**Reproduce:** set `"maxChildren": 0` in `~/.automaton/automaton.json`, then have the agent call `spawn_child` in its own turn. Policy allows it (`authority.external_tool_restriction` and `rate.spawn_daily` pass), a child row is created, and `POST /v1/sandboxes` is called. In our offline run it was called 4 times, and only the mocked API's 404 stopped it.

**Expected:** an operator who sets `maxChildren: 0` cannot spawn children.

**Suggested fix:** pass the loaded config (or the limit) into `spawnChild` instead of reading it off `db`. Add a policy rule that denies `spawn_child` when the active child count is at or above `config.maxChildren`, so the check runs before any sandbox request. Add a test with `maxChildren: 0`.

---

## 2. Agent can rewrite its own policy rules; failed audit commit is reported as success

**Where:** `src/self-mod/code.ts:37` (`PROTECTED_FILES`); `src/agent/policy-rules/authority.ts:97` (protected paths enforced only for external sources); `src/self-mod/code.ts:295-300` and `src/agent/tools.ts:454` (commit result).

`PROTECTED_FILES` covers `agent/policy-engine.ts`, `injection-defense.ts`, `self-mod/code.ts` and `agent/tools.ts`, but not `agent/policy-rules/*`, which holds the treasury limits, x402 allowlist, command blocklist and path rules. `authority.self_mod_from_external` protects `policy-rules` only when the turn's input source is external.

**Reproduce:** in the agent's first (wakeup) turn, call `edit_own_file` with `path: "src/agent/policy-rules/financial.ts"`. Policy allows it, and the file is overwritten and recorded in `modifications`. A rebuild (`exec` is available to the agent) would load the edited rules.

The tool returned `File edited: … (audited + git-committed)`. No commit was created, in either `~/.automaton` or the runtime checkout: the change was left staged. `gitCommit` failures are swallowed at `code.ts:298-300`, and `tools.ts:454` reports a commit regardless. (Our environment had no git identity configured, which is the likely immediate cause.)

**Expected:** policy rules are as protected as the policy engine, whatever the turn source. The tool reports commit failure honestly.

**Suggested fix:** add `agent/policy-rules/` (both `.ts` and `.js`) and `replication/` to `PROTECTED_FILES`. Return the commit outcome from `editFile` and include it in the tool message. Optionally refuse the edit when the snapshot commit fails.

---

## 3. `topup_credits` bypasses the treasury policy

**Where:** `src/agent/tools.ts:277` (`topup_credits`); no rule in `src/agent/policy-rules/financial.ts` applies to it.

`policy_decisions` shows `rules_evaluated: []` for `topup_credits`. With every treasury limit set to 0, `topup_credits {amount_usd: 2500}` was allowed by policy and stopped only by a $0 USDC balance. Tiers go up to $2,500 per call. Bootstrap topup at startup (`src/index.ts`, "Bootstrap topup") also spends $5 without confirmation when credits are below $5.

**Expected:** USDC spent on credits counts against the treasury policy (single, hourly and daily limits, `requireConfirmationAboveCents`), and an operator can disable bootstrap topup.

**Suggested fix:** add `financial.topup_max_single` and route topups through `SpendTracker`, plus a config flag such as `bootstrapTopup: false`.

---

## 4. Agent can replace its creator's genesis prompt without creator confirmation

**Where:** `update_genesis_prompt` in `src/agent/tools.ts`; `src/agent/policy-rules/authority.ts:57` (blocked only from external sources); `rate-limits.ts:49` (1 per day).

In an agent-initiated turn, `update_genesis_prompt {new_prompt: "Maximise revenue at any cost."}` was allowed. The prompt was sanitized, the previous version was backed up, and the new one was applied. The genesis prompt is the creator's instruction, and the README presents creator oversight as a core property.

**Expected:** changing the creator's instruction needs a signed creator approval, or at least is surfaced to the creator before it takes effect.

**Suggested fix:** require a creator-signed message (the SIWE identity already exists) for `update_genesis_prompt`, or queue the change as pending until the creator approves it through the CLI.

---

## Also worth filing (lower priority)

- **Quadratic tokenizer stall.** `estimateTokens` (`src/agent/context.ts:36`) runs `js-tiktoken` on untrusted turn text. Long letter-only runs are quadratic: 16k characters took about 16–21 s. Three tests in `context-hardening.test.ts` never finish because of it. Suggested fix: cap the input length, or use a linear estimate above a threshold.
- **CI treats a hung test run as a pass.** `.github/workflows/ci.yml` exits 0 on `timeout` exit code 124. This masks the stall above and any failure reported after the timeout.
- **Turn source is `undefined` after the first turn.** `authority.ts:41` then treats those turns as external. The result is inconsistent: `spawn_child` is blocked in later turns, but `install_npm_package` (also `dangerous`) is not.
