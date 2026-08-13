# Attached Resource Review — August 2026

This review records the resources identified from the supplied screenshots and how Internet-Well should treat them. A screenshot, social-media recommendation, star count, or benchmark graphic is discovery evidence only; it is not a trust or performance determination.

## Newly added resources

### ComposioHQ/awesome-claude-skills

Verified upstream: `https://github.com/ComposioHQ/awesome-claude-skills`.

The repository is an Apache-2.0 curated collection of Claude skills and plugins and advertises a large cross-agent catalog. It is valuable as a discovery source, but the collection links to many independently maintained skills and also contains connected-app workflows capable of real external actions.

Internet-Well therefore treats it as a **curated discovery and selective-adoption source**, not as a blanket trusted bundle. Each selected skill must receive its own provenance, exact-pin, license, script, tool-permission, credential, dependency, network-behavior, and baseline review before adoption. Never install the entire collection merely because it is popular.

### microsoft/playwright-mcp

Verified upstream: `https://github.com/microsoft/playwright-mcp`.

This is Microsoft's Apache-2.0 Playwright MCP browser-automation server. It operates through structured accessibility snapshots and is appropriate when an agent needs persistent browser state, rich introspection, or iterative browser reasoning.

The screenshot's token comparison is **not adopted as a verified benchmark**. Upstream documentation itself notes that coding agents can benefit from CLI + Skills workflows because they can be more context-efficient, while MCP remains useful for persistent state and richer agentic loops.

Selection rule:

- prefer **Agent Browser or Playwright CLI + Skills** when coding-agent context efficiency and concise browser operations are the dominant requirement;
- prefer **Playwright MCP** when persistent browser state, richer structural introspection, exploratory automation, or long-running browser loops justify the additional context cost;
- benchmark the actual target workflow before claiming one option is cheaper or faster.

All browser options remain high-risk integrations: use isolated profiles, hostname allowlists, credential isolation, download controls, logging, and explicit approval for state-changing production actions.

## Resources already governed before this review

The remaining attached resources were already present in Internet-Well's governed catalog or executable integration layer: Anthropic Agent Skills; skills.sh / Vercel Skills CLI; Vercel Agent Browser; Get Shit Done; Taste Skill; Humanizer; Storyscope; React Bits; Anime.js; Shader Gradient; Jitter; Refero; 10x App Builder; and Ponytail.

They are not duplicated merely because they reappeared in screenshots. Existing provenance, license, privacy, accessibility, performance, and permission controls remain controlling.

## Supply-chain rule

Agent skills are executable supply-chain dependencies even when they are mostly Markdown. A skill can instruct an agent to execute commands, access credentials, connect external accounts, modify repositories, browse authenticated sessions, or publish content. Internet-Well therefore requires explicit source identity, exact pins, selective adoption, permission review, controlled testing, and rollback evidence before critical use.
