# Apple Design Skills integration

Internet-Well integrates the verified public repository `s1gmamale1/apple-design-skills` as a governed community design-skill family.

Verified source commit used for the initial integration:

`8a3fbea8b561405e5719d682ebd1d14c952aecd7`

Upstream license: MIT.

## Why it exists

The family adds Apple-oriented interaction and design reasoning for Claude Code, Codex, and other agents. It covers HIG-informed design foundations, materials, motion, web interaction, platform surfaces, media delivery, accessibility, and brand tactics.

It is complementary to Taste Skill. Taste provides broad product-design judgment; Apple Design Skills provide a narrower Apple/HIG-inspired design and interaction lens.

## Authority hierarchy

This is a community skill family, not Apple documentation and not an Apple endorsement. When guidance conflicts, use this order:

1. Current official Apple Human Interface Guidelines and platform documentation.
2. Product-specific accessibility, legal, security, privacy, and brand requirements.
3. Internet-Well governance and evidence rules.
4. Community skill guidance from this repository.

## Safe execution

Internet-Well never runs the upstream `install.sh` or `install.ps1` automatically.

Inspect and plan:

```bash
internet-well-apple-design show
internet-well-apple-design list-skills
internet-well-apple-design plan
```

Pin and clone the verified source after review:

```bash
internet-well-apple-design install \
  --ref 8a3fbea8b561405e5719d682ebd1d14c952aecd7 \
  --approve
```

After separately reviewing a particular `SKILL.md` and its references, adopt only that skill:

```bash
internet-well-apple-design adopt apple-design-motion \
  --target codex \
  --approve
```

Existing skills are never overwritten silently.

## Skill family

- `apple-design`
- `apple-design-foundations`
- `apple-design-materials`
- `apple-design-motion`
- `apple-design-web`
- `apple-design-interaction`
- `apple-design-os`
- `apple-design-backend`
- `apple-design-tactics`

## Mandatory quality gates

Any output influenced by the skill family must still be checked for keyboard accessibility, screen-reader semantics, reduced motion, contrast, legibility, responsive behavior, low-end-device performance, GPU and battery cost, native platform behavior, and brand distinctiveness.

Do not copy Apple trademarks, product imagery, videos, trade dress, or distinctive protected expression. The upstream repository itself states that it intentionally excludes Apple's copyrighted reference media.
