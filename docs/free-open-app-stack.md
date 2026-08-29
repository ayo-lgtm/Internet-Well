# Free/Open App Stack

Internet Well should prefer capable open-source software and durable free tiers when selecting infrastructure, while treating “free” as a constraint rather than evidence of quality. Every candidate still needs license, security, maintenance, privacy, operational and fit review.

## User and agent navigation

Use the capability checklist below for backend requirements. For applications intended to install directly from the web without App Store/Google Play distribution, use **[Storeless App / PWA Production Framework](storeless-pwa-framework.md)**. It covers Home Screen installation, iPhone guidance, Web Push/VAPID, service workers, badges, deep links, offline/update behavior, iOS capability detection, guided fallbacks, open-source resources and production verification.

## Resources received for evaluation

### Discovery directories

- `punkpeye/awesome-mcp-servers` — MIT-licensed directory of MCP servers. Use as a discovery source, not an automatic trust list. Individual servers require independent review.
- `ripienaar/free-for-dev` — directory of SaaS/PaaS/IaaS offerings with developer free tiers. Useful for finding low-cost infrastructure choices; free-tier terms can change, so verify at selection time.
- `Shubhamsaboo/awesome-llm-apps` — Apache-2.0 collection of runnable AI-agent, RAG, MCP and related application examples. Treat examples as reference implementations and evaluate their dependencies separately.

### Runtime/model infrastructure

- `ollama/ollama` — local/open-model runtime option. Useful where local inference, privacy, development without per-request API fees, or provider independence matters. Model licenses and hardware requirements remain separate constraints.

### Storeless/PWA infrastructure

- `pwa-builder/PWABuilder` — MIT-licensed PWA tooling and maintained install-experience components. Use for validation, install UX and cross-platform PWA guidance.
- `pwa-builder/pwa-starter` — production-oriented PWA starter/reference for greenfield apps; do not rewrite an existing application merely to adopt it.
- `serwist/serwist` — service-worker/PWA tooling for modern JavaScript applications; evaluate current version/license when selected.
- `web-push-libs/web-push` — standards-based Node.js Web Push/VAPID server library. Prefer a language-appropriate sibling when the backend is not Node.js.
- See `docs/storeless-pwa-framework.md` for the complete installation, notification, iOS fallback and verification workflow.

### Web data extraction

- `D4Vinci/Scrapling` — BSD-3-Clause adaptive scraping/crawling framework with parsing, fetchers, spiders and MCP support. Use only for authorized/public data collection consistent with applicable terms, robots directives, privacy rules and project policy. Anti-bot functionality is not authorization to evade access controls.

### Previously evaluated

- `fingerprintjs/fingerprintjs` — browser fingerprinting capability; approved only for narrowly scoped abuse/fraud signals with privacy/security review. Not a default analytics or identity layer.

### Rejected / quarantine

- `ShadowHackers/gmail-account-creator` (as depicted in submitted material) — do not integrate. Automated bulk account creation, anti-detection and phone-verification bypass are incompatible with Internet Well's legitimate application-infrastructure catalog. If retained at all, retain only a metadata-level blocked-resource record for detection/governance; do not ingest operational instructions or code.

## Backend stages received so far

The submitted backend series is useful as a capability checklist, but Internet Well should normalize each stage into a production requirement and then select the smallest reliable implementation. A stage is not automatically a separate service.

### 01 — Authentication

**Requirement:** prove who the user is and establish a secure authenticated session. Support only identity methods the product needs: email/password, magic link/OTP, OAuth/OIDC, passkeys, or enterprise identity.

**Free/open-first options:**

- **Supabase Auth / GoTrue** — strong default when the project already uses Supabase; avoids adding another identity vendor and integrates with PostgreSQL/RLS.
- **Auth.js** (`nextauthjs/next-auth`, ISC) — strong framework-level option for Next.js and other supported web stacks; GitHub metadata was rechecked on 2026-08-29.
- **Keycloak** — mature self-hosted identity and access-management server for heavier enterprise/OIDC/SAML needs.
- **ZITADEL / Ory** — evaluate when a project needs a dedicated self-hosted identity platform rather than application-level auth.

