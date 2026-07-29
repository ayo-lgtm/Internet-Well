# Intensive Verification — Tranche 01

Verification date: 2026-07-29

This tranche covers six foundational AI/agent repositories selected for their central role in the Founder OS capability graph. Research-catalog presence is not approval. Each candidate is evaluated against `METHODOLOGY.md`; promotion requires exact pinning, license review, security review, reproducible smoke tests, and explicit restrictions.

## Summary

| Candidate | Exact pin evaluated | Proposed status | Main reason |
|---|---|---|---|
| Microsoft MarkItDown | PyPI `markitdown==0.1.6`; Git tag `v0.1.6` | approved-with-restrictions / Tier B after smoke test | focused, permissive, useful ingestion tool; file and URI processing must be sandboxed |
| Microsoft Playwright MCP | npm `@playwright/mcp@0.0.75`; Git tag `v0.0.75` | experimental / Tier C | powerful browser session access; upstream states it is not a security boundary |
| Microsoft Semantic Kernel | PyPI `semantic-kernel==1.44.0` | approved-with-restrictions / Tier B after smoke test | mature SDK, but Microsoft identifies Agent Framework as its successor |
| LangGraph | PyPI `langgraph==1.2.9` | approved-with-restrictions / Tier B after smoke test | strong durable-workflow fit; extra complexity and dependency security history require care |
| PydanticAI | PyPI `pydantic-ai==1.104.0` | approved-with-restrictions / Tier B after smoke test | typed Python agent framework with provenance; recent SSRF fixes require strict minimum pinning |
| LiteLLM | PyPI `litellm==1.92.0` | approved-with-restrictions / Tier B after smoke test | useful provider routing and signed images; broad data plane and rapid release cadence increase risk |

## 1. Microsoft MarkItDown

### Identity and pin

- Canonical repository: `https://github.com/microsoft/markitdown` `[V]`
- Evaluated release: `v0.1.6`, released 2026-05-26 `[V]`
- PyPI package: `markitdown==0.1.6`; Python >=3.10; MIT license expression `[V]`
- PyPI maintainers shown as `afourney` and `bansalg` `[V]`

### Function and fit

MarkItDown converts common files and streams into Markdown for indexing, extraction, and LLM-oriented document pipelines. It is appropriate as a preprocessing component, not a complete OCR, document-understanding, malware-scanning, or evidentiary-preservation system.

### Security and privacy

- Upstream warns that MarkItDown performs I/O with the privileges of the current process and can access resources that process can access `[V]`.
- Untrusted files, URLs, archives, and plugins must run in an isolated worker with narrow filesystem and network permissions `[I]`.
- Optional extras materially expand the dependency and attack surface; install only required format groups `[I]`.
- Conversion output can omit layout, provenance, signatures, metadata, or visual context and must not be treated as a legally complete rendition `[I]`.

### Licensing

MIT permits commercial use, modification, distribution, and SaaS use with preservation of copyright and license notice. Microsoft and third-party trademark restrictions remain separate from the software license.

### Reproducibility gate

CI must install `markitdown==0.1.6`, convert a local text fixture, and verify deterministic Markdown output without credentials or network access.

### Proposed disposition

`approved-with-restrictions`, Tier B, after the smoke test passes. Required restrictions: isolated file processing, minimal extras, input limits, timeouts, malware scanning where appropriate, and human review for legal or high-impact documents.

## 2. Microsoft Playwright MCP

### Identity and pin

- Canonical repository: `https://github.com/microsoft/playwright-mcp` `[V]`
- Evaluated release: `v0.0.75`, commit prefix `8116437`, released 2026-05-07 `[V]`
- License: Apache-2.0 `[V]`
- Release commits are shown as signed with GitHub's verified signature `[V]`

### Function and fit

Playwright MCP exposes browser automation to LLM clients through MCP and accessibility snapshots. It is useful for bounded browser tasks, verification, and controlled research. Upstream itself notes that coding agents may prefer CLI plus skills because it is more token-efficient.

### Security and privacy

