# Internet-Well Resource Role Taxonomy

Every registry record must be interpreted by role before an agent recommends adoption.

## Production dependency

Software directly added to a product or operational environment. Requires compatibility, license, security, maintenance, rollback, and integration verification.

## Framework

A reusable architecture or application foundation. Adoption may shape public interfaces and long-term maintenance; evaluate switching cost and ecosystem boundaries.

## Standard

A normative or professional benchmark that defines expected controls or outcomes. Standards guide assessment; they are not installed.

## Template

Reusable documents, configuration, or starter structure. Agents must adapt it to the project and verify assumptions rather than treating it as authoritative.

## Reference implementation

A working example used to study architecture, workflows, or design choices. It is not automatically suitable for copying or production. License and clean-room boundaries matter.

## Agent skill

A packaged procedure for an AI agent. It must declare inputs, outputs, authority, evaluation, failure handling, and human-review gates.

## Agent runtime

Infrastructure that hosts or orchestrates agents, tools, memory, planning, or workflows. Requires threat modeling, tool authorization, observability, and containment.

## Autonomous system

A system that can plan and act toward a goal with limited supervision. It requires explicit action budgets, stop conditions, approvals, audit logs, recovery, and independent evaluation. Claims that it can reliably make money, trade profitably, go viral, or complete arbitrary tasks are never accepted without reproducible evidence and domain review.

## Dataset or benchmark

Evidence used for training or evaluation. Confirm provenance, license, representativeness, contamination risk, privacy, and measurement validity.

## Service or provider

A hosted capability. Assess pricing, data flows, retention, region, portability, lock-in, account permissions, and failure behavior.

## Selection rule

A resource can serve multiple roles, but the selection record must identify the exact role proposed for the target project. Agents must not turn a reference implementation into a production dependency or an experimental autonomous system into an unsupervised operator without a new review.
