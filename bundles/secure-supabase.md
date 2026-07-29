# Bundle: Secure Supabase

## Outcome

Establish defensible tenant isolation, data access, secrets handling, storage controls, migration safety, observability, backup, and recovery for a Supabase-backed product.

## Required capabilities

Schema ownership, RLS, policy testing, service-role isolation, authentication review, storage policies, Edge Function security, migration control, audit and logs, backup and restore, secrets detection, incident response, and production separation.

## Selection rules

Apply `stacks/supabase.md` and the product profile. Prefer database-native constraints and tests over UI-only controls. Select only compatible registry resources. Never treat the existence of RLS as evidence that every table and path is protected.

## Implementation order

1. inventory schemas, roles, clients, functions, storage, and secrets;
2. classify data and tenants;
3. verify RLS and policy coverage;
4. isolate privileged keys and server operations;
5. test migrations and storage;
6. establish backup, restore, logs, alerts, and incident response;
7. run cross-tenant and failure verification.

## Verification

Test anonymous, authenticated, cross-user, cross-tenant, service-role, storage, RPC, function, and direct-API paths; inspect policies; verify secrets; restore a representative backup; test migration rollback.

## Human review

Database, security, privacy, and domain experts must review production policies, privileged functions, regulated data, destructive migrations, backup retention, and public exposure.
