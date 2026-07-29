# Stack Guide: Supabase

## Scope

Use for products relying on Supabase Database, Auth, Storage, Edge Functions, Realtime, or related services.

## Required review areas

- schema and migration ownership;
- Row Level Security on every exposed table;
- service-role key isolation;
- authentication and authorization boundaries;
- storage bucket policies;
- Edge Function secrets and external data flows;
- tenant isolation;
- backup, restore, and migration procedures;
- logs, rate limits, abuse controls, and cost monitoring;
- local, preview, staging, and production separation.

## Selection guidance

Pair database changes with migration tooling and tests. Use PostgreSQL guidance for schema and query design. Use secrets detection before commits. Use browser and integration tests for authenticated critical journeys. Security scanners do not replace explicit RLS and authorization tests.

## High-risk mistakes

- exposing a service-role key to a client;
- relying on frontend checks instead of RLS;
- permissive storage policies;
- testing only as an administrator;
- applying production SQL manually without versioned migrations;
- assuming backups have been verified without a restore test;
- sending user data to AI or analytics providers without mapping and approval.

## Verification minimum

Demonstrate anonymous, normal-user, cross-tenant, privileged, and revoked-access behavior. Verify migrations from a clean state and test a restore path where the product risk justifies it.
