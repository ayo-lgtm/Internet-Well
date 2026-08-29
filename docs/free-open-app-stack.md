# Free/Open App Stack

Internet Well should prefer capable open-source software and durable free tiers when selecting infrastructure, while treating “free” as a constraint rather than evidence of quality. Every candidate still needs license, security, maintenance, privacy, operational and fit review.

## Resources received for evaluation

### Discovery directories

- `punkpeye/awesome-mcp-servers` — MIT-licensed directory of MCP servers. Use as a discovery source, not an automatic trust list. Individual servers require independent review.
- `ripienaar/free-for-dev` — directory of SaaS/PaaS/IaaS offerings with developer free tiers. Useful for finding low-cost infrastructure choices; free-tier terms can change, so verify at selection time.
- `Shubhamsaboo/awesome-llm-apps` — Apache-2.0 collection of runnable AI-agent, RAG, MCP and related application examples. Treat examples as reference implementations and evaluate their dependencies separately.

### Runtime/model infrastructure

- `ollama/ollama` — local/open-model runtime option. Useful where local inference, privacy, development without per-request API fees, or provider independence matters. Model licenses and hardware requirements remain separate constraints.

### Web data extraction

- `D4Vinci/Scrapling` — BSD-3-Clause adaptive scraping/crawling framework with parsing, fetchers, spiders and MCP support. Use only for authorized/public data collection consistent with applicable terms, robots directives, privacy rules and project policy. Anti-bot functionality is not authorization to evade access controls.

### Previously evaluated

- `fingerprintjs/fingerprintjs` — browser fingerprinting capability; approved only for narrowly scoped abuse/fraud signals with privacy/security review. Not a default analytics or identity layer.

### Rejected / quarantine

- `ShadowHackers/gmail-account-creator` (as depicted in submitted material) — do not integrate. Automated bulk account creation, anti-detection and phone-verification bypass are incompatible with Internet Well's legitimate application-infrastructure catalog. If retained at all, retain only a metadata-level blocked-resource record for detection/governance; do not ingest operational instructions or code.

## Backend production checklist

This is a living checklist. New stages supplied by maintainers should be added after validation.

1. Identity, authentication and authorization
2. Input/schema validation
3. API contracts and versioning
4. Database/storage and migrations
5. Secrets and configuration management
6. Error handling with consistent, non-sensitive responses
7. Rate limiting, quotas and abuse controls
8. Logging, metrics, tracing and alerting
9. Background jobs, queues and retries where required
10. Caching where justified
11. File/object storage and malware/content controls where uploads exist
12. Email, Web Push/PWA notifications and other messaging where required
13. Security headers, CORS/CSRF/session controls as applicable
14. Dependency, secret and vulnerability scanning
15. Backup, restore and disaster-recovery expectations
16. Privacy, retention and deletion controls
17. Testing: unit, integration, end-to-end, accessibility and failure paths
18. CI/CD, environment separation, rollback and deployment verification
19. Health/readiness checks and graceful degradation
20. Documentation, runbooks and ownership

## Selection policy

For every backend capability, Internet Well should rank candidates in this order when technically appropriate:

1. already-present platform capability with no incremental service;
2. maintained open-source/self-hostable option;
3. durable free tier from a reputable provider;
4. paid service only when it materially improves reliability, security, compliance or total operating cost.

Never choose a tool solely because it is free. Record license, maintenance status, security posture, data handling, vendor lock-in, free-tier limits, migration path and operational burden before recommending production use.
