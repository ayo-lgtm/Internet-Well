# Internet-Well Founder OS Architecture

## Purpose

Internet-Well is an agent-accessible operating system for choosing and applying evidence-backed software-building capabilities. The registry is the knowledge layer; the Brain adds routing, project intelligence, selection, execution, verification, governance, and cross-repository connection.

## Operating model

```text
Founder goal
  -> authorized project inspection
  -> project assessment
  -> product and stack profiles
  -> data and risk classification
  -> playbook selection
  -> capability gap analysis
  -> smallest compatible bundle
  -> registry resource selection
  -> adoption and rollback plan
  -> explicit authorization
  -> incremental implementation
  -> independent integrated verification
  -> launch or operating decision
  -> continuous re-verification
```

## Layers

### 1. Knowledge

`registry/`, `evidence/`, `licenses/`, `evaluations/`, and `rejected/` establish what is known, how strongly it is known, what obligations apply, and what cannot be trusted.

### 2. Project intelligence

`skills/experimental/project-intelligence/`, `profiles/`, and `stacks/` identify the actual product, critical journeys, data, architecture, stage, current controls, constraints, and unknowns.

### 3. Decision intelligence

`commands/`, `playbooks/`, `capabilities/`, `bundles/`, `REFERENCE-TYPES.md`, and `outputs/` convert a goal into a traceable resource and implementation decision.

### 4. Execution

`skills/experimental/adoption-verifier/` applies authorized changes in reversible slices. Installation is never treated as proof of successful adoption.

### 5. Verification

Every implementation is tested through the target system's real interfaces where practical. Results distinguish passed, failed, blocked, and unverified work.

### 6. Connection

`connections/AGENT-PROTOCOL.md` defines how Codex and other agents consult the Brain from another repository while preserving commit identity, evidence, and authority boundaries.

### 7. Governance

`automation/verify_registry.py`, `automation/verify_founder_os.py`, generated indexes, schemas, and GitHub Actions enforce registry tiers, freshness, artifact structure, links, references, and high-risk review gates.

## Core objects

### Project assessment

Captures product type, stack, stage, hosting, users, jurisdictions, data classes, critical journeys, constraints, current controls, risks, unknowns, and permitted actions.

### Capability

An outcome-oriented need such as architecture, browser testing, secrets detection, incident response, accessibility, legal readiness, decision records, AI evaluation, marketing operations, or backup and restore.

### Resource

A verified tool, framework, standard, template, reference implementation, skill, runtime, autonomous system, dataset, benchmark, or provider. Its proposed role must be explicit.

### Bundle

The smallest compatible set of capabilities and resources needed for the outcome. Bundles identify overlap, dependencies, order, exclusions, verification, and human review.

### Playbook

An end-to-end professional workflow with inputs, workflow, outputs, evidence requirements, stop conditions, and authority boundaries.

### Decision record

The traceable explanation of what was selected, what was rejected, why, at which pin, under which assumptions, and with what confidence.

### Adoption plan

The scoped steps, pin, license obligations, data flows, approvals, verification, rollback, status, and remaining risk for an authorized resource integration.

## Risk classes

- **Low:** reversible local changes with no sensitive data or external effect.
- **Moderate:** changes affecting dependencies, CI, hosted environments, user experience, operational cost, or internal data.
- **High:** authentication, authorization, production data, security controls, legal/compliance, finance, trading, health, employment, regulated data, safety, irreversible actions, or external communications.

High-risk work requires explicit action-specific approval and qualified human review.

## Selection policy

1. Define the outcome and explicit exclusions.
2. Assess the project from evidence.
3. Identify mandatory capabilities independent of tools.
4. Apply product and stack guidance.
5. Search the registry for candidates.
6. Eliminate rejected, stale, incompatible, legally unsuitable, duplicative, or materially unverified candidates.
7. Prefer the smallest adequate bundle.
8. Document alternatives and why they lost.
9. Identify approvals, cost, data, licensing, maintenance, and rollback.
10. Verify the integrated result, not the installation command.

## Autonomy policy

Agents default to read-only consultation. Scope expands only through explicit authorization. Production, money, trading, purchases, publishing, communications, credentials, personal or regulated data, legal or medical decisions, and destructive actions require narrow permissions, logs, limits, stop conditions, rollback, and human review.

## Reference implementations

A repository can prove that a class of system is possible without proving that it is accurate, safe, profitable, legally suitable, or appropriate to copy. Internet-Well records its role, pin, license, evidence, restrictions, and clean-room boundary. MiroFish is an example: useful for decision-simulation architecture, not validated prediction.

## Definition of done

A Brain run is complete only when:

- the requested outcome and exclusions are explicit;
- the assessment and selection are traceable to current evidence;
- every mandatory capability is covered or marked blocked;
- authority boundaries were preserved;
- relevant checks ran against the integrated state;
- failures and unverified claims are disclosed;
- rollback and ownership are clear;
- required human reviews are identified;
- the founder can understand the current verdict and next decision.

## Promotion path

Experimental skills become approved only after fixture tests, adversarial evaluation, real-project trials, prompt-injection review, permission-boundary verification, schema-valid outputs, and competent human review. The Lexura scenario under `evaluations/founder-os/` is the first high-risk end-to-end fixture.
