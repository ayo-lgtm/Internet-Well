# Internet-Well Agent Skills

Skills are executable operating procedures for agents. Registry records describe resources; skills tell an agent how to perform work safely and how to prove the result.

## Lifecycle

- `approved/` — independently evaluated, prompt-injection reviewed, permission-bounded, reproducible, and human-reviewed.
- `experimental/` — useful but not yet proven for unsupervised critical work.
- `deprecated/` — preserved for migration and historical evidence; agents must not select them for new work.

No skill becomes approved from documentation or agent confidence alone.

## Experimental operating core

- `experimental/project-intelligence/SKILL.md` — inspect an authorized repository and produce an evidence-backed project assessment.
- `experimental/resource-selector/SKILL.md` — choose the smallest compatible registry-backed resource bundle and document rejected alternatives.
- `experimental/adoption-verifier/SKILL.md` — integrate an approved selection in reversible slices and verify real behavior.

Together they implement:

```text
inspect -> assess -> route -> select capabilities -> select resources
-> obtain approval -> adopt -> verify -> report residual risk
```

## Approval requirements

A skill may be promoted only after:

1. explicit inputs and schema-valid outputs;
2. clear read, write, external-action, and destructive-action boundaries;
3. prompt-injection and untrusted-input review;
4. representative fixture evaluations;
5. adversarial and failure-path tests;
6. real-project trials with fresh evidence;
7. truthful handling of blocked, failed, and unverified work;
8. reproducible evaluation transcripts;
9. competent human review.

The first end-to-end high-risk fixture is `evaluations/founder-os/lexura-scenario.md`.

## Agent rule

Never treat an experimental skill as production approval. Never set human-review status on behalf of a person. Never deploy, purchase, publish, communicate, trade, access production secrets, or perform destructive work merely because a skill describes how it could be done.
