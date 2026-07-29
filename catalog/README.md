# Curated Repository Candidate Catalog

This directory contains research-backed candidates for future Internet-Well registry admission.

A catalog entry is **not an approval**. It records why a repository matters, its intended role, known license or operational risks, and the capabilities it may support. A candidate becomes a registry record only after the evidence, pinning, licensing, execution testing, and human-review requirements in `METHODOLOGY.md` are satisfied.

## Lifecycle

```text
research candidate
  -> primary-source verification
  -> pinned release or commit
  -> license and security review
  -> sandboxed evaluation
  -> registry record
  -> bundle and playbook use
  -> periodic re-verification
```

`curated-repositories.json` is machine-readable and powers the experimental project detector and resource selector. The selector must prefer validated registry entries over candidate-only entries and must clearly label candidate recommendations as unverified.
