# Next.js Stack Guide

## Detection

Look for `next` in package manifests, `app/` or `pages/`, route handlers, server actions, middleware or proxy files, Next configuration, and Vercel-oriented deployment settings.

## Required controls

Server/client boundary review, authentication and authorization at server seams, secret isolation, input validation, secure caching, error boundaries, route testing, dependency scanning, CSP and headers, image/file controls, observability, build verification, and rollback.

## Compatible capabilities

Architecture documentation, unit testing, browser testing, accessibility, API contract testing, secrets detection, SAST, dependency scanning, observability, performance testing, privacy review, and deployment verification.

## Verification

Run type checking, lint, production build, route and server-action tests, authenticated critical-path browser tests, accessibility checks, header inspection, secret scans, dependency scans, and deployment-preview verification.

## Human review

Authentication, authorization, payments, personal data, regulated workflows, production middleware, and security headers require competent review before release.
