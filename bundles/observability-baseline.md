# Bundle: Observability Baseline

## Outcome

Make critical user and system failures detectable, diagnosable, owned, and recoverable without collecting unnecessary sensitive data.

## Required capabilities

Service catalog, critical-journey indicators, structured logs, metrics, traces where justified, error monitoring, uptime checks, dashboards, alerts, ownership, runbooks, retention, privacy, and incident integration.

## Selection rules

Select the smallest system that covers current scale and risks. Prefer existing platform telemetry when adequate. Avoid duplicate providers, uncontrolled high-cardinality data, sensitive payload logging, and alerts without owners or action.

## Implementation order

1. define services, journeys, owners, and failure objectives;
2. instrument errors and key indicators;
3. add dashboards and actionable alerts;
4. establish privacy, access, and retention;
5. connect runbooks and incidents;
6. test alert and diagnosis paths.

## Verification

Trigger safe synthetic failures; confirm logs, metrics, traces, uptime checks, dashboards, alert delivery, ownership, retention, redaction, and incident links; measure noise and blind spots.

## Human review

Operations, security, privacy, and service owners must review production telemetry, sensitive fields, retention, paging, regulated data, and incident thresholds.
