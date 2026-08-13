# Human review and Tier A governance

## Purpose

Automation may collect evidence, run tests, and propose a disposition. It may not assign Tier A. Tier A requires a competent human reviewer who accepts responsibility for the reviewed scope.

## Reviewer qualifications

A reviewer must have demonstrable experience relevant to the reviewed domain, such as application security, identity, infrastructure, privacy, accessibility, legal operations, AI evaluation, or product engineering. Reputation, stars, employer name, or model-generated credentials are not sufficient evidence.

## Required disclosure

The reviewer must record:

- name or stable professional identity;
- relevant expertise;
- relationship to the project or upstream resource;
- financial or employment conflicts;
- scope reviewed;
- evidence examined;
- tests independently reproduced;
- limitations and unresolved questions;
- approval, restriction, or rejection decision;
- review date and expiration date.

## Review standard

The reviewer must independently confirm:

1. canonical source and exact version or commit;
2. license and material redistribution or hosted-use obligations;
3. maintenance and security posture;
4. reproducible installation or execution where applicable;
5. compatibility with the claimed use case;
6. documented failure modes and restrictions;
7. accuracy of the registry record;
8. sufficiency of tests for the assigned tier;
9. absence of unsupported security, legal, compliance, or quality claims.

## Approval record

Tier A approval must be represented by a reviewed pull request or signed review record referencing:

- registry path;
- exact pin;
- evidence paths;
- test run or artifact identifiers;
- reviewer identity;
- decision and restrictions;
- expiration or re-review trigger.

## Re-review triggers

A Tier A record returns to Tier B or pending review when any of the following occurs:

- major version change;
- license change;
- ownership or governance change;
- material security advisory;
- architecture or deployment-model change;
- failed reproducibility check;
- unsupported upstream status;
- evidence expiration;
- material contradiction discovered in production use.

## Prohibited practices

- self-approval without disclosed conflict;
- model-generated or fabricated reviewer identity;
- approval based solely on documentation or popularity;
- approval of legal or regulatory sufficiency outside the reviewer’s competence;
- permanent approval without re-review triggers;
- deletion of prior restrictions or dissenting evidence.
