# Evidence Policy

Every material claim in a registry record carries an evidence tag:

| Tag | Meaning |
|---|---|
| `[V]` Verified | Confirmed directly from primary evidence (API response, license file, registry metadata, official release page) during research |
| `[C]` Corroborated | Multiple independent reliable sources agree |
| `[M]` Maintainer-claimed | Stated by the project; not independently verified |
| `[R]` Community-reported | Reported by users; not independently verified |
| `[I]` Inference | Reasoned conclusion from verified facts |
| `[U]` Unknown | Could not be determined |

## Standard verification signals

The verification foundation uses (see METHODOLOGY §1a for detail):

- **OpenSSF Scorecard** — automated open-source security-health signals
- **SLSA** — build integrity and software provenance
- **SPDX** — standardized licensing and SBOM identifiers
- **GitHub dependency graph** — dependency, license, vulnerability visibility
- **GitHub Dependabot alerts** — known vulnerable dependencies

These signals do not prove a repository is safe; they provide defensible
verification evidence. Human review is additionally required for Tier A in
sensitive areas (see `schemas/record-schema.md`).

## Where evidence lives

- **Inline in records** — each Evidence section names its sources and
  dates. The record is the citation of first resort.
- **[`RECHECK.md`](RECHECK.md)** — the open-debt ledger: everything that
  could not be verified, why, and how to close it. An honest registry is
  defined as much by this file as by its approvals.
- **[`../evaluations/README.md`](../evaluations/README.md)** — execution-
  test transcript (commands, results, failed attempts).
- Raw captures (API responses, license texts) are re-fetchable from the
  cited primary sources; snapshot into this directory only when a source
  is at risk of disappearing or being retroactively changed — name files
  `YYYY-MM-DD-<source>-<what>.<ext>`.

## Retention and decay

Facts decay. `last_verified` dates gate a 90-day re-verification sweep
(CI-enforced). License drift is the most-observed failure mode in this
registry's own research (Terraform, Sentry, n8n, Grafana, Renovate all
relicensed) — every entry touch re-reads the license at the new pin.