**Agent rule:** do not build password hashing, OAuth flows, recovery tokens, session rotation, or passkey protocol code from scratch when a maintained identity implementation fits. Prefer secure cookie/session handling over exposing long-lived bearer tokens to browser JavaScript. Require MFA or step-up authentication for high-risk actions where appropriate.

### 02 — Authorization / RBAC

**Requirement:** decide what an authenticated actor is allowed to read, create, update, delete, approve, administer, or execute. Authentication answers *who are you?*; authorization answers *what may you do?*

**Free/open-first options:**

- **PostgreSQL roles + Row Level Security** — first choice for Supabase/Postgres applications when permissions are data-centric.
- **Casbin** — open-source authorization library for RBAC/ABAC and policy models when application-level policy becomes more complex.
- **framework middleware/route guards** — acceptable for coarse page/API access, but not sufficient by itself when records require per-user/per-tenant enforcement.

**Agent rule:** enforce authorization server-side and at the data boundary. UI hiding is never an access-control mechanism. Prefer least privilege, deny-by-default policies, tenant isolation tests, and explicit admin/service-role boundaries. Never place privileged service keys in a browser client.

### 03 — Email verification

**Requirement:** verify control of an email address where verification materially matters to account activation, recovery, abuse reduction, or communications. Email verification is not identity proof.

**Free/open-first options:**

- **use the existing auth platform's verification flow first** — e.g. Supabase Auth when already selected.
- **Nodemailer + SMTP** — open-source Node.js transport layer when the application owns verification-token generation and an SMTP service is already available.
- **self-hosted SMTP/mail infrastructure** can be evaluated for mature teams, but operational deliverability burden is substantial.
- **free-tier transactional email providers** such as Resend can be considered when self-hosting is not operationally sensible; verify the current free-tier limits at implementation time.

**Required controls:** short-lived single-use tokens, hashed token storage where practical, rate-limited resend, no account enumeration, clear expiration handling, deliverability/error telemetry, and a recovery path for mistyped addresses.

### 04 — File uploads

**Requirement:** safely accept and store user files without routing large blobs through the relational database.

**Free/open-first options:**

- **Supabase Storage** — default when already using Supabase; pair bucket policies with RLS-aware application authorization.
- **tus / `tus/tusd`** — MIT-licensed resumable-upload protocol/server; useful for large or unreliable-network uploads and independently rechecked on 2026-08-29.
- **Uppy** — open-source upload UI/client ecosystem; useful with tus or compatible storage backends.
- **S3-compatible object storage** — use existing platform/object-storage capability before adding a specialized upload SaaS.

**Required controls:** server-authorized upload scopes, type/size limits, randomized object keys, private-by-default buckets for sensitive content, signed URLs where appropriate, metadata validation, malware/content scanning when risk warrants it, retention/deletion rules, and protection against users overwriting another user's objects.

### 05 — Search & filtering

**Requirement:** let users retrieve relevant records by text and structured facets without prematurely deploying a search cluster.

**Free/open-first options:**

- **PostgreSQL indexes + full-text search** — default for small/medium product datasets and projects already on Postgres. Add `pg_trgm` where fuzzy matching is sufficient.
- **OpenSearch** (`opensearch-project/OpenSearch`, Apache-2.0) — validated open-source distributed search engine for large/complex search workloads.
- **Meilisearch** — fast developer-focused search option, but re-check the exact current license and deployment terms before production adoption; GitHub currently reports the repository license as `NOASSERTION` rather than a simple permissive SPDX value.
- **Typesense** — evaluate as another self-hostable search option when instant typo-tolerant product search is needed.

**Agent rule:** start with database-native search unless measured requirements justify a separate index. Search engines introduce synchronization, reindexing, failure-recovery, security and operational complexity. Every filter/sort field exposed by an API must be allow-listed rather than interpolated blindly into queries.

### 06 — Pagination

**Requirement:** bound response sizes and incrementally retrieve collections.

