---
name: Scrapy
category: market-research
subcategory: data-collection
status: approved-with-restrictions
type: framework
canonical_repo: https://github.com/scrapy/scrapy
website: https://scrapy.org
pinned_version: 2.17.0 (PyPI, published 2026-07-07)
license: BSD-3-Clause
score: 84
confidence: high
tested: true
last_verified: 2026-07-23
---

# Scrapy — structured web data collection for market research

## What it does
The standard Python web-crawling framework: spiders, CSS/XPath
extraction, throttling, robots.txt middleware, and pipelines. In this
registry it anchors the market/competitive-research function: pricing
pages, changelogs, job postings, and directory data collected
reproducibly instead of by hand.

## When to use
- Recurring competitive monitoring (pricing/feature pages into a
  dated dataset) and market sizing from public directories — with the
  restrictions below strictly observed

## When not to use / restrictions
- **Legal/ethical boundaries are the founder's responsibility**: honor
  robots.txt (`ROBOTSTXT_OBEY=True`), site ToS, rate limits, and
  copyright/database rights on collected content; never collect personal
  data without a lawful basis (GDPR applies to scraped personal data)
  `[I]` — these are legal constraints, not tool settings
- JavaScript-heavy sites need a rendering layer (Playwright integration)
- Not a turnkey "market research tool" — it collects data; analysis and
  interpretation remain human work

## Evidence
- License BSD-3-Clause `[V]` — PyPI metadata 2.17.0 (2026-07-23)
- Published 2026-07-07; long-lived project (since 2008) with active
  multi-maintainer community stewarded by Zyte `[C]`
- De facto standard; huge production adoption `[C]`

## Validation results (sandboxed test, 2026-07-23)
- `pip install scrapy==2.17.0` — reproducible
- Exercised the extraction core offline: parsed an HTML document via
  `HtmlResponse` and extracted price texts and link hrefs with CSS
  selectors — exact expected values asserted, pass. (Live crawling
  intentionally not performed from the research environment.)

## Security findings
- Crawling executes against third-party infrastructure — misconfigured
  concurrency is indistinguishable from abuse; set conservative
  `DOWNLOAD_DELAY`/`AUTOTHROTTLE` `[I]`

## Legal / licensing findings
- BSD-3-Clause — commercial use permitted. The license covers the tool,
  not the data you collect; collected-data rights are a separate,
  per-source legal question (counsel for anything monetized).

## Installation
`pip install scrapy==2.17.0`

## Agent integration
Agents can draft spiders and selector logic; **crawl targets, rates,
and data-use decisions are human-approved per source**. Never let an
agent expand crawl scope autonomously.

## Required human review
Target list + ToS/robots review per source; personal-data assessment;
storage/retention of collected data.

## Score notes
Functional 18/20 · Security 15/20 · Maintenance 14/15 · Docs 9/10 ·
License 10/10 · Reproducibility 9/10 · Provenance 7/10 · Integration 2/5
→ **84** (restrictions reflect legal-use burden, not code quality)
