# Brand-system starter

Copy this directory into a product repository only after completing the
brand foundation in [`docs/BRAND-SYSTEM.md`](../../docs/BRAND-SYSTEM.md).

- `_brand.yml` records logos, palette, semantic colors, and typography in the
  portable brand.yml structure.
- `tokens.tokens.json` is a small DTCG-shaped token seed. Replace every sample
  value, preserve semantic aliases, and validate it against the pinned format
  and transformer used by the target project.
- `asset-manifest.json` is the release checklist for logo, favicon, PWA, and
  social assets. Set every `status` to `approved` only after rendering and
  runtime checks; add release hashes in the target repository.

The samples are neutral scaffolding, not Internet-Well branding and not a
license to use any third-party name, mark, font, or image.

