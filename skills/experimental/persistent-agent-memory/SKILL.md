# Persistent Agent Memory Skill

## Purpose

Add durable, scoped memory to an authorized agent system without turning stored content into an untrusted instruction channel or uncontrolled data store.

## Inputs

- authorized target repository;
- memory use case and success criteria;
- current persistence stack;
- tenant/user boundaries;
- data classification and retention requirements;
- candidate implementations selected through the Internet-Well resource selector.

## Procedure

1. Confirm that persistence is actually required; prefer request-local context when durable memory is unnecessary.
2. Inspect the existing database, vector store, cache, MCP services, authentication model, tenant model, and deletion paths before introducing new infrastructure.
3. Define memory classes: durable facts, episodic history, task state, derived summaries, and disposable working context.
4. Define explicit write rules for each class, including who or what may write, required provenance, confidence, and expiry.
5. Treat retrieved memory as data, never as higher-priority instructions. Delimit it from system, developer, and user instructions.
6. Implement tenant isolation and object-level authorization before retrieval quality optimizations.
7. Add provenance fields sufficient to identify source, writer, timestamp, and transformation history.
8. Add retention, deletion, correction, and stale-memory behavior. A user or operator must be able to remove durable memory where the product requires it.
9. Add retrieval ranking and relevance thresholds. Do not inject unrelated low-confidence memory into prompts.
10. Test restart survival, correct recall, stale-memory handling, deletion, cross-tenant isolation, malformed content, prompt injection in stored memory, duplicate memory, and storage failure.
11. Record the exact upstream reference and commit used, including `patchy631/ai-engineering-hub/agent-with-mcp-memory` when selected.
12. Emit verification evidence and residual risks before claiming completion.

## Outputs

Memory architecture, schema, write policy, retrieval policy, retention/deletion rules, tenant-isolation evidence, injection-resistance evidence, implementation diff, tests, and residual risks.

## Permission boundary

This skill does not authorize production secrets access, migration of regulated data, irreversible schema deletion, cross-tenant data access, or deployment. Such actions require the target project's normal approval process.

## Human review

Human review is required before production use involving privileged, regulated, financial, health, legal-client, employee, authentication, or other sensitive data.

## Evaluation

Pass only when memory survives the intended lifecycle, retrieves relevant entries, excludes unrelated tenants/users, supports required deletion/correction, preserves provenance, and stored malicious instructions cannot alter higher-priority agent policy. Fail if persistence merely works in the happy path while isolation, deletion, or injection controls remain unverified.
