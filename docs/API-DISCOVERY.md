# Governed API Discovery

Internet-Well uses `public-apis/public-apis` as a **discovery source**, not as an approval authority or a promise of free/unlimited access.

The source is pinned to commit `988c57be4616cc9507fd3e8c34adedba5387f079`. Agents may search a locally pinned copy for candidate APIs, but Internet-Well does not automatically call discovered services.

## Commands

```bash
internet-well-api-discovery show
internet-well-api-discovery install-source --approve
internet-well-api-discovery find "currency"
internet-well-api-discovery plan-use "Frankfurter"
```

`find` ranks catalog matches only as candidates. Before an API is wired into an application, verify the current provider, official documentation, authentication model, TLS support, pricing/free tier, quotas, rate limits, terms, license, data quality, privacy/retention, CORS exposure, availability, and deprecation status.

## Hard rules

- Never use leaked, copied, shared, or third-party credentials to avoid provider pricing or quotas.
- A catalog entry is not evidence that an API is currently free, unlimited, secure, lawful for the intended use, or production-ready.
- Financial, health, legal, safety-critical, credential-bearing, or sensitive-data uses require human review before adoption.
- Prefer official provider documentation over catalog descriptions whenever they differ.
- Keep API secrets out of repositories and client-side code unless the provider explicitly designs the credential for public exposure.

The upstream catalog retains its own MIT license. Internet-Well does not relicense the APIs or providers listed in that catalog.
