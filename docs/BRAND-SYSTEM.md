# Brand and Design-System Contract

Use this contract when a founder or agent asks for a brand identity, logo,
app icon, visual refresh, or reusable design system. A completed design must
produce traceable decisions and usable assets; a mood board, a single logo,
or a palette alone is not a complete brand system.

The companion starter files live in [`templates/brand-system/`](../templates/brand-system/).
They are deliberately neutral. Replace every placeholder through a product-
specific design process and retain the source files, licenses, approvals, and
test evidence.

## Brand foundation

Record before drawing:

- product name, category, audience, jurisdictions, and primary use cases;
- positioning, promise, proof points, personality, and prohibited claims;
- three to five visual principles tied to product behavior;
- primary and secondary brand style, using
  [`design-style-catalog.md`](design-style-catalog.md) as vocabulary;
- reference products and an explicit no-copy list;
- accessibility, localization, device, print, dark-mode, and motion needs;
- trademark-search status and the human approver.

An agent may propose directions and generate drafts. A qualified human must
approve distinctiveness, cultural fit, material claims, and legal clearance.

## Logo and mark system

The minimum logo family is:

- primary lockup, horizontal lockup, wordmark, and standalone mark;
- full-color, one-color, reversed, light-background, and dark-background
  variants;
- vector masters in SVG plus approved raster exports;
- documented clear space, minimum size, background rules, and prohibited
  transformations;
- a source-of-truth asset manifest with file hashes at release.

Do not treat a stock interface icon, emoji, generated glyph, or another
organization's trade dress as a brand mark. Optimize production SVGs with a
pinned tool such as SVGO, but review the rendered result: optimization does
not establish originality, accessibility, or trademark availability.

## App icons and favicons

Every web/PWA handoff must include, as applicable:

| Asset | Minimum output | Constraint |
|---|---:|---|
| SVG favicon | scalable | simple silhouette; no external fonts or scripts |
| Browser favicon | 16×16 and 32×32 | inspect at native size |
| Apple touch icon | 180×180 PNG | opaque background; no assumed platform mask |
| PWA icon | 192×192 PNG | referenced from the manifest |
| PWA icon | 512×512 PNG | referenced from the manifest |
| Maskable PWA icon | 512×512 PNG | critical artwork inside the safe zone |
| Social card | 1200×630 | readable crop and meaningful alt text where surfaced |

Raster dimensions and file existence are necessary but insufficient. Review
edge clarity, padding, contrast, transparency, manifest paths, MIME types,
cache behavior, light/dark browser surfaces, install UI, and real-device
rendering. A tiny generic placeholder must fail the asset gate even if its
filename and dimensions are technically correct.

## Color system

Separate source palette values from semantic roles. At minimum define:

- canvas, surface, elevated surface, border, focus, and overlay;
- primary, secondary, accent, link, visited-link, and selection;
- text primary, secondary, muted, inverse, and disabled;
- success, information, warning, danger, and their foreground/surface roles;
- light, dark, high-contrast, and forced-colors behavior where applicable.

Measure WCAG 2.2 contrast for text and meaningful non-text boundaries, then
test high-contrast/forced-colors modes and actual component states. Never use
color alone to communicate status. Color.js can calculate and convert color;
axe-core can detect some rendered failures. Neither substitutes for manual
accessibility review.

## Typography system

Specify font families, sources, licenses, fallbacks, supported scripts, and
roles for display, heading, body, UI, code, and data. Define a responsive type
scale, weight, line height, letter spacing, paragraph width, and text-spacing
resilience. Keep body and interface copy as real text.

For web delivery, prefer licensed WOFF2 files, necessary subsets and weights,
local fallbacks, and measured loading behavior. Fontsource packages simplify
self-hosting but do not replace review of each font's own license, glyph
coverage, attribution requirements, or trademark terms.

## Interface iconography

Choose one coherent interface-icon family and document its grid, stroke,
size, optical alignment, filled/outline policy, and state behavior. Lucide is
an interface library, not a source of brand logos.

- Decorative icons are hidden from assistive technology.
- Informative icons have an accessible name or adjacent text.
- Icon-only controls require a programmatic label and visible focus state.
- Destructive, legal, financial, health, and safety actions must not rely on
  an unfamiliar symbol without text.
- Do not mix unrelated icon families merely to fill gaps.

## Design tokens

Store platform-neutral source tokens in the stable DTCG format, using
primitive values plus semantic aliases. Cover color, typography, spacing,
size, radius, border, shadow, opacity, motion, and z-index as applicable.
Components consume semantic or component tokens rather than raw palette
values.

Use immutable reviewable inputs and generate platform outputs. Style
Dictionary may transform tokens for CSS, JavaScript, Android, or iOS, but its
documentation currently identifies incomplete support for parts of DTCG
2025.10. Pin versions and add snapshot/fixture tests for every generated
platform.

## Component documentation

Document reusable components with:

- purpose, anatomy, variants, sizes, states, and content rules;
- keyboard behavior, focus order, names/roles/values, and error handling;
- responsive, empty, loading, offline, success, error, and permission states;
- localization, long-text, zoom, reduced-motion, and dark-mode examples;
- token dependencies, deprecations, migration notes, and owners;
- interaction, accessibility, and visual-regression evidence.

Storybook is a suitable workshop and documentation surface for supported web
frameworks. A published Storybook is not proof that the product implements
the same components or passes runtime accessibility tests.

## Acceptance gates

A brand/design-system handoff passes only when:

1. the brand brief and no-copy constraints are approved;
2. trademark/domain screening and asset-license review are recorded;
3. logo, icon, color, typography, and token source files are complete;
4. favicon/PWA/social manifests resolve to non-placeholder production assets;
5. light/dark, keyboard, screen-reader, zoom, contrast, forced-colors, and
   reduced-motion checks are recorded;
6. representative components cover interaction and failure states;
7. generated token outputs are reproducible from a pinned source;
8. the final implementation is reviewed on target devices and browsers; and
9. a named human approves release and rollback remains possible.

## Primary references

- [Design Tokens Format Module 2025.10](https://www.designtokens.org/TR/2025.10/format/)
- [brand.yml structure](https://posit-dev.github.io/brand-yml/brand/)
- [Style Dictionary documentation](https://styledictionary.com/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Storybook documentation](https://storybook.js.org/docs)

