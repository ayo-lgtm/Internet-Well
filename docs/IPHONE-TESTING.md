# iPhone testing adoption guide

## Resource choice

| Candidate | Role | Selection |
|---|---|---|
| [Callstack agent-device](../registry/engineering/agent-device.md) | CLI/MCP/API device inspection, interaction, replay and evidence | First evaluation candidate for iOS; requires target-specific setup |
| [Mobile Next mobile-mcp](../registry/engineering/mobile-mcp.md) | MCP device automation and optional cloud fleet | Alternative when its client/cloud workflow fits; disable documented telemetry and verify egress |
| [Google ARTEMIS](../registry/engineering/artemis.md) | Android agent QA | Retain for Android; mainline iOS remains unverified in the existing record |
| Playwright | Deterministic web regression | Complement device execution; mobile viewport/WebKit on Linux is not a physical iPhone |

Selection is provisional, based on inspected documentation; neither iOS tool has been execution-tested by Internet-Well. Cataloging does not install, connect or authorize a provider.

## Before execution

1. Confirm target URL or app build, data classification, allowed actions and observable acceptance criteria.
2. Use an isolated simulator or dedicated device. Identify the device explicitly. Local iOS needs a suitable Mac/Xcode host; physical devices require trusted pairing, Developer Mode and signing as specified by the selected tool. A remote/cloud device requires separately configured access and terms.
3. Inspect pinned install/build scripts and dependencies; choose an immutable reviewed install version. Do not globally install latest by default.
4. Run documented diagnostics before starting the agent. Verify tool/device versions and a working stop path.
5. Use synthetic cases and test-only credentials. Never publish session artifacts, tokens, client documents or personally identifying data into this public repository.
6. For mobile-mcp set MOBILEMCP_DISABLE_TELEMETRY=1 and verify egress. For agent-device set AGENT_DEVICE_NO_UPDATE_NOTIFIER=1 when npm update checks are unwanted. Neither setting governs the connected model provider.
7. Establish finite step/time/cost bounds and keep device-mutating operations sequential.

## Acceptance matrix

| Journey | Observable evidence |
|---|---|
| Load in mobile Safari | Correct URL, usable viewport, no blocked navigation; screenshot and visible UI |
| Sign in and return | Authentication succeeds and the original intake/draft returns; never record real credentials |
| Guided intake | User can describe facts without knowing the legal outcome; answers persist across navigation/reload |
| Evidence upload | Synthetic file is accepted, displayed and retrievable with appropriate access controls |
| Review and export | Facts, timeline and packet match the supplied synthetic facts; no invented evidence |
| Voice input | Permission handling and actual speech-to-text verified on physical hardware |
| Spoken playback | Actual audible output, stop/cancel and interruption behavior verified on hardware |
| Accessibility | VoiceOver focus, labels, order and error announcements verified with VoiceOver; UI-tree inspection is supplementary |
| Failure recovery | Offline/expired-session/retry behavior preserves data appropriately and never reports false completion |

Use a plainly marked synthetic scenario: a fictional tenant paid a fictional deposit and seeks help organizing a return-of-deposit dispute. This is test data, not a legal conclusion. Do not contact a lawyer, submit a claim or send a packet externally during QA.

## Evidence and verdict

Capture the exact product version/URL, tool pin, OS/device, executed steps, expected/actual outcomes and sanitized artifacts. Report each criterion as pass, fail, partial or blocked. Separate browser emulation, simulator and physical-device results. Do not convert a documented capability into a runtime pass.

## Stop and rollback

Stop on unexpected production data, unapproved provider egress, account changes, uncontrolled loops or loss of device ownership. Close the session, release reserved devices and revoke temporary test access. Remove helpers/configuration only using a reviewed target-specific procedure; deleting the registry entry does not uninstall software.
