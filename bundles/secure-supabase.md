# Bundle: Secure Supabase

## Outcome

Establish defensible tenant isolation, data access, secrets handling, storage controls, migration safety, observability, backup, and recovery for a Supabase-backed product.

## Required capabilities

Schema ownership, RLS, policy testing, service-role isolation, authentication review, storage policies, Edge Function security, migration control, audit and logs, backup and restore, secrets detection, incident response, and production separation.

## Recommended resource set

- platform: Supabase and PostgreSQL;
- migrations: dbmate or the project's existing migration system;
- secrets: Gitleaks; TruffleHog only with AGPL review and a specific need for live validation;
- dependency and container scanning: Trivy and OSV-Scanner;
- infrastructure: OpenTofu when infrastructure is managed outside the Supabase dashboard;
- backup: pgBackRest for managed PostgreSQL workflows where compatible, or Restic for encrypted filesystem/object backup layers;
- policy and authorization testing: project-specific SQL and API tests; OpenFGA or SpiceDB only when authorization genuinely exceeds PostgreSQL RLS needs;
- monitoring: platform-native logs first, then Prometheus/OpenTelemetry only when operational needs justify them.

## Selection rules

Apply `stacks/supabase.md` and the product profile. Prefer database-native constraints and tests over UI-only controls. Select the smallest compatible set. Never treat the existence of RLS as evidence that every table, RPC, storage bucket, Edge Function, or service-role path is protected.

## Implementation order

1. inventory schemas, roles, clients, functions, storage, and secrets;
2. classify data, users, and tenants;
3. verify RLS and policy coverage;
4. isolate privileged keys and server operations;
5. test migrations, RPCs, storage, and Edge Functions;
6. establish backup, restore, logs, alerts, and incident response;
7. run cross-tenant, revoked-access, failure, and rollback verification.

## Verification

Test anonymous, authenticated, cross-user, cross-tenant, service-role, storage, RPC, function, and direct-API paths. Run secret and dependency scans, build from clean migrations, restore a representative backup, and test rollback. A dashboard screenshot is not sufficient evidence.

## Human review

Database, security, privacy, and domain experts must review production policies, privileged functions, regulated data, destructive migrations, backup retention, public exposure, and any catalog-only candidate before it is treated as approved.
