# Workflow: Launch Checklist (web product)

Pre-launch gate assembled entirely from validated registry entries. Each
item cites its record; "verify" means produce the artifact, not tick the
box. Mobile launches: add fastlane + MASVS
([records](../registry/launch-maintenance/fastlane.md),
[MASVS](../registry/security/owasp-masvs.md)).

## Security
- [ ] ASVS Level 1 self-assessment done; deviations listed
      ([ASVS](../registry/security/owasp-asvs.md))
- [ ] Secrets scan clean over full git history
      ([Gitleaks](../registry/security/gitleaks.md)); pre-commit hook on
      ([pre-commit](../registry/engineering/pre-commit.md))
- [ ] Dependency/container scan at pinned versions; SBOM stored with the
      release ([Trivy](../registry/security/trivy.md),
      [Syft](../registry/security/syft.md))
- [ ] SAST in CI ([Semgrep CE](../registry/security/semgrep.md) — local
      rules, `--metrics=off`)
- [ ] DAST baseline scan of staging, alerts triaged
      ([ZAP](../registry/security/zaproxy.md))
- [ ] Threat model exists and matches shipped architecture
      ([Threat Dragon](../registry/security/owasp-threat-dragon.md),
      [C4 diagrams](../registry/product/c4-model.md))

## Quality & accessibility
- [ ] E2E tests green for the critical journeys
      ([Playwright](../registry/engineering/playwright.md))
- [ ] Lighthouse ≥90 on perf/SEO/a11y for key pages, cited audits fixed
      ([Lighthouse](../registry/marketing/lighthouse.md))
- [ ] axe scan zero violations + one manual keyboard/screen-reader pass
      ([axe-core](../registry/design/axe-core.md)) — no public WCAG
      claims from automated results alone

## Operations
- [ ] Backups running AND a restore drill completed
      ([restic](../registry/operations/restic.md))
- [ ] Metrics + alerting live ([Prometheus](../registry/operations/prometheus.md));
      status page up ([Uptime Kuma](../registry/operations/uptime-kuma.md))
- [ ] Incident bootstrap done ([workflow](incident-response-bootstrap.md))
- [ ] Migrations are versioned, rollback tested
      ([dbmate](../registry/launch-maintenance/dbmate.md))
- [ ] Dependency-update automation on
      ([Renovate](../registry/launch-maintenance/renovate.md))

## Email & marketing
- [ ] SPF/DKIM/DMARC valid on sending domains
      ([checkdmarc](../registry/marketing/checkdmarc.md)); DMARC reports
      flowing ([parsedmarc](../registry/marketing/parsedmarc.md))
- [ ] Analytics live, privacy policy discloses it
      ([Plausible CE](../registry/marketing/plausible-ce.md) or
      [Umami](../registry/marketing/umami.md))

## Legal (counsel required — not optional)
- [ ] Terms/CSA + DPA reviewed by a licensed attorney
      ([Common Paper](../registry/legal-compliance/common-paper-csa.md))
- [ ] License obligations of every shipped dependency satisfied
      ([ScanCode](../registry/legal-compliance/scancode-toolkit.md),
      [matrix](../licenses/obligations-matrix.md))
- [ ] If AI features ship: risk register per NIST AI RMF GenAI profile,
      LLM Top 10 review
      ([RMF](../registry/legal-compliance/nist-ai-rmf.md),
      [LLM Top 10](../registry/engineering/owasp-llm-top10.md))

This checklist reduces mistakes and surfaces risk; it does not guarantee
a bug-free launch, legal compliance, or product-market fit.
