# Executable Vibe Integrations

Internet-Well does not merely list these resources. Version 0.3.1 includes a controlled integration manager that can inspect, plan, pin, and—only after explicit approval—install or connect eligible resources.

## Commands

```bash
internet-well-integrations list
internet-well-integrations show taste-skill
internet-well-integrations plan animejs --ref 4.0.0
internet-well-integrations plan anthropic-skills --ref <exact-commit>
internet-well-integrations install animejs --ref 4.0.0 --approve
```

Planning never executes third-party code. Installation requires `--approve`, and open-source integrations reject floating refs such as `latest`, `main`, `master`, or `HEAD`.

## Integration models

### Selective skill adoption

Used for Anthropic Skills, Taste Skill, Humanizer, and React Bits. Internet-Well pins a source checkout for inspection. Users must select and adopt only the reviewed files or components rather than copying an entire upstream repository by default.

### Package or CLI adapter

Used for Anime.js, Agent Browser, and the Skills CLI. Internet-Well generates a pinned command and can execute it only after approval. A successful installation is not approval of runtime behavior.

### Pinned reference implementation

Used for Get Shit Done and Storyscope. Internet-Well creates a detached checkout at an exact ref. These sources remain references until their license, scripts, behavior, and measurable benefit have been reviewed.

### Hosted provider integration

Used for Shader Gradient, Jitter, Refero, and 10x App Builder. Internet-Well does not copy unavailable website code. It generates a provider-review and consent record covering terms, retention, training use, data residency, ownership, exportability, deletion, security, and relevant quality gates.

## Approval boundaries

Separate approval is required for:

- installing third-party code;
- browser sessions or authenticated accounts;
- external form submissions, messages, purchases, publishing, deployment, or account changes;
- sending private code or assets to hosted providers;
- copying any upstream file into a product repository;
- production use.

## Verification after integration

Every integration must be tested against a matched baseline and record:

- exact source and pin;
- license result;
- inspected scripts and dependencies;
- requested permissions and network destinations;
- quality improvement or regression;
- token, time, and cost impact;
- accessibility and performance impact where relevant;
- rollback method;
- human-review decision.

The executable adapter is a governed path to use a resource. It is not a declaration that the upstream resource is safe, appropriate, or Tier A.