**Free/open-first implementation:** usually **no additional product or repository is required**. Use the database/framework already present.

- PostgreSQL `LIMIT/OFFSET` is acceptable for smaller, shallow result sets.
- Prefer cursor/keyset pagination for large, frequently changing, or feed-like datasets.
- Prisma, GraphQL and common web frameworks already expose pagination patterns; use them only where they match the chosen API contract.

**Agent rule:** apply maximum page sizes server-side; use a deterministic sort with a stable unique tie-breaker; do not expose unbounded `limit`; define cursor encoding/expiry semantics; and test inserts/deletes between page requests to avoid duplicates/skips where correctness matters.

### 07 — Sorting

**Requirement:** return results in an explicit, predictable order.

**Free/open-first implementation:** again, **no separate service is normally required**. Use PostgreSQL/ORM/search-engine ordering already in the stack.

**Agent rule:** allow-list sortable fields and directions; create indexes for common expensive sorts; include stable tie-breakers; define null ordering; keep sorting semantics consistent across UI and API; and never interpolate arbitrary user-provided SQL identifiers.

### 08 — Caching

**Requirement:** reduce repeated computation/database reads only where measurements or workload characteristics justify cache complexity.

**Free/open-first options:**

- **HTTP/browser/CDN cache headers** — cheapest first layer for public/static/revalidatable content.
- **framework/platform cache** — prefer existing Next.js/Vercel/Cloudflare/etc. cache primitives when already deployed there and semantics are understood.
- **Valkey** (`valkey-io/valkey`, BSD-3-Clause) — strong fully open-source Redis-protocol-compatible choice for distributed cache, ephemeral state, rate-limit counters and similar workloads; repository/license rechecked on 2026-08-29.
- **Memcached** — simple distributed cache where its simpler data model is enough.

**Agent rule:** do not cache sensitive user data in shared keys; namespace tenant/user data; define TTL and invalidation before implementation; avoid using cache as the sole source of durable truth; protect distributed caches from public network exposure; and instrument hit/miss/latency so the cache proves its value.

## Backend production checklist

This is a living checklist. New stages supplied by maintainers should be added after validation.

1. Authentication / identity
2. Authorization (RBAC/ABAC/data policies)
3. Email/contact verification where required
4. File/object uploads where required
5. Search and filtering where required
6. Pagination for collections
7. Sorting for collections
8. Caching where justified
9. Rate limiting, quotas and abuse controls
10. Error handling with consistent, non-sensitive responses
11. Input/schema validation
12. API contracts and versioning
13. Database/storage and migrations
14. Secrets and configuration management
15. Logging, metrics, tracing and alerting
16. Background jobs, queues and retries where required
17. Email, Web Push/PWA notifications and other messaging where required — for storeless/mobile-web apps use `docs/storeless-pwa-framework.md`
18. Security headers, CORS/CSRF/session controls as applicable
19. Dependency, secret and vulnerability scanning
20. Backup, restore and disaster-recovery expectations
21. Privacy, retention and deletion controls
22. Testing: unit, integration, end-to-end, accessibility and failure paths
23. CI/CD, environment separation, rollback and deployment verification
24. Health/readiness checks and graceful degradation
25. Documentation, runbooks and ownership

## Selection policy

For every backend capability, Internet Well should rank candidates in this order when technically appropriate:

1. already-present platform capability with no incremental service;
2. maintained open-source/self-hostable option;
3. durable free tier from a reputable provider;
4. paid service only when it materially improves reliability, security, compliance or total operating cost.

Never choose a tool solely because it is free. Record license, maintenance status, security posture, data handling, vendor lock-in, free-tier limits, migration path and operational burden before recommending production use.

## Agent implementation principle

The goal is not to maximize the number of dependencies. For each requested app, the engineering agent should map requirements to this capability matrix, identify which capabilities are already provided by the selected platform, and add only the smallest justified open/free component for gaps. Every recommendation must distinguish **open source**, **self-hostable**, **free tier**, and **paid**, because those are not interchangeable concepts.
