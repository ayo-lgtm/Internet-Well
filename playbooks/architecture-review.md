# Playbook: Architecture Review

## Purpose

Evaluate whether the system structure supports the product's critical journeys, security, reliability, maintainability, cost, and expected scale without unnecessary complexity.

## Inputs

Project assessment, diagrams, repositories, deployment topology, data stores, integrations, workloads, incidents, performance evidence, constraints, and future requirements.

## Workflow

1. Map context, containers, components, data flows, trust boundaries, and external dependencies.
2. Trace critical journeys end to end.
3. Review coupling, ownership, failure domains, consistency, concurrency, caching, queues, migrations, portability, and recovery.
4. Identify accidental complexity, single points of failure, hidden state, and unsupported scale assumptions.
5. Record material decisions and alternatives.
6. Select documentation, decision-record, testing, observability, and infrastructure resources only for actual gaps.
7. Produce a staged target architecture with compatibility and rollback.

## Outputs

Current architecture map, critical-flow analysis, risks, decision records, selected resources, target-state options, migration order, and verification gates.

## Verification

Validate diagrams against code and deployment configuration; exercise critical boundaries; test failure and recovery paths; compare performance and cost assumptions with evidence.

## Stop conditions

Stop before broad rewrites, data migrations, platform replacement, or production infrastructure changes without approved acceptance criteria and rollback.

## Human review

Senior engineering, security, data, and domain owners must review high-risk architecture, migrations, authentication, regulated data, production resilience, and material cost commitments.
