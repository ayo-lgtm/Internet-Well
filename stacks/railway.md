# Railway Stack Guide

## Detection

Look for Railway configuration, service variables, deployment references, database plugins, persistent volumes, health checks, and container or buildpack settings.

## Required controls

Service isolation, environment separation, secret scoping, health checks, restart behavior, database backups, volume persistence, network exposure, deployment provenance, observability, cost controls, rollback, and region awareness.

## Compatible capabilities

Container validation, infrastructure review, secrets management, database backup and restore, observability, uptime monitoring, deployment verification, cost analysis, incident response, and disaster recovery.

## Verification

Inspect service configuration; test health and failure behavior; confirm secrets are not embedded in images; verify database backup and restore; validate public exposure, logs, restart policy, deployment history, and rollback.

## Human review

Production databases, billing, domains, network exposure, persistent storage, regulated data, and destructive service changes require explicit authorization and qualified review.
