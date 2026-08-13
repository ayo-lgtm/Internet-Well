# Internet-Well — The Founder OS Brain

> **Developer Preview v0.3.0.** Internet-Well performs local, preliminary repository assessment and governed planning. It is not a penetration test, legal opinion, privacy certification, or production approval.

Internet-Well helps founders and connected AI agents turn a product goal into an evidence-backed plan, choose compatible open-source capabilities, preserve explicit product decisions, and identify where qualified human review is required.

## Privacy-first by default

Internet-Well does not upload source code or findings. The CLI runs locally, redacts absolute project and home-directory paths by default, classifies reports as `private`, identifies potentially sensitive filenames without reading their contents, and refuses to write reports inside the assessed Git repository unless explicitly authorized.

Private projects do not need to be published. Keep their reports in a separate private location and never commit confidential findings to this public repository. Public examples in this repository must be synthetic or derived only from intentionally public material. Read [`docs/PRIVACY-AND-DATA-HANDLING.md`](docs/PRIVACY-AND-DATA-HANDLING.md) before assessing proprietary, regulated, privileged, or personal data.

## Install

Use a tagged release or verified commit:

```bash
python3 -m pip install .
internet-well --version
internet-well-integrations list
```

## Five-minute local assessment

Write private reports outside the assessed repository:

```bash
mkdir -p "$HOME/.internet-well/reports"

internet-well assess /path/to/project \
  --classification private \
  --format markdown \
  --output "$HOME/.internet-well/reports/assessment.md"

internet-well plan /path/to/project \
  --goal "prepare a safe public launch" \
  --classification private \
  --format markdown \
  --output "$HOME/.internet-well/reports/plan.md"

internet-well security /path/to/project \
  --classification private \
  --format markdown \
  --output "$HOME/.internet-well/reports/security-plan.md"
```

Every output contains a preliminary-assessment notice, report classification, local-processing declaration, path-redaction status, and privacy gate.

A synthetic public report example is available at [`examples/assessment-example.md`](examples/assessment-example.md). It does not describe a real private product or production environment.

## CodeWiki and documentation providers

The `docs` command generates a provider-neutral documentation manifest. Hosted CodeWiki use requires explicit consent after reviewing retention, model-training, access, deletion, subprocessors, data-residency, and incident terms:

```bash
internet-well docs /path/to/project \
  --provider codewiki \
  --provider-consent \
  --classification private \
  --output "$HOME/.internet-well/reports/docs-manifest.json"
```

Prefer a local or self-hosted documentation provider for confidential repositories. CodeWiki is a documentation and onboarding layer, not Internet-Well's security, compliance, legal, privacy, or launch authority.

## Commands

- `assess` — preliminary project, stack, risk, and capability assessment.
- `plan` — evidence-backed resource and implementation planning.
- `security` — preliminary security capability planning; not a penetration test.
- `launch-review` — preliminary launch-readiness planning; not an approval.
- `docs` — governed documentation manifest for CodeWiki-style systems.

Important options:

- `--classification private|internal|shareable` — defaults to `private`.
- `--include-paths` — opt in to absolute local paths.
- `--allow-in-repo-output` — override the default report-write protection.
- `--provider-consent` — required for hosted CodeWiki.

## Vibe Coder Intelligence

Internet-Well includes a governed layer for portable agent skills, design resources, browser runtimes, long-running coding workflows, writing tools, component libraries, animation engines, hosted app generators, and code-minimization review skills.

The layer is executable, not merely a catalog. Use:

```bash
internet-well-integrations list
internet-well-integrations show agent-browser
internet-well-integrations plan animejs --ref 4.0.0
internet-well-integrations plan anthropic-skills --ref <exact-commit>
internet-well-ponytail show
internet-well-ponytail plan --ref v4.8.4
```

Execution requires explicit approval:

```bash
internet-well-integrations install animejs --ref 4.0.0 --approve
internet-well-ponytail install --ref v4.8.4 --approve
```

The managers reject floating refs such as `latest`, `main`, `master`, and `HEAD`. They distinguish selective skill adoption, package or CLI adapters, pinned reference implementations, and hosted-provider consent records.

Start with:

