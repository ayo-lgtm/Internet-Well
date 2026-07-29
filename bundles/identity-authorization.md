# Identity and Authorization Bundle

Use this bundle only after the project assessment defines users, tenants, organizations, relying applications, protocols, session model, authorization complexity, regulated data, hosting constraints, and operator capability.

## Decision order

1. Preserve a functioning existing authentication system unless a documented requirement is unmet.
2. Separate authentication requirements from authorization requirements.
3. Prefer framework-native or existing-platform authentication for ordinary SaaS applications.
4. Prefer database-native constraints and row-level security for simple tenant and ownership rules.
5. Add a dedicated authorization engine only when the access graph cannot be expressed clearly and tested safely in the application/database layer.
6. Add a full identity platform only when centralized federation, enterprise lifecycle, or multiple relying applications justify its operating burden.

## Application authentication choices

### Supabase Auth
Prefer when Supabase is already the system of record and authentication integrates directly with PostgreSQL RLS. Required checks: exact GoTrue/service version, JWT expiry and rotation, service-role separation, email/SMS provider behavior, redirect allowlists, MFA/passkey support, anonymous users, account linking, admin API exposure, and RLS regression tests.

### Auth.js
Prefer for Next.js applications needing conventional sessions and OAuth/OIDC providers without a separate identity control plane. Promotion requires an exact stable pin, adapter-specific tests, encrypted-cookie/session review, CSRF and callback validation, secret rotation, deployment-host handling, and migration-state review.

### Better Auth
Prefer for TypeScript applications when its plugin and framework support materially fit the product. Use stable releases, not beta versions, for production. Require minimum pins that include SSRF fixes, explicit database schema migration review, cookie/session tests, provider allowlists, plugin minimization, and passkey/MFA recovery tests.

## Full identity platforms

### Keycloak
Use for enterprise federation, SAML/OIDC brokering, centralized realms, service accounts, delegated administration, or multiple applications. Do not use merely to add email/password login to one product. Require current patch pins, migration-guide review, database backup/restore, key rotation, clustered-session planning, admin-event auditing, SMTP controls, rate limiting, and hardened admin-console access.

### ZITADEL
Use only after AGPL and exception-boundary review and when its organization, project, federation, passkey, and multi-tenant capabilities justify a separate control plane. Require exact image digest, backup/restore test, license review, outbound email configuration, key and domain design, and operator runbooks.

### Ory Kratos + Hydra
Use Kratos for identity/account flows and Hydra for OAuth2/OIDC authorization-server responsibilities when a headless composable architecture is intentional. Do not describe either component alone as a complete identity platform. Require explicit login/consent applications, browser/native flow tests, cookie and domain design, key management, database migrations, and failure-mode tests.

## Authorization choices

### Database-native authorization
Default for ownership, organization membership, and modest role models. With Supabase/PostgreSQL, prefer RLS plus tested database constraints when the model is understandable and performant. Test every role and tenant boundary directly.

### Casbin
Use as an embedded policy engine for RBAC/ABAC models where application-local evaluation is desirable. Require deterministic policy fixtures, adapter consistency, enforcement at every protected boundary, model-change review, and deny-by-default behavior.

### OpenFGA
Use for relationship-based authorization when object relations, nested groups, sharing, delegation, or cross-product permissions justify an external service. Pin `v1.15.1` or later within the verified line. Require model tests, tuple lifecycle ownership, consistency expectations, tenant partitioning, cache safety, observability, and service-unavailable behavior.

### SpiceDB
Use for Zanzibar-style relationship authorization where its schema, consistency controls, and operational model fit. Pin at least `v1.51.1` because of the patched moderate-severity advisory. Require schema tests, caveat tests, datastore backup/restore, consistency-token handling, dispatch limits, and failure-mode design.

## Mandatory test matrix

Every selected system must be tested for:

- successful login and logout;
- expired, revoked, replayed, and rotated sessions/tokens;
- disabled user and removed membership;
- cross-tenant access attempts;
- object ownership transfer;
- role downgrade and privilege removal;
- OAuth redirect and state validation;
- account linking and recovery abuse;
- MFA/passkey enrollment and recovery;
- authorization dependency timeout or outage;
- audit-log completeness without leaking secrets;
- backup, migration, and rollback.

## Prohibited claims

Do not claim that using an identity product makes an application secure, compliant, multi-tenant-safe, or enterprise-ready. Do not infer authorization from successful authentication. Do not use aggregate feature count as the selection criterion.