# Docker Stack Guide

## Detection

Look for Dockerfiles, Compose files, container manifests, build contexts, registries, volume mounts, health checks, and container-based CI or deployment.

## Required controls

Minimal trusted base images, non-root runtime, pinned digests where practical, multi-stage builds, secret-free layers, narrow network and filesystem access, health checks, resource limits, image scanning, SBOMs, provenance, and rebuild policy.

## Compatible capabilities

Container scanning, SBOM generation, dependency and license review, secrets detection, reproducible builds, runtime hardening, deployment verification, observability, and disaster recovery.

## Verification

Build without cached secrets; inspect image history and user; scan vulnerabilities and licenses; generate an SBOM; run health and failure tests; validate mounts, ports, environment variables, resource limits, and reproducibility.

## Human review

Privileged containers, host mounts, production credentials, internet-exposed services, regulated data, and orchestration changes require security and operations review.
