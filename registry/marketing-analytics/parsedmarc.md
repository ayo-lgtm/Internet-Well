---
name: parsedmarc
category: marketing-analytics
subcategory: email-deliverability
status: approved
type: tool
canonical_repo: https://github.com/domainaware/parsedmarc
website: https://domainaware.github.io/parsedmarc/
pinned_version: 10.2.4 (PyPI, published 2026-07-20)
license: Apache-2.0
score: 80
confidence: high
tested: true
last_verified: 2026-07-23
---

# parsedmarc — DMARC aggregate/failure report analysis

## What it does
Parses the DMARC aggregate (RUA) and failure reports that mailbox
providers send you into structured JSON, computing SPF/DKIM/DMARC
alignment per source; optional pipelines into Elasticsearch/Grafana.
The feedback half of the deliverability loop that checkdmarc's
record-validation half begins.

## When to use
- After publishing `rua=` in your DMARC record: weekly parse of
  provider reports to see who is sending as your domain and whether
  legitimate mail is aligning — the evidence needed before escalating
  policy none→quarantine→reject

## When not to use
- Without a DMARC record publishing rua (nothing to parse)
- Real-time abuse response (reports arrive on ~daily provider cycles)

## Evidence
- License Apache-2.0 `[V]` — PyPI metadata 10.2.4 (2026-07-23)
- Published 2026-07-20; active `[V]` — PyPI history
- Same maintainer (domainaware / Sean Whalen) as checkdmarc — a
  coherent, maintained email-auth toolset; individual-led `[C]`

## Validation results (sandboxed test, 2026-07-23)
- `pip install parsedmarc==10.2.4` — reproducible
- Parsed a constructed minimal RUA aggregate XML with `--offline`:
  exit 0; org, policy, record count, and per-record SPF/DKIM/DMARC
  alignment all computed correctly in JSON output. Fully offline
  (`--offline` skips reverse-DNS enrichment).

## Security findings
- Reports contain source IPs and mail-flow metadata about your domain —
  low sensitivity, but treat report mailbox credentials (IMAP ingestion
  mode) with normal secret hygiene `[I]`

## Legal / licensing findings
- Apache-2.0 — commercial use permitted.

## Installation
`pip install parsedmarc==10.2.4`

## Agent integration
JSON output; an agent can summarize weekly reports (new sources,
alignment failures) and open an issue when an unknown sender appears.
DMARC policy changes remain human.

## Required human review
Interpretation of unknown senders (could be forwarding, not spoofing);
policy escalation decisions.

## Score notes
Functional 17/20 · Security 16/20 · Maintenance 13/15 · Docs 8/10 ·
License 10/10 · Reproducibility 10/10 · Provenance 5/10 · Integration
4/5 → **80** (individual-led maintainer concentration noted)
