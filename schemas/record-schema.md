# Registry Record Schema

Every file under `registry/<category>/*.md` is a Markdown record with flat
YAML front matter. `automation/verify_registry.py` enforces this contract
(machine-readable form: [`record.schema.json`](record.schema.json)).

## Front matter fields

| Field | Required | Values / format |
|---|---|---|
| `name` | yes | Human-readable resource name |
| `category` | yes | Must equal the directory name: `engineering`, `security`, `product`, `design`, `legal-compliance`, `marketing`, `finance`, `operations`, `launch-maintenance` |
| `subcategory` | yes | Finer function slug (e.g. `dast`, `crm`, `backup-restore`) — preserves distinctions the nine directories flatten (sales-support, mobile, AI) |
| `status` | yes | `approved` · `approved-with-restrictions` · `experimental` · `rejected` · `recheck-required` |
| `tier` | yes | `A` · `B` · `C` (tier `D` = rejected; lives only in `rejected/README.md`) |
| `human_reviewed` | yes | `true` only after a competent human has reviewed the record and its evidence; set by a person, never by automation |
| `type` | yes | `tool` · `framework` · `template` · `standard` · `reference-implementation` · `agent-skill` |
| `canonical_repo` | yes* | URL, or `none (...)` with explanation for non-repo resources |
| `website` | yes | Official site |
| `pinned_version` | yes | Release/commit verified (include VCS hash when available) |
| `license` | yes | SPDX identifier; annotate open-core boundaries inline |
| `score` | yes | 0–100 per METHODOLOGY §5, or `null` for standards/templates |
| `confidence` | yes | `high` · `medium` · `low` |
| `tested` | yes | `true` · `false` · `not-applicable` — sandboxed execution test at the pin (transcript in `evaluations/README.md`) |
| `last_verified` | yes | `YYYY-MM-DD`; entries older than 90 days fail the weekly CI staleness check |

## Tier rules (enforced)

- **A** — status `approved` AND `tested: true` AND `confidence: high` AND
  `human_reviewed: true`. Sensitive categories (`security`,
  `legal-compliance`, `finance`) can never be A without human review —
  automated scoring alone is insufficient there by design.
- **B** — generally reliable; approved (with or without restrictions) with
  documented limitations.
- **C** — promising, insufficient evidence for critical work:
  `experimental` status, or approved with low/medium confidence and no
  execution test.
- **D** — rejected/abandoned/unsafe/legally unsuitable/unverifiable;
  recorded with reasons in `rejected/README.md`.

## Body sections

What it does · When to use · When not to use (and restrictions) ·
Evidence (claims tagged `[V]`/`[C]`/`[M]`/`[R]`/`[I]`/`[U]` — see
`evidence/README.md`) · Validation results · Security findings ·
Legal/licensing findings · Installation · Agent integration · Required
human review · Score notes.
