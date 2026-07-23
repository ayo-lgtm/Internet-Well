# Licensing

This directory summarizes license obligations across the registry so a
founder (or agent) can answer "what does using this oblige me to do?"
without re-reading 55 records.

- [`obligations-matrix.md`](obligations-matrix.md) — every SPDX license
  family in the registry, its obligations, and which records carry it.

Rules this registry follows:

1. Licenses are read from license files and registry metadata at the
   pinned version — never from repo badges or listicles (badge/LICENSE
   mismatches were found during research, e.g. Chatwoot).
2. Open-core boundaries are recorded explicitly: directory-based
   (Chatwoot `enterprise/`, Documenso `packages/ee`, Metabase in-repo
   commercial editions) or file-marker-based (Twenty
   `/* @license Enterprise */`).
3. Licenses are re-verified on every entry touch and every major-version
   upgrade — license changes ride majors.
4. Registry content itself is CC-BY-4.0; described resources retain their
   own licenses.

This summary is not legal advice; consult counsel for anything with legal
effect (see each record's Required-human-review section).
