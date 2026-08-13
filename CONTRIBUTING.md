# Contributing to Internet-Well

Thanks for contributing. Internet-Well is an evidence-backed Founder OS, so contributions should improve verifiability, safety, portability, or usefulness rather than simply increase the number of tools in the catalog.

## Before opening a pull request

1. Read `AGENTS.md` and follow its authority boundaries.
2. Keep private repositories, customer data, credentials, personal data, privileged material, and unpublished product findings out of this public repository.
3. Use synthetic fixtures and public examples for tests and documentation.
4. Do not add a dependency or skill only because it is popular. Record source identity, license, maintenance status, permissions, privacy implications, compatibility, and limitations.
5. Pin third-party code or executable skills to an exact release or commit where the integration model requires it.
6. Keep changes small and reversible.

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip build
python3 -m pip install -e .
python3 -m py_compile internet_well.py automation/*.py
```

Run the repository verification scripts and relevant integration tests before submitting a PR.

## Pull requests

A useful PR should include:

- the problem or capability gap;
- the selected approach and rejected alternatives when material;
- security, privacy, license, and compatibility considerations;
- tests or verification evidence;
- rollback or removal notes for executable integrations;
- any remaining human-review requirement.

Do not include private assessment reports in a PR. Generated reports should remain outside the repository unless they are explicitly synthetic public fixtures.

## Security reports

Do not report vulnerabilities or credentials in public issues. Follow `SECURITY.md` and use GitHub private vulnerability reporting.

## Licensing

By contributing, you agree that your contribution may be distributed under the repository's declared license. Upstream materials retain their original licenses and must not be copied into Internet-Well unless redistribution is permitted and attribution requirements are satisfied.
