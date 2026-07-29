# Playbook: Cost and Infrastructure Optimization

## Purpose

Reduce unnecessary infrastructure and provider cost without degrading critical journeys, security, reliability, or future reversibility.

## Inputs

Architecture, usage, bills, resource metrics, provider contracts, performance, incidents, growth assumptions, environments, and operational constraints.

## Workflow

1. Establish current cost by service, environment, user, request, workload, and business outcome.
2. Identify idle resources, overprovisioning, duplicate providers, inefficient queries, storage growth, egress, model usage, and avoidable operational labor.
3. Separate safe efficiency changes from architecture or vendor migrations.
4. Model savings, engineering effort, switching cost, risk, and break-even.
5. Select profiling, observability, infrastructure, database, and cost resources only for material opportunities.
6. Implement reversible changes from lowest to highest risk.
7. Measure savings and service quality after each change.

## Outputs

Cost baseline, drivers, prioritized opportunities, selected resources, savings ranges, implementation order, guardrails, rollback, and measured outcomes.

## Verification

Compare before and after cost and usage; run load and critical-journey checks; verify reliability, latency, data integrity, security, and provider billing; disclose incomplete billing periods.

## Stop conditions

Stop before deleting resources, changing production capacity, entering paid commitments, moving regulated data, or accepting service degradation without authorization.

## Human review

Finance, engineering, security, data, legal, and business owners must review material commitments, migrations, production capacity changes, regulated data, and savings claims.
