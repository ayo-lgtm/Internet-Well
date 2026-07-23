---
name: ScanCode Toolkit
category: compliance
subcategory: license-compliance
status: approved
type: tool
canonical_repo: https://github.com/aboutcode-org/scancode-toolkit
website: https://aboutcode.org
pinned_version: 32.5.0 (PyPI, published 2026-01-15)
license: Apache-2.0 AND CC-BY-4.0 (license/data files) per PyPI expression
score: 82
confidence: high
tested: true
last_verified: 2026-07-23
---

# ScanCode Toolkit — license, copyright, and origin detection

## What it does
Scans codebases to detect licenses (SPDX-mapped), copyrights, and package
origins — the reference open tool for answering "what licenses am I
actually shipping?" Feeds SBOM/attribution workflows.

## When to use
- Pre-launch license audit of your product's full dependency tree
- Generating attribution notices for permissive-licensed dependencies
- Verifying a candidate dependency's real license before adoption (this
  registry's use case)

## When not to use
- As legal advice: results classify text, they don't resolve compatibility
  questions — that's counsel's job
- Quick per-package checks (registry metadata is faster; ScanCode is for
  thorough audits)

## Evidence
- License expression `Apache-2.0 AND CC-BY-4.0 AND LicenseRef-scancode-*`
  `[V]` — PyPI metadata 32.5.0 (2026-07-23): code Apache-2.0, license
  reference data CC-BY-4.0
- Published 2026-01-15; slower cadence than scanners (semi-annual majors)
  `[V]` — PyPI history
- Professional provenance: nexB / AboutCode org; used by major OSS
  compliance programs and the ClearlyDefined project `[C]`

## Validation results (sandboxed test, 2026-07-23, Phase 2)
- `pip install scancode-toolkit==32.5.0` in fresh venv — reproducible
  (large install; several minutes)
- Scanned a C-file fixture containing an SPDX MIT header and a copyright
  line: detected `mit` license expression and
  `Copyright (c) 2026 Example Corp` exactly; JSON output well-formed.
  Fully offline.

## Security findings
- Local scanning; no code egress `[M]`

## Legal / licensing findings
- Apache-2.0 code; CC-BY-4.0 data requires attribution if you redistribute
  scan-data derivatives. Output usable freely in internal audits.

## Installation
`pip install scancode-toolkit==32.5.0` (check Python-version constraints;
native wheels involved).

## Agent integration
JSON/SPDX output; an agent can flag detected-license changes between
dependency updates for human legal review.

## Required human review
Any compatibility conclusion or shipped attribution file — have counsel
spot-check the first pass.

## Score notes
Functional 17/20 · Security 15/20 · Maintenance 12/15 · Docs 8/10 ·
License 9/10 · Reproducibility 7/10 · Provenance 9/10 · Integration 5/5
→ **82**
