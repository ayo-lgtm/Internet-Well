# Skill: Governed Agentic Video Production

Status: **experimental**

## Purpose
Plan and supervise video-production work using the pinned OpenMontage integration while preserving Internet-Well's approval, licensing, credential, cost, privacy, and verification boundaries.

## Inputs
- video objective and intended audience;
- platform/output profile and duration;
- source assets and ownership/consent status;
- desired style and brand constraints;
- accessibility requirements;
- budget and permitted providers;
- confidentiality/data classification;
- publication target and approval owner.

## Procedure
1. Read `registry/marketing/openmontage.md` and the pinned integration entry.
2. Decide whether OpenMontage is needed. For a trivial trim, subtitle burn, or simple export, prefer a smaller tool.
3. If OpenMontage is justified, generate an integration plan with the exact verified commit. Do not use floating refs.
4. Before installation or execution, review:
   - AGPL-3.0 deployment implications;
   - install scripts and dependency graph;
   - external providers and credentials;
   - local binaries and GPU/runtime requirements;
   - network egress;
   - media/input trust boundaries;
   - cost limits and provider approval thresholds;
   - rollback and cleanup.
5. Preserve the production separation:
   - pipeline manifest = stages and gates;
   - stage skills = operating procedure;
   - tools = executable capability;
   - schemas = artifact contracts;
   - checkpoints = resumability/audit trail;
   - reviewers = quality and policy gates.
6. Obtain human approval before any paid provider call, use of confidential media, generation involving a real person's likeness/voice, or external publish action.
7. Require pre-render checks for asset availability, rights/consent, brand requirements, captions/subtitles, budget, and delivery promise.
8. Require post-render review for file validity, representative frames, audio, captions, accessibility, factual/brand claims, and platform requirements.
9. Keep a decision log containing providers considered, selected provider, fallbacks, estimated/actual cost, approvals, failures, and final verification evidence.
10. Return the finished artifact only after the relevant gates pass; otherwise return the failed gate and remediation path.

## Outputs
Return:
- selected production approach and why;
- exact upstream pin;
- provider/runtime plan;
- cost and approval gates;
- rights/consent checklist;
- accessibility plan;
- production stage checklist;
- verification evidence;
- residual risks;
- publish approval status.

## Permission boundary

This skill may plan and, when separately authorized, supervise execution within the approved local/project scope. It cannot spend money, use provider credentials, upload confidential media, clone or generate a real person's likeness or voice, publish externally, modify production systems, or accept new license obligations without the corresponding explicit authorization.

## Human review

Human review is mandatory before paid-provider use, confidential-media processing, material rights or consent decisions, public claims, use of a real person's likeness or voice, and final publication. AGPL deployment implications must be reviewed before modifying or network-deploying covered OpenMontage code.

## Prohibited shortcuts
- No vendoring OpenMontage into Internet-Well.
- No floating `main`/`latest` pin.
- No automatic paid API spend.
- No unreviewed use of confidential source media.
- No impersonation or unauthorized likeness/voice cloning.
- No automatic publication.
- No assertion that a render is valid merely because generation completed.

## Verification
Record the exact pin, commands executed, providers called, costs incurred, approvals captured, and post-render checks. If execution was not performed, say so explicitly.

## Evaluation

Pass when the exact upstream pin is recorded, the AGPL boundary is preserved, provider and budget decisions are auditable, required rights/consent and accessibility gates are completed, and the render passes post-production verification before release. Fail when generation completion is treated as proof of quality, costs or credentials are used without authorization, rights review is skipped, or publication occurs without human approval.
