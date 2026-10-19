# Startup Distribution + Agentic Video Integration

Internet-Well now treats **launch distribution** and **video production** as separate governed capabilities that can be composed into one launch workflow.

## Sources

### Places To Post Your Startup
- Canonical repository: `mmccaff/PlacesToPostYourStartup`
- Pin: `1941a95f344d90ea5ffe2e0b4c25ffa92dfd3d73`
- License: CC0-1.0
- Internet-Well role: candidate discovery for launch and distribution channels.

The directory is not treated as a live truth source. Every destination must be revalidated before selection or use.

### OpenMontage
- Canonical repository: `calesthio/OpenMontage`
- Pin: `08e2151fa02de28a5d6a312b3d575692bf147ad7`
- Website: `https://openmontage.video`
- License: AGPL-3.0-only
- Internet-Well role: pinned external agentic-video production system and architecture reference.

Internet-Well does not vendor OpenMontage. The AGPL boundary is preserved by using an external pinned checkout only after approval.

## Combined launch path

```text
Product / feature ready for launch
        ↓
Audience + objective definition
        ↓
Launch Distribution Planner
        ↓
Verified channel shortlist
        ↓
Asset requirements by channel
        ↓
Governed Video Production (when video is justified)
        ↓
Rights + budget + provider approval
        ↓
Render + post-render verification
        ↓
Human approval
        ↓
Channel-specific external submission
        ↓
Measure qualified traffic, activation, conversion, retention, feedback
```

The two capabilities may be used independently. A product does not need video merely because a launch destination supports it.

## CLI

Inspect all governed integrations:

```bash
internet-well-integrations list
internet-well-integrations show places-to-post-your-startup
internet-well-integrations show openmontage
```

Generate non-executing plans:

```bash
internet-well-integrations plan places-to-post-your-startup \
  --ref 1941a95f344d90ea5ffe2e0b4c25ffa92dfd3d73

internet-well-integrations plan openmontage \
  --ref 08e2151fa02de28a5d6a312b3d575692bf147ad7
```

Any checkout still requires `--approve`. Posting, publishing, spending, account creation, and provider credential use are separate state-changing actions and are not authorized by installing a source integration.

## Agent Brain routing

Use these capability terms:
- `startup-launch-distribution`
- `launch-channel-discovery`
- `community-launch`
- `agentic-video-production`
- `video-production-pipeline`
- `launch-video`

The composed `product-launch-campaign` bundle joins channel discovery with optional video production while preserving separate approval points for media creation and external distribution.