- Upstream explicitly states Playwright MCP is **not a security boundary** `[V]`.
- A connected agent may read authenticated pages, cookies, storage, downloads, clipboard content, and sensitive form data depending on browser configuration `[I]`.
- Browser sessions must use dedicated profiles, isolated containers, scoped accounts, hostname allowlists, download restrictions, action approval, and complete audit logs `[I]`.
- `browser_run_code_unsafe` is explicitly named to signal sandbox-escape implications `[V]`.
- Exposing the server on `0.0.0.0` without network controls creates material remote-access risk `[I]`.

### Licensing

Apache-2.0 is commercially suitable and includes patent terms. Browser binaries, websites, extensions, and downloaded content have separate licenses and terms.

### Reproducibility gate

CI must install exact npm version `@playwright/mcp@0.0.75` and run its help/version path without starting an externally reachable server or accessing a real browser profile.

### Proposed disposition

Experimental, Tier C. It must remain permission-gated until sandbox, session isolation, tool allowlisting, prompt-injection, download, and credential-exposure evaluations pass.

## 3. Microsoft Semantic Kernel

### Identity and pin

- Canonical repository: `https://github.com/microsoft/semantic-kernel` `[V]`
- Python package evaluated: `semantic-kernel==1.44.0`, released 2026-07-07 `[V]`
- Python >=3.10; MIT; PyPI lists Microsoft and named maintainers `[V]`
- Repository license is MIT `[V]`

### Function and fit

Semantic Kernel supports model connectors, plugins, agents, workflows, MCP, and multiple vector/data integrations. It is suitable where its abstractions fit an existing Microsoft-oriented or multi-provider architecture.

### Maintenance and migration risk

PyPI currently states that Microsoft Agent Framework is the production-ready successor to Semantic Kernel and points users to a migration guide `[V]`. This materially changes the recommendation: Semantic Kernel remains active and usable, but new projects must compare it against the successor before adopting it.

### Security and privacy

- The optional integration surface is large; every connector may add credentials, data flows, transitive dependencies, and provider-specific behavior `[I]`.
- Install only required extras and create an explicit model/tool/data-flow inventory `[I]`.
- Plugins and model-selected tools require schema validation, authorization, budgets, timeouts, audit trails, and human approval for consequential actions `[I]`.

### Reproducibility gate

CI must install `semantic-kernel==1.44.0`, import the package, instantiate a local `Kernel`, and verify that no provider credential or network call is required for initialization.

### Proposed disposition

`approved-with-restrictions`, Tier B, after smoke test. Restriction: existing systems and migration/reference use are stronger cases than unexamined greenfield adoption; compare Microsoft Agent Framework before selecting.

## 4. LangGraph

### Identity and pin

- Canonical repository: `https://github.com/langchain-ai/langgraph` `[V]`
- License: MIT `[V]`
- Evaluated stable PyPI release: `langgraph==1.2.9`, released 2026-07-10 `[V]`
- PyPI uses trusted publishing for the evaluated release and publishes package hashes `[V]`

### Function and fit

LangGraph is a low-level framework for stateful, durable, multi-step agent workflows. It is useful where explicit state, conditional routes, interrupts, checkpoints, retries, and recovery are product requirements. It is not a universal default for simple tool calls or linear workflows.

### Security history and restrictions

- Earlier LangGraph/LangChain ecosystem advisories included a SQLite checkpoint SQL-injection issue, a deserialization issue in related dependencies, and path-traversal risk in related components; patched versions were released `[C]`.
- The selected pin must resolve `langgraph-checkpoint-sqlite>=3.0.1` when that package is used, and dependency resolution must be captured in an SBOM `[I]`.
- Checkpoint state may contain prompts, user data, tool outputs, and secrets; persistence requires data classification, encryption, tenant isolation, retention, and deletion controls `[I]`.
- Graph complexity can conceal infinite loops, repeated actions, and hidden side effects; enforce recursion limits, idempotency, action budgets, and approval nodes `[I]`.

### Reproducibility gate

CI must install `langgraph==1.2.9`, compile a two-node local `StateGraph`, invoke it, and verify deterministic state output with no model or network dependency.

### Proposed disposition

`approved-with-restrictions`, Tier B, after smoke test and dependency inventory. Use only where durable graph semantics justify the added operational complexity.

