# Internet-Well — The Founder OS Brain

Internet-Well helps founders and connected AI agents turn a goal into an evidence-backed plan, choose compatible open-source capabilities, implement them only with permission, and verify the integrated result.

It is designed to answer:

- What does this product need now?
- Which product, engineering, security, privacy, legal, accessibility, AI, infrastructure, marketing, finance, or operations capabilities are missing?
- Which verified resources fit this exact product, stack, stage, risk, and business model?
- Is a resource a production dependency, standard, template, reference implementation, agent runtime, or autonomous system?
- How should selected resources be combined, adopted, verified, updated, and removed?
- What can an AI agent do autonomously, and where is human review required?
- Which existing working repository can inform a capability without being blindly copied?

## Start here

- **Founders:** read [`START-HERE.md`](START-HERE.md).
- **AI agents:** read [`AGENTS.md`](AGENTS.md) before taking any action.
- **Architecture:** read [`FOUNDER-OS.md`](FOUNDER-OS.md).
- **Task routing:** use [`commands/`](commands/README.md).
- **End-to-end work:** choose from [`playbooks/`](playbooks/README.md).
- **Reusable selections:** use [`bundles/`](bundles/).
- **Product intelligence:** use [`profiles/`](profiles/).
- **Stack intelligence:** use [`stacks/`](stacks/).
- **Connected agents:** follow [`connections/AGENT-PROTOCOL.md`](connections/AGENT-PROTOCOL.md).
- **Resource roles:** read [`REFERENCE-TYPES.md`](REFERENCE-TYPES.md).

Do **not** begin by randomly browsing the registry. Define the outcome, assess the project, identify capability gaps, select a playbook and bundle, and only then choose resources.

## Operating flow

```text
Founder goal
  -> project assessment
  -> product and stack profile
  -> data and risk classification
  -> playbook selection
  -> capability gap analysis
  -> smallest compatible resource bundle
  -> adoption plan
  -> explicit authorization
  -> incremental implementation
  -> integrated verification
  -> decision record and continuous recheck
```

## Example connected-agent request

> Use Internet-Well at the current verified commit to assess this repository. Preserve all existing product decisions. Return the project profile, critical journeys, capability gaps, selected playbooks, smallest compatible resource bundle, rejected alternatives, approvals, implementation order, and verification gates. Do not modify anything without authorization.

## Repository layers

| Layer | Paths | Purpose |
|---|---|---|
| Agent entry and governance | `AGENTS.md`, `START-HERE.md`, `FOUNDER-OS.md` | Operating rules, authority, and architecture |
| Task routing | `commands/`, `playbooks/` | Convert goals into professional workflows |
| Decision intelligence | `capabilities/`, `profiles/`, `stacks/`, `bundles/`, `outputs/` | Profile projects and select compatible capability bundles |
| Agent execution | `skills/experimental/` | Project intelligence, resource selection, adoption, and verification procedures |
| Connection protocol | `connections/` | Contract for Codex and other agents working from another repository |
| Resource taxonomy | `REFERENCE-TYPES.md` | Distinguish dependencies, standards, references, runtimes, and autonomous systems |
| Verified knowledge | `registry/`, `evidence/`, `licenses/`, `evaluations/` | Establish what resources are trustworthy and under what restrictions |
| Governance and automation | `schemas/`, `automation/`, `.github/workflows/`, `METHODOLOGY.md`, `PHASES.md` | Enforce evidence, freshness, schemas, links, safety gates, tiers, and reproducibility |
| Rejections | `rejected/` | Preserve unsuitable candidates and reasons |

## Implemented product profiles

AI SaaS, legal tech, fintech, marketplaces, mobile apps, developer tools, internal enterprise tools, healthcare products, and autonomous agents.

## Implemented stack guides

Supabase, Next.js, React, Vercel, Railway, GitHub Actions, Python, Node.js, Docker, Cloudflare, AWS, and Lovable.

## Implemented professional playbooks

Full product build, existing-product audit, launch readiness, product-market fit, architecture review, security review, privacy and data governance, AI quality and safety, legal and compliance readiness, accessibility, incident response, operations and monitoring, infrastructure cost optimization, marketing, autonomous-agent readiness, open-source adoption, trading-system research, and decision simulation.

## Implemented reusable bundles

AI SaaS launch, legal-tech launch, secure Supabase, production Next.js, autonomous agent, accessibility baseline, observability baseline, privacy baseline, startup legal foundation, and full founder stack.

## Executable operating skills

- `skills/experimental/project-intelligence/` — inspect a repository and create an evidence-backed project assessment.
- `skills/experimental/resource-selector/` — choose the smallest compatible verified resource bundle and document rejected alternatives.
- `skills/experimental/adoption-verifier/` — integrate approved resources in reversible slices and prove the resulting behavior.

They remain experimental until fixture and real-project evaluations justify promotion.

## Machine-readable contracts

`outputs/` contains schemas for project assessment, resource selection, adoption plans, audits, and launch verdicts. CI validates JSON, operating-artifact structure, local links, registry references, and high-risk human-review gates.

## Lexura proof scenario

`evaluations/founder-os/lexura-scenario.md` tests whether the Brain correctly routes a high-risk multilingual legal-tech AI product, preserves explicit founder exclusions, and avoids reintroducing rejected features or unsupported case-outcome claims.

## Verified registry

Internet-Well does not copy upstream repositories. Each record points to a pinned upstream release or commit and documents evidence, limitations, license obligations, testing status, security findings, and required human review.

The registry is a decision input, not an install script. Popularity, expert reputation, stars, or score never override reproducibility, compatibility, risk, license, or restrictions.

### Approval tiers

| Tier | Meaning |
|---|---|
| A | Strong evidence, suitable license, strong posture, reproducibly tested, and competent human review |
| B | Generally reliable with documented limitations or dependencies |
| C | Promising or experimental; insufficient evidence for unsupervised critical use |
| D | Rejected, abandoned, unsafe, legally unsuitable, or unverifiable |

## Honest limits

Internet-Well cannot guarantee a bug-free launch, universal compliance, secure deployment under every configuration, successful product-market fit, profitable trading, viral content, reliable autonomous money generation, or accurate real-world prediction. It reduces avoidable mistakes, makes decisions traceable, surfaces risks early, and identifies when qualified human review is required.

## License

Internet-Well's original registry and operating content is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Upstream resources retain their own licenses, recorded in each registry entry.
