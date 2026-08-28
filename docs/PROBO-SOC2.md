# Probo + Internet-Well: SOC 2 Readiness and Auditor Handoff

Internet-Well integrates [Probo](https://github.com/getprobo/probo) as a governed GRC/readiness engine pinned to commit `bdb350aa88e60f3664caab6f41a665edd7729298` (MIT license).

This integration is designed to reduce the cost of SOC 2 readiness by using open-source tooling for control management, policies, risks, vendors, access reviews, and evidence organization, then handing a complete package to an independent CPA firm for the examination and report.

## What this integration does

- routes SOC 2 readiness goals to Probo through the Agent Brain;
- creates a Type I readiness plan, defaulting to the Security Trust Services Criteria unless the user selects additional criteria;
- defines an evidence contract with source provenance, timestamps, owners, reviewers, and exceptions;
- prepares an auditor-handoff checklist and evidence package;
- requires written confirmation that the auditor accepts customer-managed Probo evidence and does not require a separate commercial GRC subscription;
- keeps the final examination and report issuance with an independent licensed CPA firm.

## What it does not do

Internet-Well and Probo do **not** grant SOC 2, issue a SOC 2 report, provide CPA attestation, or make a company compliant merely because automated checks pass. A qualified independent CPA firm remains the attestation authority.

## CLI

```bash
internet-well-compliance show
internet-well-compliance soc2-readiness
internet-well-compliance soc2-readiness --criteria security --criteria availability
internet-well-compliance evidence-template
internet-well-compliance auditor-handoff --company "Example Co"
```

The commands are local planning/evidence-contract operations. They do not connect to Probo, upload evidence, contact an auditor, use credentials, or submit an audit request.

## Low-cost Type I path

For a small SaaS company, the lowest-complexity starting scope is commonly a Type I examination with the Security Trust Services Criteria only, provided that customer or contractual requirements do not require Availability, Confidentiality, Processing Integrity, or Privacy. Scope must be approved by management and agreed with the auditor.

The intended workflow is:

1. Define the system boundary and selected Trust Services Criteria.
2. Map and assign controls in Probo.
3. Approve policies and document control owners.
4. Collect source evidence without copying secrets or unnecessary personal data.
5. Complete risk, vendor, access, change-management, monitoring, and incident-response evidence.
6. Review exceptions and remediation with human owners.
7. Generate the auditor handoff package.
8. Obtain written auditor confirmation of evidence format, scope, fee, timeline, and report issuance.
9. Transfer evidence using the auditor-approved secure channel.
10. The independent CPA performs the examination and issues the report.

## Auditor selection gate

Before engagement, verify at minimum:

- the firm is a licensed CPA firm qualified to perform SOC engagements;
- its relevant AICPA peer-review status;
- it accepts evidence from a customer-managed/self-hosted GRC system such as Probo;
- it does not force purchase of a second commercial GRC platform;
- the audit fee and any add-on fees are documented;
- the final SOC 2 report is included in the engagement;
- evidence-transfer format and security are agreed;
- scope, system boundaries, and examination date are agreed.

Internet-Well should treat auditor pricing as time-sensitive market information. Do not hard-code a particular CPA firm as the permanent cheapest option.

## Evidence handling

Audit evidence is confidential. Do not commit evidence exports, credentials, private keys, production secrets, customer data, privileged material, or personal data to Internet-Well. Use the evidence template as a schema/contract and store actual audit evidence in an access-controlled system approved for the engagement.

## Upstream governance

Internet-Well never silently updates the Probo pin. Upgrades require review of license changes, security advisories, breaking changes, data-model/export changes, compatibility, and rollback.
