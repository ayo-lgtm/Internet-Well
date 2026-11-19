# Internet-Well Harvest — every repo resource from the Instagram posts
**Compiled 2026-11-18 · Sources: the reels shared in chat (filed in `~/workspace/knowledge.md`) plus a scan of the curator accounts' other recent videos (@gittrend.io Nov 8–18, @jamesmbuilds Sep–Nov, @pedrohtmallet, @mercythaddeus_)**

**Result: 71 new research candidates appended to the local catalog copy (`catalog/curated-repositories.json`: 77 → 148 entries). Nothing pushed to GitHub — the push is the owner's call, same as FreeHire. All entries are research candidates under the catalog's existing policy, not registry approvals.**

Method note: the videos' on-screen repo names were wrong in roughly a third of the gittrend.io cases checked — every repo below was verified against its actual GitHub page or primary coverage, never cataloged from the video alone.

---

## 1. Added to the catalog (71)

### Agent tooling & coding agents
| Repo | License | What it does |
|---|---|---|
| [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | MIT | AG-UI: open event protocol streaming any agent's tokens, tool calls and state into any frontend; spec frozen at 1.0 (CopilotKit) |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | MIT | Control plane to run and steer Claude Code, Codex, Cursor, OpenCode from desktop, web or phone (~51–61K stars) |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | Apache-2.0 | Annotate an agent's plans/diffs in the browser and send the notes back in one click (~11.7K stars) |
| [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer) | Apache-2.0 | Plugin that cuts coding-agent token costs (authors report 18–31% on SWE-Bench) by learning repo facts and pruning tools (~7.5K stars) |
| [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) | Apache-2.0 | Evaluates AI agent skills/plugins: quality gates, security scanning, live agent runs (~3.4K stars) |
| [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | unknown | Open-source terminal coding agent; runs local models via Ollama |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | MIT | Stacks 34 providers' free tiers behind one local OpenAI-compatible endpoint (50K+ stars; personal projects, per its own README) |
| [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) | MIT | Eleven Claude skills that clean-room clone an app, then fix what real user reviews complain about |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | MIT | 74 Claude skills structuring an individual investor's routine (regime checks, sizing, journaling) |
| [NousResearch/hermes-official-plugins](https://github.com/NousResearch/hermes-official-plugins) | MIT | Every first-party plugin for the Hermes Agent in one repo |
| [gettogo/togo](https://github.com/gettogo/togo) | unknown | iPhone/Watch app to monitor and steer 16 coding agents on your own machines over SSH |
| [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | Apache-2.0 | Stanford local-first personal AI framework — your assistant on your own laptop |
| [agentes-chat/agentes-chat](https://github.com/agentes-chat/agentes-chat) | AGPL-3.0 | Self-hosted Slack where agents sit in channels as teammates with roles and budgets (week-old; installed via curl — review before running) |

### Browser & device agents (flagged: separate profile / spare device only)
| Repo | License | What it does |
|---|---|---|
| [anomalyco/browse](https://github.com/anomalyco/browse) | MIT | MCP server + extension letting agents drive your real browser — your tabs and logins |
| [Player-YN/BrowserKitten](https://github.com/Player-YN/BrowserKitten) | MIT | Agent in a Chrome side panel working on your signed-in session |
| [JosssphZhou/poki](https://github.com/JosssphZhou/poki) | AGPL-3.0 | Agent operates your real iPhone via MCP, no jailbreak (verified only on Chinese-interface iPhones; spare device only) |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | MIT | 87-tool MCP server letting assistants configure and automate Home Assistant |

### Web, SEO & design
| Repo | License | What it does |
|---|---|---|
| [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) | Apache-2.0 | Vendor-stewarded skill pack feeding agents expert guidance on 250 modern web features (15.5K stars) |
| [AgriciDaniel/jev-seo](https://github.com/AgriciDaniel/jev-seo) | MIT | Full SEO audit from one URL — 52 Search Central rules + Jev (TypeSafe) judgments; PDF/Excel/Markdown out, ~1¢/site |
| [meta/astryx](https://github.com/meta/astryx) | MIT | Meta's open design system: 150+ accessible React components themed via CSS variables (~20K stars) |
| [vercel-labs/ui](https://github.com/vercel-labs/ui) | Apache-2.0 | 50+ headless UI behaviors (keyboard, focus, ARIA) that coding agents compose into accessible interfaces |
| [expo/exact](https://github.com/expo/exact) | MIT | Expo's agent-first runtime: write once, run natively on web, macOS, iOS, Android |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | MIT | Agent skill turning a codebase into an interactive architecture map linked to files/lines |
| [shadcn-labs/pdfcn](https://github.com/shadcn-labs/pdfcn) | MIT | Copy-paste PDF components for React via the shadcn registry — directly relevant to shadcn builds |

### Media, content & video pipeline
| Repo | License | What it does |
|---|---|---|
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | GPL-3.0 | Node-based GUI for image/video generation models |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | MIT | 3Blue1Brown-style math/explainer animation library |
| [academa-labs/manimgx](https://github.com/academa-labs/manimgx) | MIT | Manim-compatible API reimplemented on a Rust/GPU core for 3D animation |
| [wassgha/rescript](https://github.com/wassgha/rescript) | PolyForm Noncommercial | Transcript-based editor: delete words, the clip is cut; fully on-device (note: NOT a permissive license) |
| [rushindrasinha/youtube-shorts-pipeline](https://github.com/rushindrasinha/youtube-shorts-pipeline) | MIT | Topic → finished, uploaded YouTube Short for ~$0.11 (project's figure) |
| [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) | Apache-2.0 | Agent skill that reverse-engineers any video shot-by-shot into a remake plan |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | AGPL-3.0 | Voice clone/transcribe/dub (app is AGPL, but bundled voice models are non-commercial — personal use only) |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | unknown | AI workflow turning documents into natively editable PowerPoint decks (~78K stars) |
| [Likely7/Veyra-NRVideo](https://github.com/Likely7/Veyra-NRVideo) | GPL-3.0 | Real-time GPU video/game-stream enhancement (super-resolution, denoising) on Windows |
| [GabrieleLozupone/kokon](https://github.com/GabrieleLozupone/kokon) | AGPL-3.0 | Local prompt-based photo editor — describe the edit, it happens on your machine |
| [FluentRead/FluentRead](https://github.com/FluentRead/FluentRead) | GPL-3.0 | Bilingual reading extension: translations alongside the original page |

### Data, documents & research
| Repo | License | What it does |
|---|---|---|
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | BSD-3-Clause | Scraping framework built for JS-heavy, anti-bot-protected sites (~104K stars) |
| [datalab-to/indra](https://github.com/datalab-to/indra) | Apache-2.0 (code) | CPU-only OCR: PDFs/images → Markdown/JSON in 80+ languages (model weights under modified OpenRAIL-M — restricted) |
| [chenxiachan/textfold](https://github.com/chenxiachan/textfold) | Apache-2.0 | Folds papers/pages/AI replies into five zoomable levels of detail |
| [Zleap-AI/SAG-Wiki](https://github.com/Zleap-AI/SAG-Wiki) | MIT | Tiny local knowledge base indexing your files with no LLM/embedding calls (new installs route to the vendor's key-gated API — noted) |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | MIT | Checks a username across 400+ social networks (OSINT) |
| [anefzaoui/misterdownloadmanager](https://github.com/anefzaoui/misterdownloadmanager) | GPL-3.0 | Clean-room, ad-free download manager in Rust (IDM alternative) |

### Security & reverse engineering (authorized use only)
| Repo | License | What it does |
|---|---|---|
| [usestrix/strix](https://github.com/usestrix/strix) | unknown | Autonomous AI pentesting that proves vulnerabilities with working exploits (~76K stars) |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | MIT | 83 Claude Code skills for bug bounty/red-team built from 681 disclosed reports (scope enforced in code) |
| [qybaihe/bla](https://github.com/qybaihe/bla) | MIT | Defense shield hardening releases against AI reverse engineering (beware near-identical impersonator repos — this is the verified one) |
| [morluto/rea](https://github.com/morluto/rea) | MIT | MCP server letting agents drive Ghidra/IDA to reverse-engineer binaries (star count inflated after a suspicious surge — trust the repo, not the number; malicious lookalikes exist) |
| [reacher-z/Awesome-REA](https://github.com/reacher-z/Awesome-REA) | MIT | Source-reviewed catalog of 1,253 reverse-engineering tools, cases and papers |

### Benchmarks & evaluation
| Repo | License | What it does |
|---|---|---|
| [TIGER-AI-Lab/WebsiteBench](https://github.com/TIGER-AI-Lab/WebsiteBench) | Apache-2.0 | Benchmark: rebuild 70 websites from browsing alone; best model passes 26.2% |

### Platforms & self-hosting
| Repo | License | What it does |
|---|---|---|
| [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | AGPL-3.0 | Postiz: schedule posts on every platform; ships an MCP server (open-source Buffer counterpart) |
| [opf/openproject](https://github.com/opf/openproject) | GPL-3.0 | OpenProject: free self-hosted Asana alternative (~17K stars) |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Sustainable Use (fair-code) | Workflow automation with native AI — note: NOT OSI open source; no hosted resale |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | AGPL-3.0 | Self-hostable remote desktop (TeamViewer alternative) |
| [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | GPL-2.0 | Self-hosted media server (Plex alternative) |
| [immich-app/immich](https://github.com/immich-app/immich) | AGPL-3.0 | Self-hosted photo/video backup, Google Photos-style |
| [Kareadita/Kavita](https://github.com/Kareadita/Kavita) | GPL-3.0 | Self-hosted ebook/comics/manga server |
| [navidrome/navidrome](https://github.com/navidrome/navidrome) | GPL-3.0 | Self-hosted personal music streaming |
| [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole) | EUPL-1.2 | Network-wide ad/tracker blocking via DNS sinkhole |
| [localsend/localsend](https://github.com/localsend/localsend) | Apache-2.0 | Cross-platform AirDrop alternative over local WiFi (use v1.18.2+ — older versions have a critical MITM advisory) |
| [we-promise/sure](https://github.com/we-promise/sure) | AGPL-3.0 | Self-hosted personal finance app (community fork of Maybe Finance) |
| [libracoder/kiri](https://github.com/libracoder/kiri) | Apache-2.0 | Tiny Rust Docker Desktop replacement speaking the Docker Engine API |
| [aws/aws-emulator](https://github.com/aws/aws-emulator) | CC0-1.0 | Official AWS local emulator: test AWS code with no AWS account |
| [RunanywhereAI/trnrt](https://github.com/RunanywhereAI/trnrt) | Apache-2.0 | LLM inference engine for AWS Trainium2 with an OpenAI-compatible API |
| [cactus-compute/cactus](https://github.com/cactus-compute/cactus) | Apache-2.0 | Runs text/speech/vision models on-device in a sub-50MB engine |
| [BenchUp3D/editor](https://github.com/BenchUp3D/editor) | MIT | 3D woodworking/furniture modeling with joinery plans and cut lists |
| [zacharytgray/HyprMac](https://github.com/zacharytgray/HyprMac) | MIT | Hyprland-style tiling window manager for macOS |
| [net-merge/net-merge](https://github.com/net-merge/net-merge) | MIT | Bonds WiFi + mobile hotspot for redundancy/bandwidth |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | Unlicense | Downloads video/audio from YouTube, Instagram, TikTok, X and hundreds more sites |

### Learning resources
| Repo | License | What it does |
|---|---|---|
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | CC0-1.0 | Recreate your favorite technologies from scratch |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | CC-BY-4.0 | System design, taught and interview-prepped |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | CC-BY-4.0 | Free programming books in many languages |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | MIT | Every classic algorithm in Python, for education |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | custom (restrictive) | roadmap.sh interactive developer roadmaps |

## 2. Already in the catalog (not duplicated)
- **browser-use/browser-use** (Mercy's list + a jamesmbuilds video) — already entry in the 77.
- **aquasecurity/trivy** (jamesmbuilds) — already in the 77. Note: Trivy had a March 2026 supply-chain compromise (malicious v0.69.4, force-pushed action tags, CVE-2026-33634) — pin to a commit SHA.
- **strelov1/freehire** — added Oct 23 as #77.
- The FirmOS stack from the @restructureai reel (Kimai, Invoice Ninja, Cal.com, Whisper, Ollama, vLLM, LiteLLM, Qdrant, Keycloak) — several already cataloged (cal.com, litellm, qdrant, ollama, vllm, keycloak); the rest live in the FirmOS scaffold, not the Well.

## 3. Harvested but held out of the catalog (with reasons)
- **Turnitout** (AhmadHassan-BTed/Turnitout-Humanizer) — AI-detector/plagiarism evasion and watermark stripping. Excluded on purpose grounds in October; the exclusion stands.
- **Claude Unlimited** (DevDock-AI/claude-unlimited) — pools subscriptions to rotate around usage limits; likely violates Anthropic/OpenAI terms and risks account bans.
- **Openjutsu** (D3voz/openjutsu) and **Open-Genjutsu** (Anil-matcha/open-genjutsu) — person-swap video tools (deepfake-adjacent; Openjutsu also buries non-commercial InsightFace and AGPL dependencies).
- **GestaltX** (huamidev/GestaltX) — edits a load-bearing iOS system file (boot-break risk), author account reportedly banned, sideload-only.
- **NX2Apple** (LNPANDY/NX2Apple) — requires your own Switch prod.keys and game dumps; legally grey.
- **HermesEnabler** (pookjw/HermesEnabler) — patches MobileGestalt to unlock Hermès watch faces; system-file patching for a cosmetic unlock.
- **vork** (voyager-so/vork) — pitched as open source; actually source-available under a paid "Preview License."
- **BRUTAL** (C# game framework) — the video and other coverage disagree on the owner handle; the Well does not guess URLs. Pending a primary-source check.
- **Capri AI Desktop** and **Infradeck** — medium-confidence identification (several same-named repos / inconsistent owner handle). Pending confirmation.
- **Rerun** (rerun-build/rerun) — the video describes an "AI coworkers" platform; the repo is a data-visualization SDK. Mismatch needs a human look before cataloging.
- **Jumpe** (Pedro's "JUMPE" post) — a commercial Brazilian SaaS discount code, not a repo.
- **Robotar** (avatar generator, Rahul's list) and **Impeccable** (design skill, Rahul's list) and jamesmbuilds' unnamed award-site repo — real tools, but the exact repos could not be confirmed from public material. Not guessed.

## 4. Non-repo resources from the same posts (for the Well's notes, not the catalog)
- **Rahul Singh's how-to set** (all 50 videos filed): the SEO-fix prompt for Claude Code; the DESIGN.md + design-skill + Chrome DevTools MCP method for fixing generic-looking sites; the 20-point App Review rejection checklist; the 3 security mistakes (keys in the app, no DB rules, no rate limits); the pre-launch legal checklist; domain-setup rules (app subdomain, separate email subdomains, sitemap + Search Console); the four pre-code documents (PRD, design doc, TRD, implementation plan).
- **Chrome DevTools MCP** (Google) — named in Rahul's design-fix video; lets an agent see the real rendered site.
- **x402 protocol** (@nathanrbentley) — real agent-payments rail (Coinbase/Linux Foundation), not a repo and not a revenue feature today; median seller lifetime revenue $3.96.
- **Tranchi.ai** (@maxclosesdeals) — commercial probate-wholesaling platform; the standing note stands: do not buy until the free Dallas County route is proven.
- **OpenClaw** (formerly ClawdBot; @mercythaddeus_ Jan post) — MIT personal-assistant agent, now foundation-run; flagged in coverage for a large advisory history — worth its own look before any trial.
- **@mercythaddeus_'s website-list posts** (Feb–Mar: "websites that feel illegal," "rare finds") — websites, not repos; available to harvest the same way if wanted.

## 5. Coverage
- Every reel shared in chat: filed and mined (knowledge.md Parts 1–2).
- @gittrend.io: all 50 recent posts scanned; 46 repo videos identified (Nov 8–18 window fully covered).
- @jamesmbuilds: 14 repo posts watched (Sep 13–Nov 13); 23 repos identified across them.
- @pedrohtmallet: caption-linked repos (3) + 2 keyword-gated posts watched.
- @mercythaddeus_: repo content is the Oct 31 list (already filed); the rest of her feed is prompt packs, not repos.
- @rahulsingghh_: all 50 videos were already covered in knowledge.md Part 1.
