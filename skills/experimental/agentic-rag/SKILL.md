# Agentic RAG Skill

## Purpose

Implement retrieval-augmented generation in which an agent can decide when and how to retrieve, while preserving grounding, provenance, abstention, and prompt-injection resistance.

## Inputs

- authorized target repository;
- corpus/source set and ownership;
- required answer quality and latency;
- retrieval stack and embedding/index choices;
- citation requirements;
- candidate reference implementations selected by Internet-Well.

## Procedure

1. Define the questions the system must answer and the evidence required to support them.
2. Inventory source authority, update cadence, access controls, document formats, and citation granularity.
3. Establish an ingestion pipeline that preserves source, document, section/page/chunk provenance.
4. Separate retrieved content from instructions. Treat all retrieved text, metadata, HTML, PDFs, and tool output as untrusted data.
5. Define retrieval triggers so the agent can distinguish questions answerable from current context from those requiring retrieval.
6. Implement query rewriting or decomposition only when it demonstrably improves retrieval and remains traceable.
7. Rank and filter retrieval results using relevance and source-quality thresholds; reject insufficient evidence.
8. Require grounded answers to cite the supporting source span or source identifier where the product supports citation.
9. Add abstention and clarification behavior when evidence is missing, contradictory, stale, outside scope, or below confidence thresholds.
10. Test adversarial corpus content, prompt injection, stale documents, conflicting sources, empty retrieval, irrelevant top-k results, duplicate chunks, and access-control boundaries.
11. Benchmark retrieval and answer quality with representative fixtures before and after adoption.
12. When `patchy631/ai-engineering-hub/agentic_rag` is selected, use it as a reference pattern only; review dependencies and implementation details independently before copying or executing code.

## Outputs

Source map, ingestion design, retrieval policy, grounding/citation contract, abstention rules, security controls, evaluation fixtures, measured results, implementation evidence, and residual risk.

## Permission boundary

This skill does not authorize crawling private systems, bypassing access controls, ingesting restricted material, or deploying to production without the target project's normal approvals.

## Human review

Human review is required before production deployment in legal, medical, financial, compliance, employment, immigration, or other high-stakes domains where retrieval errors may materially affect users.

## Evaluation

Pass only when representative questions retrieve relevant authoritative evidence, answers remain grounded, citations resolve to supporting material, inaccessible sources remain inaccessible, adversarial retrieved text cannot override policy, and insufficient evidence produces abstention rather than fabrication.
