# Internet-Well Agent Connection Protocol

## Purpose

Define how an agent working in another repository consults Internet-Well without copying the Brain or bypassing its evidence and approval rules.

## Request envelope

A connected agent sends:

```json
{
  "goal": "outcome in founder language",
  "target_repository": "repository reference",
  "permission_scope": "read-only | scoped-write | explicit-action",
  "known_context": {
    "product_type": null,
    "stage": null,
    "users": [],
    "jurisdictions": [],
    "constraints": []
  },
  "requested_outputs": [
    "project-assessment",
    "selected-playbook",
    "capability-gaps",
    "resource-selection",
    "implementation-plan",
    "verification-plan"
  ]
}
```

## Required response

The Brain returns:

1. assessment conforming to `outputs/project-assessment.schema.json`;
2. selected playbook and rationale;
3. capability gaps;
4. resource bundle conforming to `outputs/resource-selection.schema.json`;
5. rejected alternatives;
6. required approvals;
7. ordered implementation plan;
8. verification plan;
9. evidence gaps and confidence;
10. no writes unless authorized.

## Connection modes

- **Repository reference:** agents read Internet-Well from GitHub and cite exact paths and pins.
- **Git submodule or checkout:** allowed for local read-only access; never vendor upstream resources.
- **Codex/agent skill:** package the routing procedures while keeping Internet-Well as source of truth.
- **MCP server:** expose assessment, selection, adoption planning, and verification as tools.
- **CLI/API/GitHub App:** future interfaces must enforce the same schemas and permission gates.

## Freshness and integrity

The client must identify the Internet-Well commit used. Stale registry records, failed CI, unresolved evidence debt, or modified generated files must be surfaced. A connected agent cannot silently upgrade Tier C evidence to production approval.

## Authority

Read-only consultation is the default. Product writes, installations, deployments, merges, purchases, account changes, external communications, trading, and destructive actions require explicit action-specific authorization.

## Example request

> Use Internet-Well at the current verified commit to assess this repository for launch. Preserve all existing product decisions. Return the project profile, critical journeys, capability gaps, smallest compatible resource bundle, rejected alternatives, approvals, implementation order, and verification gates. Do not modify anything.
