# Internet-Well v0.5 — Agent Reliability Layer

Internet-Well's reliability layer measures whether an agent selected the right resources, stayed within policy, completed observable acceptance criteria, and can prove the result. An agent saying that work is complete is never sufficient evidence by itself.

## Architecture

The reliability layer has five connected parts:

1. **Benchmark suite** — repeatable scenarios covering capability selection, compliance, web extraction, MCP selection, local models, design handoff, and production code changes.
2. **Trajectory tracing** — records goal, stages, actions, evidence, failures, approvals, cost, latency, and final state.
3. **Independent completion verifier** — returns `PASS`, `FAIL`, or `HUMAN_REVIEW` from observable criteria and evidence rather than agent self-report.
4. **Failure memory** — sanitizes failed runs and converts them into reusable regression cases.
5. **Release gate** — Tier A or otherwise sensitive work cannot be treated as production-ready without the required human review and existing authorization boundaries.

## CLI

```bash
internet-well-reliability scenarios
internet-well-reliability trace-new "select a production analytics stack"
internet-well-reliability evaluate selfhosted-analytics-selection run.json
internet-well-reliability verify production-code-change run.json
internet-well-reliability suite runs.json
internet-well-reliability regression authorized-web-extraction failed-run.json
```

A run JSON should contain criterion results, evidence references, and metrics. Criterion values may be booleans or objects such as:

```json
{
  "criteria": {
    "license-verified": {"passed": true, "evidence": ["license-check:commit-sha"]}
  },
  "evidence": ["ci:run-123", "runtime:test-456"],
  "metrics": {
    "policy_violations": 0,
    "unverified_claims": 0,
    "hallucinated_claims": 0,
    "required_tests_failed": 0
  }
}
```

## Release semantics

`PASS` means the scenario met its machine-verifiable criteria and no hard failure was detected. `HUMAN_REVIEW` means machine-verifiable criteria passed but the risk tier or policy requires a person to approve the consequential next step. `FAIL` means observable criteria, evidence, thresholds, or hard safety conditions were not satisfied.

The verifier cannot grant credentials, approve regulated work, authorize production deployment, waive legal review, bypass security controls, or override any other Internet-Well approval boundary.

## Failure memory and regressions

Failed and human-review runs can be converted into sanitized regression fixtures. Secret-like fields are removed before storage. The regression assertion prevents a future evaluator from returning `PASS` while the original failure condition remains unresolved. This creates a measurable self-improvement loop: trace a real failure, convert it into an eval, fix the system, and keep the regression permanently.

## Observability contract

A useful trace should preserve: goal, source/capability selection, verification evidence, rejected alternatives, tool calls, approvals, failures, runtime evidence, cost, latency, and final state. Production integrations should attach stable evidence references rather than copying private data into public traces.

## Acceptance-gate principle

No workflow should be considered complete merely because its execution path ended successfully. Completion requires proof against scenario-specific acceptance criteria. For code changes, that means the requested behavior, tests, security checks, rollback path, and independent verifier outcome. For compliance work, it means preserving the independent-attestation boundary. For external-system actions, it means explicit authority and least privilege.
