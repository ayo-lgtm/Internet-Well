# Internet-Well — The Founder OS Brain

Internet-Well helps founders and AI agents turn a goal into an evidence-backed plan, select suitable open-source resources, implement them with permission, and verify the result.

It is designed to answer questions such as:

- What does this product need before launch?
- Which testing, security, compliance, infrastructure, marketing, or operations capabilities are missing?
- Which verified resources fit this exact product and stack?
- How should those resources be combined and added safely?
- What can an AI agent do autonomously, and where is human review required?
- Which existing repository can serve as a reference for a capability the founder wants to build?

## Start here

- **Founders:** read [`START-HERE.md`](START-HERE.md).
- **AI agents:** read [`AGENTS.md`](AGENTS.md) before taking any action.
- **Architecture:** read [`FOUNDER-OS.md`](FOUNDER-OS.md).
- **Task routing:** choose a procedure in [`commands/`](commands/README.md).
- **End-to-end work:** select a playbook in [`playbooks/`](playbooks/README.md).

Do **not** begin by randomly browsing the registry. Define the outcome, assess the project, identify capability gaps, and only then select resources.

## How it works

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
  -> verification evidence
```

## Example request

> Use Internet-Well to audit my Next.js and Supabase AI application for launch. Identify its critical journeys and capability gaps, select the appropriate verified resource bundle, explain rejected alternatives, implement only after authorization, and verify the integrated result.

## Repository layers

| Layer | Paths | Purpose |
|---|---|---|
| Agent entry and governance | `AGENTS.md`, `START-HERE.md`, `FOUNDER-OS.md` | Explain how humans and agents must operate |
| Task routing | `commands/`, `playbooks/` | Convert goals into ordered professional workflows |
| Decision intelligence | `capabilities/`, `profiles/`, `stacks/`, `outputs/` | Select capabilities and produce structured decisions |
| Agent execution | `skills/` | Packaged procedures with permission and evaluation boundaries |
| Verified knowledge | `registry/`, `evidence/`, `licenses/`, `evaluations/` | Establish what resources are trustworthy and under what restrictions |
| Governance and automation | `schemas/`, `automation/`, `METHODOLOGY.md`, `PHASES.md` | Enforce evidence, freshness, tiers, and reproducibility |
| Rejections | `rejected/` | Preserve unsuitable candidates and reasons |

## The verified registry

Internet-Well does not copy upstream repositories. Each record points to a pinned upstream release or commit and documents evidence, limitations, license obligations, testing status, security findings, and required human review.

The registry is a decision input, not an install script. Popularity and score never override compatibility, risk, or restrictions.

### Approval tiers

| Tier | Meaning |
|---|---|
| A | Strong evidence, suitable license, strong posture, reproducibly tested, and competent human review |
| B | Generally reliable with documented limitations or dependencies |
| C | Promising or experimental; insufficient evidence for unsupervised critical use |
| D | Rejected, abandoned, unsafe, legally unsuitable, or unverifiable |

## Current v2 capabilities

The first Founder OS operating layer includes:

- agent operating contract and authority boundaries;
- founder and agent onboarding;
- project assessment and resource-selection commands;
- product-audit, launch-readiness, and decision-simulation playbooks;
- outcome-oriented capability graph;
- AI SaaS and Supabase guidance;
- machine-readable project-assessment and resource-selection schemas;
- the original verified registry and evidence system.

Additional profiles, stack guides, professional playbooks, bundles, and evaluated agent skills will be added incrementally.

## Honest limits

Internet-Well cannot guarantee a bug-free launch, universal compliance, secure deployment under every configuration, successful product-market fit, profitable trading, virality, or accurate real-world prediction. It reduces avoidable mistakes, makes decisions traceable, surfaces risks early, and identifies when qualified human review is required.

## License

Internet-Well's original registry and operating content is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Upstream resources retain their own licenses, recorded in each registry entry.
