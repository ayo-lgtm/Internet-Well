# Internet-Well Founder OS

## Purpose

Internet-Well is an agent-accessible operating system for choosing and applying evidence-backed software-building capabilities. Its registry is the knowledge layer; the OS adds routing, selection, execution, and verification.

## Operating model

```text
Founder goal
  -> project assessment
  -> product and stack profile
  -> risk classification
  -> playbook selection
  -> capability gap analysis
  -> resource bundle selection
  -> adoption plan
  -> authorized implementation
  -> independent verification
  -> evidence-backed decision record
```

## Layers

### 1. Knowledge

`registry/`, `evidence/`, `licenses/`, `evaluations/`, and `rejected/` establish what is known, how strongly it is known, and what cannot yet be trusted.

### 2. Decision

`commands/`, `playbooks/`, `capabilities/`, `profiles/`, and `stacks/` convert a goal into a compatible resource bundle and ordered plan.

### 3. Execution

`skills/` packages repeatable procedures. An agent may execute only within its permission boundary and must preserve human approval gates.

### 4. Verification

Every implementation must be checked through the target project's real interfaces where practical. Registry validation does not prove that a particular integration works.

## Core objects

### Project profile

Captures product type, stack, stage, hosting, users, jurisdictions, data classes, critical journeys, constraints, and permitted actions.

### Capability

An outcome-oriented need such as browser testing, secrets detection, incident response, accessibility testing, architecture documentation, decision records, or AI evaluation.

### Resource

A tool, framework, standard, template, reference implementation, or skill that may satisfy part of a capability.

### Bundle

The smallest compatible set of resources needed for the target outcome. Bundles must identify overlaps, dependencies, ordering, and exclusions.

### Playbook

An end-to-end workflow with inputs, selection rules, execution sequence, outputs, verification requirements, and stop conditions.

### Decision record

The traceable explanation of what was selected, what was rejected, why, under which assumptions, and with what confidence.

## Risk classes

- **Low:** reversible local changes with no sensitive data or external effect.
- **Moderate:** changes affecting CI, dependencies, hosted environments, user experience, or operational cost.
- **High:** authentication, authorization, production data, legal/compliance, financial behavior, security controls, regulated data, safety, or irreversible actions.

High-risk work requires explicit approval and qualified human review where the registry says so.

## Capability-selection policy

1. Define the outcome.
2. Identify mandatory capabilities independent of tools.
3. Search the registry for candidates.
4. Eliminate incompatible, stale, legally unsuitable, or unverified candidates.
5. Prefer the smallest adequate bundle.
6. Document rejected alternatives.
7. Add implementation-specific controls from the relevant stack guide.
8. Verify the resulting system, not merely the installation command.

## Definition of done

A run is complete only when:

- the requested outcome is mapped to acceptance criteria;
- the selection is traceable to current registry evidence;
- implementation stayed within authorization;
- relevant checks ran against the integrated state;
- failures and unverified claims are disclosed;
- a founder can understand the result and the next decision.

## Product direction

Internet-Well should eventually expose this operating model through agent skills, machine-readable routing, a capability graph, and optional interfaces. The repository remains the source of truth; interfaces must not bypass its evidence and approval rules.
