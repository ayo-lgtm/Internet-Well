# Privacy and Data Handling

Internet-Well is designed for local repository assessment. The CLI does not upload source code, findings, or reports.

## Safe defaults

- Absolute project and home-directory paths are redacted by default.
- Reports are classified `private` by default.
- Reports cannot be written inside the assessed Git repository unless `--allow-in-repo-output` is supplied.
- Potentially sensitive filenames are identified without reading their contents.
- Hosted CodeWiki use requires `--provider-consent`.
- Every report states that it is preliminary and is not a security, legal, privacy, or production approval.

## Private repositories

A private repository can be assessed locally without publishing its code or findings. Keep raw reports outside the repository and outside synchronized public folders. Do not commit assessments, architecture maps, vulnerability findings, customer data, credentials, privileged material, or proprietary decisions to the public Internet-Well repository.

Recommended command:

```bash
internet-well assess /path/to/private-project \
  --classification private \
  --format markdown \
  --output "$HOME/.internet-well/reports/project-assessment.md"
```

## Hosted documentation providers

Before using a hosted provider, review its retention, model-training, subprocessors, access controls, deletion, data residency, and incident terms. Remove secrets, personal data, privileged content, and proprietary material. Then explicitly pass `--provider-consent`.

Open-source or self-hosted documentation systems remain subject to the operator's storage, logging, backup, and access configuration.

## Sharing reports

`--classification shareable` records an explicit intent; it does not guarantee that a report is safe to publish. Review every report for product names, business logic, security findings, architecture details, customer information, legal strategy, and other confidential material before sharing.

## What Internet-Well does not do

Internet-Well does not provide encrypted report storage, access control, automatic legal-privilege protection, guaranteed secret detection, or secure deletion. Users remain responsible for the environment in which the CLI runs and where reports are stored.
