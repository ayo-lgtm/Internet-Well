---
name: Omarchy Meeting Recorder
category: operations
subcategory: local-meeting-transcription
status: experimental
tier: C
human_reviewed: false
type: tool
canonical_repo: https://github.com/jankeesvw/omarchy-meeting-recorder
website: https://github.com/jankeesvw/omarchy-meeting-recorder
pinned_version: 5d098eb39de870f9d56933566bcde589c33b6d74 (2026-10-14)
license: MIT
score: 58
confidence: medium
tested: false
last_verified: 2026-10-23
---

# Omarchy Meeting Recorder

## What it does
Records microphone and computer audio as separate tracks, imports existing recordings, and produces editable transcripts, speaker labels, playback and optional chapters. Local transcription and diarization are maintainer claims, not independently measured privacy or accuracy guarantees [M].

## When to use
Evaluate local meeting capture and transcription on Omarchy Linux / Hyprland; study a Rust, GTK 4 and libadwaita implementation of dual-track recording and transcript playback [M]. Selected because it addresses local meeting capture; the existing startup-distribution source addresses a different capability and is not an alternative [I].

## When not to use
- Not a verified Windows, macOS, iOS, browser or server deployment [U].
- Not yet approved for confidential, privileged or regulated meetings: runtime network behavior, storage protections and dependency security have not been tested [U].
- Do not assume optional AI chapters remain local. The README says transcript text goes to the configured agent service [V].
- Do not enable unreviewed Actions or automatic publication. Configured commands can run automatically after transcription [V].

## Evidence
- [Canonical repository](https://github.com/jankeesvw/omarchy-meeting-recorder) is public and not archived at inspection [V].
- [Inspected commit](https://github.com/jankeesvw/omarchy-meeting-recorder/commit/5d098eb39de870f9d56933566bcde589c33b6d74) is dated 2026-10-14 [V].
- [License file](https://github.com/jankeesvw/omarchy-meeting-recorder/blob/5d098eb39de870f9d56933566bcde589c33b6d74/LICENSE) grants MIT permissions with copyright and permission-notice preservation [V].
- [README](https://github.com/jankeesvw/omarchy-meeting-recorder/blob/5d098eb39de870f9d56933566bcde589c33b6d74/README.md) describes PipeWire/libpulse capture, ffmpeg, whisper-rs/whisper.cpp, GTK 4, libadwaita 1.6+, optional Vulkan acceleration and model downloads [V]. Their end-to-end behavior has not been tested [U].
- [Agent runner](https://github.com/jankeesvw/omarchy-meeting-recorder/blob/5d098eb39de870f9d56933566bcde589c33b6d74/src/agent.rs) contains per-agent tool-disabling configuration and explicitly treats transcripts as untrusted [V]. Effective isolation across installed agent versions remains untested [U].
- [Actions documentation](https://github.com/jankeesvw/omarchy-meeting-recorder/blob/5d098eb39de870f9d56933566bcde589c33b6d74/docs/actions.md) describes shell commands, automatic actions and an example that publishes a transcript to an unlisted GitHub gist [V]. Unlisted publication is not confidential access control [I].
- Repository tree includes benchmark and release workflows [V]; workflow success, benchmark results and release provenance were not verified [U].

## Validation results
Metadata, immutable commit, MIT license, README, agent runner and Actions documentation inspected on 2026-10-23. No installation, recording, transcription, packet capture, dependency scan or upstream test execution performed. Latest stable release, release cadence, maintainer concentration, institutional backing, CVEs, unresolved security issues, signed artifacts, SBOM and full installation reproducibility remain unknown [U]. No production-readiness claim is made.

## Security findings
Treat transcript text, imported media and generated chapters as untrusted data. Review media-decoding dependencies and agent isolation before use. Actions execute user-configured shell commands and can disclose or modify meeting data [V/M]. Leave Actions unconfigured during baseline evaluation. Verify network egress and agent configuration rather than relying on the headline privacy claim. This record is not a security audit.

## Legal/licensing findings
Application source is MIT [V]; commercial use, modification and redistribution are permitted subject to its notice requirements. Dependencies and downloaded models retain separate licenses. README identifies an OpenMDW-licensed NVIDIA diarization model; those model terms and the full dependency license inventory have not been independently reviewed [M/U]. Recording authorization, organizational policy and retention requirements must be assessed for the intended setting; catalog inclusion authorizes no recording.

## Installation
No software is installed by this addition. Inspect packaging and build scripts at the exact pin before any authorized isolated build. Do not run the upstream curl-to-shell installer merely because this record exists. README describes a roughly 1.6 GB default transcription-model download and a roughly 120 MB diarization model [M]. Confirm download identities, integrity, disk capacity and hardware compatibility. Optional agent services may have separate charges and data-processing terms [I].

## Agent integration
Registry candidate only; no executable adapter, default bundle or automatic installation is added. For an adoption plan:
1. Confirm Omarchy/Hyprland, audio routing, data classification and recording authorization.
2. Pin source and model revisions; review dependencies and installers.
3. Use synthetic audio with known speakers, overlapping speech and silence.
4. Verify capture, pause/resume, imports, recovery, speaker accuracy and CPU/GPU resource use.
5. Establish a baseline without an agent or Actions; measure network traffic after approved model downloads.
6. Review and separately authorize any chapter provider or export destination before enabling it.
7. Recheck upstream changes before changing this pin; remove this record and regenerate the index to roll back catalog inclusion.

## Required human review
Review intended recording use, storage/retention, model and dependency terms, agent-provider data handling and every configured Action before adoption. Keep tier C until execution evidence and review justify reconsideration.

## Score notes
Provisional evidence score: functional quality 12/20; security posture 8/20; maintenance health 8/15; documentation/usability 8/10; license suitability 8/10; reproducibility/testing 4/10; professional provenance 6/10; integration readiness 4/5 = 58/100. Deductions reflect untested runtime behavior, incomplete dependency/model review and narrow platform compatibility; not a measured product-quality rating.
