# Playbook: Operations and Monitoring

## Purpose

Create an operating system that detects failures, supports users, protects data, controls change, and restores critical services.

## Inputs

Project assessment, critical journeys, service map, owners, SLOs, incidents, logs, metrics, traces, support channels, backups, vendors, and deployment processes.

## Workflow

1. Define critical services, journeys, owners, dependencies, and acceptable failure.
2. Establish service indicators, objectives, dashboards, alerts, and escalation.
3. Review logs, metrics, traces, privacy, retention, and access.
4. Map deployment, rollback, change management, support, incident response, backup, restore, and continuity.
5. Eliminate noisy alerts and blind spots.
6. Select monitoring, uptime, logging, backup, runbook, and incident resources according to scale and risk.
7. Rehearse representative failure and recovery scenarios.

## Outputs

Service catalog, ownership, SLOs, dashboards, alerts, runbooks, selected resources, backup and recovery plan, incident flow, and operating cadence.

## Verification

Trigger safe synthetic failures; verify alerts reach owners; test dashboards and logs; restore from backup; execute rollback; measure recovery; confirm privacy and access controls.

## Stop conditions

Stop before production failover, destructive recovery, paging external teams, or changing retention and monitoring of sensitive data without authorization.

## Human review

Operations, security, privacy, data, and business owners must review production SLOs, on-call duties, regulated logs, backup policy, disaster recovery, and customer-impacting changes.
