# Workflow: Re-verify a Registry Entry

Triggered by the weekly CI staleness check (entries >90 days old fail
`automation/verify_registry.py`) or by any advisory/relicense signal.

1. **License re-read** at the current release — license drift is this
   registry's most-observed failure mode (Terraform, Sentry, n8n,
   Grafana, Renovate). Any change of SPDX id or open-core boundary →
   update record; if it leaves open source, move to
   [`../rejected/README.md`](../rejected/README.md) with evidence and
   note migration options.
2. **Release + activity check.** New latest stable, release cadence,
   archived flag, maintainer changes. Update `pinned_version` (with VCS
   hash where available).
3. **Advisory sweep.** GitHub security tab for new GHSAs since
   `last_verified`; check whether the current pin includes fixes.
   OSV/Scorecard when reachable from the environment.
4. **Re-test if the pin moved** and the entry is execution-tested:
   re-run the documented test from
   [`../evaluations/README.md`](../evaluations/README.md) at the new pin.
5. **Update the record**: findings, `last_verified`, tier if the rules
   change the outcome. Close or open items in
   [`../evidence/RECHECK.md`](../evidence/RECHECK.md).
6. **Regenerate + lint**: `python3 automation/build_index.py && python3
   automation/verify_registry.py`.
7. **Human review** for any tier promotion, any sensitive-category
   change, and any status downgrade that affects production usage.
