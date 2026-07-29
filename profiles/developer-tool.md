# Developer Tool Product Profile

## Applies to

CLIs, SDKs, APIs, code generators, scanners, CI tools, libraries, IDE extensions, and infrastructure used by developers.

## Required capabilities

Stable interfaces, versioning, reproducible installation, secure defaults, dependency integrity, documentation, examples, telemetry transparency, error handling, sandboxing where code executes, compatibility testing, and migration guidance.

## Risk model

Primary risks are supply-chain compromise, destructive defaults, credential exposure, generated insecure code, version drift, hidden telemetry, platform incompatibility, and automation that changes repositories without review.

## Completion evidence

Installation and uninstall are reproducible; public interfaces are tested; generated changes are reviewable; credentials remain isolated; failure modes are actionable; versions and migrations are documented; and representative integrations pass.

## Human review

Security-sensitive scanners, code execution, package publishing, credential access, production infrastructure, and destructive automation require competent review and explicit authorization.
