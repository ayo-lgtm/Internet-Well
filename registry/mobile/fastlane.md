---
name: fastlane
category: mobile-engineering
subcategory: release-automation
status: approved
type: tool
canonical_repo: https://github.com/fastlane/fastlane
website: https://fastlane.tools
pinned_version: 2.237.0 (2026-07-05)
license: MIT
score: 82
confidence: medium
tested: false
last_verified: 2026-07-23
---

# fastlane — iOS/Android build and release automation

## What it does
Automates the painful parts of app-store shipping: code signing (match),
building (gym), screenshots (snapshot), TestFlight/App Store upload
(pilot/deliver), and Play Store upload (supply). The de facto open
toolchain for mobile release automation.

## When to use
- Any founder shipping iOS/Android: scripted, repeatable store releases
  instead of Xcode/Console clicking; CI-driven beta and release lanes
- App Store/Play launch prep: metadata, screenshots, and store listings
  as code in your repo

## When not to use
- Web-only products; Expo-managed React Native apps where EAS covers the
  same ground (evaluate against your stack)
- It cannot bypass store review or store policies — launch timing is
  still Apple/Google's `[I]`

## Evidence
- License MIT `[V]` — repository (2026-07-23)
- Latest 2.237.0, 2026-07-05; 567 releases, 16,800+ commits, active `[V]`
- Governance: community core team (Tumbleson, Wallner, Holtz, et al.)
  after Google stepped back from stewardship `[C]` — repo maintainers list
- Massive mobile-industry adoption `[C]` — context

## Validation results
- Not execution-tested: RubyGems was unreachable from the research
  environment, and meaningful testing requires Apple/Google developer
  accounts and signing assets, which the isolated environment
  intentionally lacks. Metadata validated from repo + release history.

## Security findings
- Handles your signing keys and store API credentials — scope App Store
  Connect/Play API keys minimally; `match` stores certs in an encrypted
  repo you control `[M]` — docs
- No unresolved material advisories located this pass; Scorecard `[U]`

## Legal / licensing findings
- MIT — commercial use permitted. Store interactions are governed by
  Apple/Google developer agreements, not by fastlane's license.

## Installation
`gem install fastlane -v 2.237.0` (or Bundler Gemfile pin; Ruby ≥2.6).

## Agent integration
Lanes are Ruby scripts agents can draft; **actual store submissions and
signing-asset changes must be human-triggered**.

## Required human review
Every store submission; credential/key management; release notes.

## Score notes
Functional 19/20 · Security 15/20 (credential surface) · Maintenance
13/15 · Docs 9/10 · License 10/10 · Reproducibility 6/10 (untested here) ·
Provenance 7/10 · Integration 3/5 → **82**
