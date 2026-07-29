# Bundle: Identity and Authorization

## Outcome

Select and operate the smallest identity and authorization architecture that securely supports the product’s users, tenants, organizations, relying applications, sessions, permissions, and recovery paths without confusing authentication with authorization.

## Required capabilities

User authentication, session management, credential and recovery protection, tenant isolation, authorization enforcement, revocation, auditability, migration and rollback, backup and restore, outage handling, and human review for consequential access-control changes.

## Selection rules

1. Preserve a functioning existing authentication system unless a documented requirement is unmet.
2. Separate authentication requirements from authorization requirements.
3. Prefer framework-native or existing-platform authentication for ordinary SaaS applications.
4. Prefer Database-native authorization, constraints, and row-level security for simple tenant and ownership rules.
5. Require deny-by-default behavior at every protected boundary.
6. Add a dedicated authorization engine only when the access graph cannot be expressed clearly and tested safely in the application/database layer.
7. Add a full identity platform only when centralized federation, enterprise lifecycle, or multiple relying applications justify its operating burden.
8. Use stable, patched releases and verify exact package or image pins before production adoption.
9. Do not infer authorization from successful authentication.

## Recommended resources

### Application authentication

- Supabase Auth — prefer when Supabase is already the system of record and authentication integrates directly with PostgreSQL RLS. Verify JWT expiry and rotation, service-role separation, redirect allowlists, MFA/passkey behavior, account linking, admin API exposure, and RLS regression tests.
- Auth.js — prefer for Next.js applications needing conventional sessions and OAuth/OIDC providers without a separate identity control plane. Promotion still requires an exact stable pin and adapter-specific verification.
- Better Auth — prefer for TypeScript applications when its framework and plugin support materially fit the product. Use stable releases, minimize plugins, and require pins that include relevant SSRF fixes.

### Full identity platforms

- Keycloak — use for enterprise federation, SAML/OIDC brokering, centralized realms, service accounts, delegated administration, or multiple applications. Do not use merely to add email/password login to one product.
- ZITADEL — use only after AGPL and exception-boundary review and when its organization, federation, passkey, and multi-tenant capabilities justify a separate control plane.
- Ory Kratos plus Hydra — use Kratos for identity/account flows and Hydra for OAuth2/OIDC authorization-server responsibilities when a headless composable architecture is intentional.

### Authorization

- Database-native authorization — default for ownership, organization membership, and modest role models. With Supabase/PostgreSQL, prefer RLS plus tested database constraints when the model is understandable and performant.
- Casbin — use as an embedded policy engine for RBAC/ABAC models where application-local evaluation is desirable.
- OpenFGA — use for relationship-based authorization when object relations, nested groups, sharing, delegation, or cross-product permissions justify an external service. Pin `v1.15.1` or later within the verified line.
- SpiceDB — use for Zanzibar-style relationship authorization where its schema, consistency controls, and operational model fit. Pin at least `v1.51.1` because of the patched advisory reviewed in Tranche 03.

## Implementation order

1. Define users, tenants, organizations, relying applications, protocols, session model, regulated data, and authorization relationships.
2. Document the authentication and authorization boundary separately.
3. Choose the smallest viable authentication system.
4. Implement deny-by-default tenant and ownership rules in the database or application layer.
5. Add a dedicated policy or relationship engine only when justified by explicit access-graph requirements.
6. Add federation, SAML, centralized administration, or a full identity control plane only when required.
7. Implement audit logging, revocation, migration, backup, rollback, and outage behavior before production launch.

## Verification

Every selected system must be tested for:

- successful login and logout;
- expired, revoked, replayed, and rotated sessions or tokens;
- disabled users and removed memberships;
- cross-tenant access attempts;
- object ownership transfer;
- role downgrade and privilege removal;
- OAuth redirect and state validation;
- account linking and recovery abuse;
- MFA/passkey enrollment and recovery;
- authorization dependency timeout or outage;
- audit-log completeness without leaking secrets;
- backup, migration, and rollback.

Do not claim that using an identity product makes an application secure, compliant, multi-tenant-safe, or enterprise-ready. Successful authentication is never evidence that authorization is correct.

## Human review

A competent security or identity reviewer must approve the trust model, tenant-boundary design, privileged roles, redirect and callback configuration, session duration and revocation, account recovery, MFA/passkey recovery, service accounts, policy-model changes, migration plan, backup and restore evidence, and every production exception. No agent may grant itself or another actor elevated access, weaken deny-by-default behavior, or change production identity configuration without explicit human authorization.
