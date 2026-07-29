# Node.js Stack Guide

## Detection

Look for `package.json`, lockfiles, Node runtime declarations, server frameworks, workers, scripts, package workspaces, and test tooling.

## Required controls

Runtime pinning, lockfile integrity, dependency review, secrets isolation, input validation, async error handling, resource limits, secure subprocess use, logging, package scripts, and reproducible builds.

## Compatible capabilities

Unit and integration testing, type checking, linting, dependency scanning, secrets detection, SAST, API testing, package provenance, performance testing, and observability.

## Verification

Install from the lockfile in a clean environment; run tests, type checks, lint, dependency and secret scans; build production artifacts; exercise critical APIs; inspect startup, shutdown, retry, and failure behavior.

## Human review

Production services, package publishing, native modules, authentication, payments, regulated data, and code-execution features require competent review.
