# Internet-Well Release Policy

Internet-Well releases are evidence snapshots, not guarantees that every upstream project remains safe or current forever.

## Versioning

Internet-Well uses semantic versioning:

- patch: corrections, refreshed evidence, and compatible verification improvements;
- minor: new commands, bundles, profiles, tranches, schemas, or compatible behavior;
- major: incompatible CLI, schema, governance, or selection-policy changes.

The CLI, `VERSION`, and `pyproject.toml` must contain the same version.

## Release gate

A release may be tagged only when:

1. the main verification workflow passes;
2. all specialized verification workflows affected by the change pass;
3. the installable package builds and installs in a clean environment;
4. CLI JSON and Markdown smoke tests pass;
5. the generated registry index is current;
6. catalog coverage is reported;
7. open evidence debts and known limitations remain visible;
8. no automation has assigned Tier A;
9. any security-sensitive failure is resolved rather than waived silently.
10. the tracked tree and complete reachable Git history pass credential hygiene checks;
11. package metadata and included license notices match the documented licensing scope.

## Release artifacts

Each release should include:

- source archive;
- Python wheel and source distribution when packaging is enabled;
- verification summary;
- catalog coverage report;
- list of promoted, restricted, experimental, and rejected resources;
- known limitations and recheck debts;
- source commit.

## Stability labels

- **experimental:** interface or recommendation policy may change materially;
- **preview:** useful for real projects but still undergoing cross-project evaluation;
- **stable:** backwards-compatibility and migration policy enforced;
- **deprecated:** retained temporarily with a replacement path;
- **removed:** no longer supported.

Version `0.5.0` remains **preview**. It is suitable for supervised assessment and planning, not unsupervised production modification.

## Re-release triggers

Publish a new release when a material security advisory, license change, abandoned upstream project, invalid evidence source, incompatible provider change, or selection regression affects recommendations.

## Prohibited release claims

A release must not claim that Internet-Well guarantees:

- bug-free software;
- legal or regulatory compliance;
- secure configuration in every environment;
- successful product-market fit;
- accurate legal, medical, financial, or employment outcomes;
- autonomous approval of critical systems.
