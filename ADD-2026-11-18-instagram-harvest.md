# Catalog addition — 2026-11-18 (Instagram harvest)

**Change:** 71 candidate entries appended to `catalog/curated-repositories.json` (77 → 148 entries). Nothing else modified. Per the catalog lifecycle, these are **research candidates, not registry approvals** — admission still requires the METHODOLOGY.md pipeline (pinning, license/security review, sandboxed evaluation, human review). **Nothing pushed to GitHub; the push is the owner's call.**

**Source of the leads:** the owner's order (2026-11-18) to harvest every GitHub-repo / how-to / better-website resource from the Instagram posts he has sent, including the curator accounts' other videos. Full evidence report: `~/workspace/internet_well/harvest/HARVEST-REPORT.md` (per-repo one-liners, sources, catches). Raw scan data: `harvest/batchA.json`, `batchB.json`, `batchC.json`, `posts_*.json` in the same folder.

**Method:** every repo verified against its GitHub page or primary coverage before entry — the videos' on-screen repo names were wrong in ~7 of 20 cases in the Nov 14–18 gittrend.io batch alone (e.g. Plannotator is backnotprop/plannotator, Kiri is libracoder/kiri, Astryx is meta/astryx). The registry does not catalog from the video alone.

**License flags recorded in the entries themselves:**
- VoiceStudio — app AGPL-3.0, bundled voice models non-commercial (personal use only).
- Rescript — PolyForm Noncommercial (not permissive, despite the reel's "free and open-source" framing).
- n8n — Sustainable Use License (fair-code; no hosted resale).
- Indra OCR — code Apache-2.0; model weights under modified OpenRAIL-M (no competitive use, <$20M orgs).
- Developer Roadmaps — custom restrictive license.
- Unknown licenses (confirm at admission): PPT Master, OpenClaude, Strix, Togo.

**Risk tags applied:** high-autonomy for browser/device/team agents (Browse, Browser Kitten, Poki, agentes.chat, T3 Code, OpenJarvis); high-security-legal for offensive-security tooling (Strix, Claude-BugHunter — authorized targets only); medium-data for scrapers/OSINT/finance (Scrapling, Sherlock, Sure, VoiceStudio).

**Harvested but deliberately NOT added** (full reasoning in the report §3): Turnitout (detector evasion — October exclusion stands), Claude Unlimited (subscription-pooling around usage limits), Openjutsu + Open-Genjutsu (person-swap), GestaltX (iOS system-file mod), NX2Apple (prod.keys), HermesEnabler (system-file patch), vork (not open source), BRUTAL / Capri AI Desktop / Infradeck / Rerun (identification or description mismatch — pending a primary-source check, never guessed), Jumpe (commercial SaaS, not a repo), Robotar / Impeccable / one unnamed design repo (repos unconfirmed from public material).

**Already in the catalog, not duplicated:** browser-use/browser-use, aquasecurity/trivy (with a new note: Trivy's March 2026 supply-chain compromise, CVE-2026-33634 — pin to a commit SHA), strelov1/freehire.