## 5. PydanticAI

### Identity and pin

- Canonical repository: `https://github.com/pydantic/pydantic-ai` `[V]`
- License: MIT `[V]`
- Evaluated stable release: `pydantic-ai==1.104.0`, released 2026-05-29 `[V]`
- PyPI trusted publishing and Sigstore/in-toto attestation link the wheel to commit `72a471306a449e18dc1ca90ce0b0f22be4ac2429` `[V]`
- V2 was still pre-release in the evidence reviewed; greenfield production should use stable v1 unless migration risk is accepted `[V]`

### Function and fit

PydanticAI is a typed Python agent framework emphasizing structured outputs and Pydantic validation. It is well suited to schema-first Python applications and bounded tool use.

### Security history and restrictions

- Releases 1.99.0 and 1.102.0 addressed SSRF cloud-metadata blocklist bypasses involving explicitly enabled local URL downloads and IPv6 transition forms `[V]`.
- Minimum acceptable pin is therefore at least 1.102.0; this tranche evaluates 1.104.0 `[I]`.
- Structured output validation does not prove factual accuracy, authorization, safety, or legal correctness `[I]`.
- URL-fetching, tool execution, model providers, and UI adapters require separate input, network, secret, and data-flow controls `[I]`.

### Reproducibility gate

CI must install `pydantic-ai==1.104.0`, import `Agent` and the test-model module, and run a local no-provider test-model interaction or, if its public test API changes, at minimum instantiate the core agent without external credentials.

### Proposed disposition

`approved-with-restrictions`, Tier B, after smoke test. Require exact pinning, SSRF-safe defaults, schema validation, explicit tool authorization, and independent output evaluation.

## 6. LiteLLM

### Identity and pin

- Canonical repository: `https://github.com/BerriAI/litellm` `[V]`
- Evaluated PyPI release: `litellm==1.92.0`, released 2026-07-12 `[V]`
- PyPI trusted publishing and package hashes are available `[V]`
- GitHub release documentation states standard images are signed with Cosign and documents verification commands `[V]`

### Function and fit

LiteLLM provides a provider-normalizing SDK and proxy/gateway with routing, fallbacks, cost tracking, logging, and guardrail integrations. It is useful when a product genuinely needs multi-provider routing or a controlled model gateway.

### Security, privacy, and operational risk

- A proxy deployment becomes a high-value data and credential plane: prompts, outputs, API keys, user identifiers, budgets, and logs may transit it `[I]`.
- Default logging, telemetry, caching, callback, and persistence behavior must be explicitly reviewed before production use `[I]`.
- The project has a very rapid release cadence; upgrades require pinned images/packages, changelog review, compatibility testing, and rollback `[I]`.
- Release 1.86.0 documented that one non-root image was built from a different patch commit and lacked a Cosign signature, while a follow-up release restored signed builds `[V]`. This demonstrates why every selected image—not merely the version family—must be verified.
- Self-hosting does not by itself guarantee that model data remains private because upstream model providers and configured callbacks remain separate data recipients `[I]`.

### Reproducibility gate

CI must install `litellm==1.92.0`, import the package, inspect the callable routing interface, and perform no provider request. A later container-specific evaluation must verify the exact chosen image signature with Cosign.

### Proposed disposition

`approved-with-restrictions`, Tier B, after package smoke test. A separate production-gateway evaluation remains mandatory before use with real credentials or user data.

## Promotion rules for this tranche

1. Smoke-test workflow must pass at the exact pins.
2. Dependency inventory and hashes must be retained in the CI artifact or transcript.
3. No candidate is Tier A because no competent human has reviewed and approved the evidence.
4. Playwright MCP remains Tier C even if installation passes; installation does not validate containment.
5. Registry records will be created or promoted only after the smoke-test result is recorded.

## Primary evidence consulted

- Official GitHub repositories, licenses, security guidance, and signed release pages.
- Official PyPI project and release pages, including release dates, hashes, trusted-publishing and attestation details.
- Project-maintained migration and security notes.

Independent reporting was used only to identify security advisories for direct version checks; official patched-version and release evidence controls the disposition.