- [`catalog/vibe-coder-resources.json`](catalog/vibe-coder-resources.json) — machine-readable candidates and restrictions;
- [`integrations/vibe/manifest.json`](integrations/vibe/manifest.json) — executable adapter contract for 14 governed resources;
- [`integrations/vibe/ponytail.json`](integrations/vibe/ponytail.json) — Ponytail-specific adapter and safety contract;
- [`docs/EXECUTABLE-VIBE-INTEGRATIONS.md`](docs/EXECUTABLE-VIBE-INTEGRATIONS.md) — usage and approval boundaries;
- [`bundles/vibe-coder-intelligence.md`](bundles/vibe-coder-intelligence.md) — selection and adoption rules;
- [`governance/AGENT-SKILL-SUPPLY-CHAIN.md`](governance/AGENT-SKILL-SUPPLY-CHAIN.md) — skill supply-chain controls.

The governed resource set covers Anthropic Agent Skills, skills.sh, Agent Browser, Get Shit Done, Taste Skill, Humanizer, Storyscope, React Bits, Anime.js, Shader Gradient, Jitter, Refero, 10x App Builder, and Ponytail.

A marketplace position, social-media recommendation, star count, or install count is not approval. Skills and providers must be pinned, inspected, permission-bounded, compared against a no-skill baseline, tested in a fixture, and reviewed before critical use.

## Operating flow

```text
Founder goal
  -> local project assessment
  -> product, stack, data, and risk profile
  -> capability gap analysis
  -> smallest compatible verified bundle
  -> explicit authorization
  -> reversible implementation
  -> runtime and integrated verification
  -> human review where required
  -> launch decision record
```

## What Internet-Well does not do

Internet-Well cannot guarantee a bug-free launch, universal compliance, secure deployment under every configuration, successful product-market fit, profitability, virality, or accurate real-world prediction. Static assessment cannot prove runtime authorization, database isolation, exploit resistance, accessibility behavior, deployment correctness, or legal compliance.

Use its output to guide deeper testing and qualified review—not to replace them.

## Repository map

- [`START-HERE.md`](START-HERE.md) — founder entry point.
- [`AGENTS.md`](AGENTS.md) — mandatory agent operating contract.
- [`FOUNDER-OS.md`](FOUNDER-OS.md) — architecture and operating model.
- [`commands/`](commands/README.md) and [`playbooks/`](playbooks/README.md) — workflows.
- [`bundles/`](bundles/) — reusable capability selections.
- [`registry/`](registry/) — verified resources, limitations, licenses, and evidence.
- [`integrations/vibe/manifest.json`](integrations/vibe/manifest.json) — governed executable integration adapters.
- [`governance/HUMAN-REVIEW.md`](governance/HUMAN-REVIEW.md) — Tier A and reviewer controls.
- [`governance/AGENT-SKILL-SUPPLY-CHAIN.md`](governance/AGENT-SKILL-SUPPLY-CHAIN.md) — portable skill and marketplace controls.
- [`docs/PRIVACY-AND-DATA-HANDLING.md`](docs/PRIVACY-AND-DATA-HANDLING.md) — privacy rules.
- [`SECURITY.md`](SECURITY.md) — responsible disclosure.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and public-data rules.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — community expectations.

## Evidence tiers

| Tier | Meaning |
|---|---|
| A | Strong evidence plus qualified, conflict-disclosed human review |
| B | Generally reliable with documented limitations or dependencies |
| C | Promising or experimental; supervised critical use only |
| D | Rejected, abandoned, unsafe, legally unsuitable, or unverifiable |

Automation cannot assign Tier A.

## Contributing

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request. Do not submit credentials, private repository findings, customer data, personal data, privileged material, or unpublished product assessments. Use synthetic fixtures for tests and documentation.

## Public release posture

Version `0.3.0` is suitable for supervised public developer use, local assessment of repositories the user is authorized to inspect, and governed third-party integration planning. It is not an autonomous modification authority or professional certification service.

## License

Internet-Well uses a split licensing model so software and non-software material are governed appropriately:

- **Software code and executable configuration:** Apache License 2.0. See [`LICENSE`](LICENSE). This software-specific license is the package license declared in `pyproject.toml`.
- **Original documentation, registry prose, governance text, and other non-software content previously published as CC-BY-4.0:** those CC-BY-4.0 permissions are not revoked. Where a file or directory carries a more specific notice, that notice controls.
- **Third-party resources and integrations:** retain their own upstream licenses and terms. Internet-Well's cataloging of a resource does not relicense that resource.

The Apache-2.0 grant is an additional software-specific permission for Internet-Well's software; it does not narrow permissions already granted under CC-BY-4.0 for previously published material.
