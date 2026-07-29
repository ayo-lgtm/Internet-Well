# Intensive Verification — Tranche 03

Verification date: 2026-07-29

This tranche covers identity, authentication, OAuth/OIDC, and fine-grained authorization. These systems are not interchangeable. Authentication establishes identity; authorization decides permitted actions. Founder OS must not recommend a full identity platform when a framework-native session layer is sufficient, or add a relationship-authorization service when database-native row policies adequately express the product's access model.

## Current exact release evidence

| Candidate | Exact release evidenced | Initial disposition | Principal restriction |
|---|---:|---|---|
| OpenFGA | `v1.15.1` | Tier B candidate after runtime test | authorization-only; model correctness, consistency, tuple lifecycle, and tenant boundaries require design review |
| SpiceDB | `v1.51.1` | Tier B candidate after runtime test | authorization-only; patched moderate-severity CVE makes minimum version enforcement mandatory |
| Keycloak | `26.6.2` | Tier B candidate with substantial operational restrictions | full identity server; recent security-fix cadence, migration complexity, database, clustering, and realm administration require experienced operators |
| Ory Kratos | `v26.2.0` | Tier B candidate with restrictions | identity and account lifecycle, not a complete OAuth authorization server |
| Ory Hydra | `v26.2.0` | Tier B candidate with restrictions | OAuth2/OIDC server, not a user directory or complete login UI |
| ZITADEL | `v4.15.0` | Tier C until licensing and runtime review complete | AGPL-3.0 core with documented exceptions; deployment model and modification obligations require legal review |
| Better Auth | stable `v1.6.6` evidence; `v1.7.0-beta.3` is prerelease | Tier B candidate after package tests | recent SSRF fixes require strict minimum pins; plugin surface expands data and attack boundaries |
| Node Casbin | `v5.50.0` | Tier B candidate after deterministic policy tests | embedded policy engine, not identity management; model and adapter behavior require tests |
| Auth.js | pending exact stable pin | candidate-only | verify package lineage, adapter behavior, session strategy, cookie defaults, and migration state before promotion |
| Supabase Auth | pending exact service/component pin | candidate-only | service behavior depends on hosted/self-hosted configuration, GoTrue version, RLS design, JWT settings, and provider configuration |

## Selection model

### Framework-native application authentication
Use Auth.js, Better Auth, or Supabase Auth when the product needs normal application login, sessions, social/OIDC providers, passkeys/MFA, and modest organization membership. Prefer the product's existing stack and avoid replacing a working authentication system solely because another project has more features.

### Full self-hosted identity platform
Use Keycloak or ZITADEL only when requirements justify a separately operated identity control plane: enterprise federation, SAML, centralized realms/organizations, lifecycle administration, service accounts, delegated administration, or multiple relying applications. These systems add databases, upgrade programs, backup requirements, email/SMS dependencies, key rotation, operational monitoring, and security response obligations.

### Headless identity and OAuth composition
Ory Kratos handles identity/account flows; Ory Hydra handles OAuth2/OIDC authorization-server duties. They may be composed, but that composition is not a turnkey default and requires explicit login/consent UX, session integration, cookie/domain design, key management, and deployment architecture.

### Fine-grained authorization
OpenFGA and SpiceDB are relationship-based authorization systems. Casbin is an embedded policy engine. Use one only when normal application roles, database constraints, and row-level policies cannot clearly and safely express required access. Do not move authorization into a separate service without defining consistency requirements, failure behavior, tuple/policy migration, auditability, tenant isolation, and a rollback path.

## Security findings and minimum-version rules

- OpenFGA versions before the fixes for incorrect cached conditional checks and host-header poisoning must not be selected. The evaluated pin is `v1.15.1`.
- SpiceDB must be at least `v1.51.1` because that patch addresses CVE-2026-40091.
- Keycloak has a sustained security-fix cadence, including recent SSRF, user-enumeration, access-control, token, SAML, UMA, and denial-of-service fixes. Internet-Well must pin current patch releases, prohibit floating tags, and require migration-guide review.
- Better Auth's release evidence includes SSRF fixes across OAuth-provider functionality. Prereleases are not production defaults.
- Identity-system configuration is security-sensitive code. Realm exports, authorization models, policies, callback URLs, cookie settings, token lifetimes, SMTP/SMS credentials, signing keys, and migration files require protected review.

## Reproducibility gates

1. Pull or install exact immutable pins only.
2. Record image digests or package-lock integrity data.
3. Run version and health endpoints without production credentials.
4. Execute local deterministic tests for login/session or policy evaluation where supported.
5. Verify fail-closed behavior when the identity or authorization dependency is unavailable.
6. Test tenant-crossing denials, revoked membership, disabled users, stale sessions, role removal, and object-transfer cases.
7. Validate migration and rollback against disposable databases.
8. Never expose development consoles or default credentials outside an isolated test network.

## Promotion policy

No candidate becomes Tier A through automation. Runtime installation alone is not sufficient. Promotion requires evidence for exact pins, license boundaries, secure defaults, backup/restore, migrations, revocation, audit logging, multi-tenancy behavior, failure handling, and a competent human review of the access model.