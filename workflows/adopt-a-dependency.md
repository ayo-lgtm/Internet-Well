# Workflow: Adopt a Dependency

Repeatable check before any new library, tool, or service enters your
product or toolchain. Derived from METHODOLOGY; an agent can execute
steps 1–6 and must stop at step 7.

1. **License first.** Read the LICENSE file at the version you would pin —
   not the repo badge. Check the SPDX id against
   [`../licenses/obligations-matrix.md`](../licenses/obligations-matrix.md).
   Watch for open-core markers: `enterprise/` or `ee/` directories,
   `@license` file headers, "editions" language. Non-OSS (BUSL, SSPL,
   ELv2, FSL, SUL, Commons Clause) → stop, find an alternative, record it
   in [`../rejected/README.md`](../rejected/README.md).
2. **Maintenance pulse.** Last release date, last meaningful commit,
   maintainer count/concentration, archived flag. Abandoned + security-
   relevant → reject (the Crater rule).
3. **Security signals.** GitHub security tab (advisories + policy),
   OpenSSF Scorecard where reachable, Dependabot/dependency-graph view,
   known CVEs. Published advisories with fast fixes are a *positive*
   signal; silence plus no policy is not.
4. **Provenance.** Prefer registries with verifiable provenance (Go module
   proxy hashes, npm/PyPI signatures, signed releases). Pin exact
   versions; never adopt from a curl|sh script without reading it.
5. **Sandboxed test.** Install at the pin in an isolated environment with
   no credentials; run a representative workflow. Record commands and
   results (see [`../evaluations/README.md`](../evaluations/README.md)).
6. **Draft the record.** Write a registry record per
   [`../schemas/record-schema.md`](../schemas/record-schema.md); run
   `python3 automation/verify_registry.py` and
   `python3 automation/build_index.py`.
7. **Human decision.** Tier assignment above C, anything in security/
   legal-compliance/finance, and the adoption itself are human calls.
