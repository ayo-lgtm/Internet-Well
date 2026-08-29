#!/usr/bin/env python3
"""Internet-Well Autonomous Engineering System.

Builds a small, role-specialized software team around the governed execution
orchestrator. It plans task graphs, assigns specialist/reviewer roles, routes
model-provider preferences, preserves approval boundaries, and emits independent
verification gates. It does not execute external tools or bypass host authorization.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from automation import execution_orchestrator as orchestrator


@dataclass(frozen=True)
class Role:
    id: str
    mission: str
    capabilities: tuple[str, ...]
    independent_from: tuple[str, ...] = ()


ROLES: tuple[Role, ...] = (
    Role("chief-of-staff", "Own scope, decomposition, sequencing, blockers, and escalation.", ("planning", "coordination", "task-graph", "handoff")),
    Role("product", "Translate the goal into observable user and product acceptance criteria.", ("requirements", "product", "acceptance-criteria")),
    Role("ux", "Design usable flows, interaction states, accessibility, and visual validation.", ("ui", "ux", "design", "accessibility")),
    Role("engineer", "Implement the smallest correct code changes with tests and rollback awareness.", ("code", "backend", "frontend", "database", "integration")),
    Role("security", "Threat-model changes and verify auth, secrets, dependencies, abuse, and supply-chain risk.", ("security", "auth", "privacy", "secrets", "supply-chain")),
    Role("qa", "Exercise critical journeys and convert failures into reproducible regression cases.", ("testing", "e2e", "regression", "browser", "quality"), independent_from=("engineer",)),
    Role("compliance", "Review licensing, privacy, legal/compliance constraints, and provenance when relevant.", ("license", "privacy", "legal", "compliance", "provenance"), independent_from=("engineer",)),
    Role("release", "Verify deployment evidence, rollback, observability, and release readiness.", ("deploy", "release", "observability", "rollback"), independent_from=("engineer",)),
    Role("verifier", "Independently determine completion from evidence rather than implementer self-report.", ("evaluation", "verification", "evidence", "reliability"), independent_from=("engineer", "chief-of-staff")),
)

ROLE_BY_ID = {r.id: r for r in ROLES}

PROVIDERS: tuple[dict[str, Any], ...] = (
    {"id": "codex", "strengths": {"code", "repository", "debug", "tests", "tool-use"}, "cost": 2, "latency": 2},
    {"id": "claude", "strengths": {"code", "architecture", "review", "long-context", "writing"}, "cost": 2, "latency": 2},
    {"id": "gemini", "strengths": {"multimodal", "research", "long-context", "code"}, "cost": 1, "latency": 2},
    {"id": "grok", "strengths": {"research", "code", "tool-use", "reasoning"}, "cost": 2, "latency": 2},
    {"id": "groq", "strengths": {"low-latency", "classification", "routing", "summarization"}, "cost": 1, "latency": 1},
)


def _terms(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9][a-z0-9+._-]*", text.casefold()) if len(w) > 2}


def select_roles(goal: str) -> list[Role]:
    text = goal.casefold()
    selected = {"chief-of-staff", "engineer", "qa", "verifier"}
    triggers = {
        "product": ("product", "user", "workflow", "feature", "retention", "launch"),
        "ux": ("ui", "ux", "design", "mobile", "accessibility", "screen", "flow"),
        "security": ("security", "auth", "login", "secret", "api", "database", "payment", "production", "fingerprint", "fraud"),
        "compliance": ("legal", "privacy", "license", "compliance", "health", "financial", "fingerprint", "tracking"),
        "release": ("production", "deploy", "release", "vercel", "railway", "supabase", "launch"),
    }
    for role_id, words in triggers.items():
        if any(word in text for word in words):
            selected.add(role_id)
    order = [r.id for r in ROLES]
    return [ROLE_BY_ID[r] for r in order if r in selected]


def provider_route(goal: str, role: Role) -> list[dict[str, Any]]:
    wanted = _terms(goal) | set(role.capabilities)
    ranked = []
    for provider in PROVIDERS:
        overlap = len(wanted & provider["strengths"])
        score = overlap * 10 - provider["cost"] - provider["latency"]
        ranked.append({"provider": provider["id"], "score": score, "matched": sorted(wanted & provider["strengths"])})
    ranked.sort(key=lambda x: (-x["score"], x["provider"]))
    return ranked


def build_task_graph(goal: str) -> dict[str, Any]:
    roles = select_roles(goal)
    nodes: list[dict[str, Any]] = []
    previous = None
    for ordinal, role in enumerate(roles, start=1):
        node_id = f"{ordinal:02d}-{role.id}"
        deps: list[str] = []
        if role.id == "chief-of-staff":
            deps = []
        elif role.id == "verifier":
            deps = [n["id"] for n in nodes if n["role"] in {"qa", "security", "compliance", "release"}] or ([previous] if previous else [])
        elif role.id in {"qa", "security", "compliance", "release"}:
            engineer = next((n["id"] for n in nodes if n["role"] == "engineer"), previous)
            deps = [engineer] if engineer else []
        elif previous:
            deps = [previous]
        nodes.append({
            "id": node_id,
            "role": role.id,
            "mission": role.mission,
            "depends_on": deps,
            "independent_from": list(role.independent_from),
            "provider_route": provider_route(goal, role)[:3],
            "status": "pending",
        })
        previous = node_id
    return {"goal": goal, "nodes": nodes, "completion_gate": "verifier must rely on observable evidence and must not be the implementer"}


def build_team(goal: str, *, state_dir: Path | None = None, plan_only: bool = False) -> dict[str, Any]:
    kwargs: dict[str, Any] = {"plan_only": plan_only}
    if state_dir is not None:
        kwargs["state_dir"] = state_dir
    task = orchestrator.start_task(goal, **kwargs)
    graph = build_task_graph(goal)
    return {
        "task_id": task["task_id"],
        "risk_tier": task["risk_tier"],
        "scenario_id": task["scenario_id"],
        "selected_adapters": task["selected_adapters"],
        "team": [asdict(r) for r in select_roles(goal)],
        "task_graph": graph,
        "governance": {
            "external_execution": "host adapters only",
            "state_changes": "explicit approval through execution_orchestrator",
            "credentials": "never persisted in task graph or task state",
            "independent_verification": True,
            "bounded_recovery": True,
        },
    }


def model_routing_policy(goal: str) -> dict[str, Any]:
    return {
        "goal": goal,
        "policy": "Prefer capability fit, then lower cost/latency; hosts may substitute providers but must preserve role and verification independence.",
        "routes": {role.id: provider_route(goal, role) for role in select_roles(goal)},
        "fallback_rule": "On provider failure, move to the next ranked provider without weakening tool permissions or approval requirements.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Internet-Well Autonomous Engineering System")
    sub = parser.add_subparsers(dest="cmd", required=True)
    team = sub.add_parser("team")
    team.add_argument("goal")
    team.add_argument("--state-dir", type=Path)
    team.add_argument("--plan-only", action="store_true")
    graph = sub.add_parser("graph")
    graph.add_argument("goal")
    route = sub.add_parser("route")
    route.add_argument("goal")
    args = parser.parse_args()
    if args.cmd == "team":
        out = build_team(args.goal, state_dir=args.state_dir, plan_only=args.plan_only)
    elif args.cmd == "graph":
        out = build_task_graph(args.goal)
    else:
        out = model_routing_policy(args.goal)
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
