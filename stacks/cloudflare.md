# Cloudflare Stack Guide

## Detection

Look for Workers, Pages, Wrangler configuration, DNS zones, proxy settings, WAF rules, R2, D1, KV, Durable Objects, Queues, or Turnstile.

## Required controls

Account and token scoping, environment separation, DNS ownership, caching correctness, WAF and rate-limit review, data-location awareness, secret isolation, storage consistency, observability, rollback, and provider-failure planning.

## Compatible capabilities

Edge security, CDN and caching review, serverless testing, secrets management, storage validation, DDoS and abuse controls, observability, deployment verification, and cost analysis.

## Verification

Test preview and production separation; inspect DNS, cache headers, redirects, WAF and rate limits; validate storage consistency and failure behavior; confirm token scope, logs, deployment history, and rollback.

## Human review

DNS, production traffic, firewall rules, personal or regulated data, account tokens, billing, and destructive storage changes require explicit authorization and qualified review.
