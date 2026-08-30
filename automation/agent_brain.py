#!/usr/bin/env python3
"""Internet-Well v0.4 Agent Brain: capability graph, router, ranking, bundles, and MCP stdio server."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable

SOURCE_ROOT = Path(__file__).resolve().parents[1]
GRAPH_REL = Path("integrations/agent-brain/capability-graph.json")
BUNDLES_REL = Path("bundles/agent-brain-bundles.json")
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9+._-]*")


class BrainError(RuntimeError):
    pass


def _roots() -> Iterable[Path]:
    configured = os.environ.get("INTERNET_WELL_ROOT")
    if configured:
        yield Path(configured).expanduser().resolve()
    yield SOURCE_ROOT
    yield Path(sys.prefix)
    yield Path(sys.base_prefix)


def _resolve(rel: Path) -> Path:
    for root in _roots():
        p = root / rel
        if p.is_file():
            return p
    raise BrainError(f"Unable to locate required Agent Brain data: {rel}")


def _load(rel: Path) -> dict[str, Any]:
    data = json.loads(_resolve(rel).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise BrainError(f"Invalid JSON object: {rel}")
    return data


def graph() -> dict[str, Any]:
    data = _load(GRAPH_REL)
    if not isinstance(data.get("nodes"), list) or not data["nodes"]:
        raise BrainError("Capability graph is empty.")
    return data


def bundles() -> dict[str, Any]:
    data = _load(BUNDLES_REL)
    if not isinstance(data.get("bundles"), list) or not data["bundles"]:
        raise BrainError("Bundle registry is empty.")
    return data


def tokens(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def evidence_score(node: dict[str, Any]) -> float:
    weights = graph().get("ranking_weights", {})
    evidence = node.get("evidence", {})
    if not weights:
        return 0.0
    total = 0.0
    weight_total = 0.0
    for key, weight in weights.items():
        try:
            w = float(weight)
            value = float(evidence.get(key, 0))
        except (TypeError, ValueError):
            continue
        total += value * w
        weight_total += w
    return round(total / weight_total, 2) if weight_total else 0.0


def _restricted(node: dict[str, Any]) -> bool:
    restrictions = {str(x).lower() for x in node.get("restrictions", [])}
    return node.get("kind") == "restricted-reference" or "reference-only" in restrictions


def _search_text(node: dict[str, Any]) -> str:
    values: list[str] = [str(node.get("id", "")), str(node.get("kind", "")), str(node.get("source", ""))]
    values.extend(str(x) for x in node.get("capabilities", []))
    values.extend(str(x) for x in node.get("restrictions", []))
    return " ".join(values).lower()


def rank(query: str, kind: str | None = None, limit: int = 8, include_restricted: bool = False) -> list[dict[str, Any]]:
    q = tokens(query)
    ranked: list[dict[str, Any]] = []
    for node in graph()["nodes"]:
        if kind and node.get("kind") != kind:
            continue
        if _restricted(node) and not include_restricted:
            continue
        hay = tokens(_search_text(node))
        lexical = len(q & hay) / max(1, len(q))
        capability_hits = len(q & tokens(" ".join(node.get("capabilities", []))))
        evidence = evidence_score(node)
        final = round((lexical * 45.0) + min(capability_hits * 6.0, 18.0) + (evidence * 0.37), 2)
        if q and lexical == 0 and capability_hits == 0:
            continue
        ranked.append({
            "id": node.get("id"),
            "kind": node.get("kind"),
            "source": node.get("source"),
            "capabilities": node.get("capabilities", []),
            "restrictions": node.get("restrictions", []),
            "evidence_score": evidence,
            "match_score": final,
        })
    ranked.sort(key=lambda x: (x["match_score"], x["evidence_score"]), reverse=True)
    return ranked[: max(1, limit)]


def route(goal: str) -> dict[str, Any]:
    goal_l = goal.lower()
    goal_tokens = tokens(goal)
    candidates: list[tuple[int, dict[str, Any]]] = []
    for bundle in bundles()["bundles"]:
        score = 0
        for pattern in bundle.get("goal_patterns", []):
            p = str(pattern).lower()
            if p in goal_l:
                score += 10 + len(tokens(p))
            score += len(goal_tokens & tokens(p))
        candidates.append((score, bundle))
    candidates.sort(key=lambda x: x[0], reverse=True)
    selected = candidates[0][1] if candidates and candidates[0][0] > 0 else None
    if selected:
        preferred = []
        by_id = {n["id"]: n for n in graph()["nodes"]}
        for rid in selected.get("preferred", []):
            node = by_id.get(rid)
            if node and not _restricted(node):
                preferred.append({"id": rid, "kind": node.get("kind"), "evidence_score": evidence_score(node), "restrictions": node.get("restrictions", [])})
        return {
            "goal": goal,
            "bundle": selected["id"],
            "required_capabilities": selected.get("capabilities", []),
            "preferred_resources": preferred,
            "verification": selected.get("verification", []),
            "restriction": selected.get("restriction"),
            "decision": "recommendation-only; explicit authorization required before state-changing implementation",
        }
    return {
        "goal": goal,
        "bundle": None,
        "required_capabilities": [],
        "preferred_resources": rank(goal),
        "verification": ["define-success-criteria", "least-privilege", "rollback", "runtime-test"],
        "decision": "no exact bundle matched; capability ranking returned",
    }


def find_capability(capability: str, limit: int = 8) -> dict[str, Any]:
    return {"capability": capability, "results": rank(capability, limit=limit)}


def recommend_stack(goal: str) -> dict[str, Any]:
    return route(goal)


def find_api(query: str, limit: int = 8) -> dict[str, Any]:
    # Internet-Well's detailed Public APIs catalog parser lives in automation.api_discovery.
    # This method routes agents to that governed source instead of silently calling providers.
    resources = rank(f"api discovery {query}", limit=limit)
    return {
        "query": query,
        "discovery_sources": resources,
        "next_command": f"internet-well-api-discovery find {json.dumps(query)}",
        "policy": "Verify provider identity, pricing, quota, authentication, TLS, terms, privacy, CORS, availability, and data quality before adoption. Never use leaked credentials.",
    }


def get_skill(query: str, limit: int = 8) -> dict[str, Any]:
    kinds = {"skill-family", "skill-library", "code-quality-skill", "workflow-system"}
    results = []
    for item in rank(query, limit=50):
        if item.get("kind") in kinds:
            results.append(item)
    return {"query": query, "results": results[:limit]}


def plan_implementation(goal: str) -> dict[str, Any]:
    decision = route(goal)
    return {
        **decision,
        "implementation_phases": [
            "1. Confirm goal, success metrics, data classification, and non-goals.",
            "2. Verify selected upstream pins, licenses, permissions, dependencies, and provider terms.",
            "3. Run baseline/no-integration fixture and record evidence.",
            "4. Implement the smallest compatible resource bundle in an isolated/reversible environment.",
            "5. Run unit, integration, security, accessibility, and runtime checks applicable to the bundle.",
            "6. Compare results against baseline and reject components that do not materially improve the target metric.",
            "7. Obtain human approval for Tier A, regulated, financial, legal, production-write, or credential-bearing actions.",
            "8. Record decision, exact pins, evidence, limitations, rollback, and upstream-monitoring plan.",
        ],
        "authorization": "planning does not authorize installation, deployment, live trading, production writes, or use of third-party credentials",
    }


def evaluate(bundle_id: str) -> dict[str, Any]:
    registry = {b["id"]: b for b in bundles()["bundles"]}
    bundle = registry.get(bundle_id)
    if not bundle:
        raise BrainError(f"Unknown bundle: {bundle_id}")
    nodes = {n["id"]: n for n in graph()["nodes"]}
    missing = [rid for rid in bundle.get("preferred", []) if rid not in nodes]
    restricted = [rid for rid in bundle.get("preferred", []) if rid in nodes and _restricted(nodes[rid])]
    scores = {rid: evidence_score(nodes[rid]) for rid in bundle.get("preferred", []) if rid in nodes}
    average = round(sum(scores.values()) / len(scores), 2) if scores else 0.0
    checks = {
        "all_resources_resolve": not missing,
        "no_restricted_resource_in_default_bundle": not restricted,
        "verification_defined": bool(bundle.get("verification")),
        "capabilities_defined": bool(bundle.get("capabilities")),
        "evidence_scores_present": bool(scores) and all(v > 0 for v in scores.values()),
    }
    return {
        "bundle": bundle_id,
        "passed": all(checks.values()),
        "checks": checks,
        "missing": missing,
        "restricted": restricted,
        "resource_evidence_scores": scores,
        "average_evidence_score": average,
        "verification": bundle.get("verification", []),
        "note": "This structural lab validates the governed architecture. Product-specific runtime claims require fixture or production-equivalent testing.",
    }


def evaluate_all() -> dict[str, Any]:
    results = [evaluate(b["id"]) for b in bundles()["bundles"]]
    return {"passed": all(x["passed"] for x in results), "bundles": results}


def mcp_tools() -> list[dict[str, Any]]:
    def tool(name: str, description: str, props: dict[str, Any], required: list[str]) -> dict[str, Any]:
        return {"name": name, "description": description, "inputSchema": {"type": "object", "properties": props, "required": required, "additionalProperties": False}}
    return [
        tool("find_capability", "Rank governed resources for a capability.", {"capability": {"type": "string"}, "limit": {"type": "integer", "minimum": 1, "maximum": 20}}, ["capability"]),
        tool("recommend_stack", "Route a product/agent goal to the best governed bundle.", {"goal": {"type": "string"}}, ["goal"]),
        tool("find_api", "Route an API need to Internet-Well's governed API discovery source.", {"query": {"type": "string"}, "limit": {"type": "integer", "minimum": 1, "maximum": 20}}, ["query"]),
        tool("get_skill", "Rank governed skills/workflow resources.", {"query": {"type": "string"}, "limit": {"type": "integer", "minimum": 1, "maximum": 20}}, ["query"]),
        tool("plan_implementation", "Create a reversible, evidence-backed implementation plan for a goal.", {"goal": {"type": "string"}}, ["goal"]),
        tool("evaluate_bundle", "Run the structural evaluation lab for a composed bundle.", {"bundle_id": {"type": "string"}}, ["bundle_id"]),
    ]


def call_tool(name: str, args: dict[str, Any]) -> Any:
    if name == "find_capability":
        return find_capability(str(args["capability"]), int(args.get("limit", 8)))
    if name == "recommend_stack":
        return recommend_stack(str(args["goal"]))
    if name == "find_api":
        return find_api(str(args["query"]), int(args.get("limit", 8)))
    if name == "get_skill":
        return get_skill(str(args["query"]), int(args.get("limit", 8)))
    if name == "plan_implementation":
        return plan_implementation(str(args["goal"]))
    if name == "evaluate_bundle":
        return evaluate(str(args["bundle_id"]))
    raise BrainError(f"Unknown tool: {name}")


def _mcp_result(request_id: Any, payload: Any) -> dict[str, Any]:
    text = json.dumps(payload, indent=2, sort_keys=True)
    return {"jsonrpc": "2.0", "id": request_id, "result": {"content": [{"type": "text", "text": text}], "structuredContent": payload}}


def serve_stdio() -> int:
    """Dependency-free MCP 2025-style stdio JSON-RPC subset for initialize/tools/list/tools/call."""
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        request_id: Any = None
        try:
            req = json.loads(raw)
            request_id = req.get("id")
            method = req.get("method")
            params = req.get("params") or {}
            if method == "initialize":
                result = {"protocolVersion": params.get("protocolVersion", "2025-06-18"), "capabilities": {"tools": {"listChanged": False}}, "serverInfo": {"name": "internet-well-agent-brain", "version": "0.5.0"}}
                response = {"jsonrpc": "2.0", "id": request_id, "result": result}
            elif method == "notifications/initialized":
                continue
            elif method == "tools/list":
                response = {"jsonrpc": "2.0", "id": request_id, "result": {"tools": mcp_tools()}}
            elif method == "tools/call":
                response = _mcp_result(request_id, call_tool(str(params.get("name")), dict(params.get("arguments") or {})))
            elif method == "ping":
                response = {"jsonrpc": "2.0", "id": request_id, "result": {}}
            else:
                response = {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}
        except Exception as exc:  # keep server alive for malformed tool requests
            response = {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32000, "message": str(exc)}}
        sys.stdout.write(json.dumps(response, separators=(",", ":")) + "\n")
        sys.stdout.flush()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-brain", description="Governed capability graph, router, evaluation lab, and MCP server.")
    subs = parser.add_subparsers(dest="command", required=True)
    p = subs.add_parser("find-capability"); p.add_argument("query"); p.add_argument("--limit", type=int, default=8)
    p = subs.add_parser("recommend-stack"); p.add_argument("goal")
    p = subs.add_parser("find-api"); p.add_argument("query"); p.add_argument("--limit", type=int, default=8)
    p = subs.add_parser("get-skill"); p.add_argument("query"); p.add_argument("--limit", type=int, default=8)
    p = subs.add_parser("plan"); p.add_argument("goal")
    p = subs.add_parser("evaluate"); p.add_argument("bundle_id", nargs="?")
    subs.add_parser("list-tools")
    subs.add_parser("serve")
    args = parser.parse_args()
    try:
        if args.command == "find-capability": payload = find_capability(args.query, args.limit)
        elif args.command == "recommend-stack": payload = recommend_stack(args.goal)
        elif args.command == "find-api": payload = find_api(args.query, args.limit)
        elif args.command == "get-skill": payload = get_skill(args.query, args.limit)
        elif args.command == "plan": payload = plan_implementation(args.goal)
        elif args.command == "evaluate": payload = evaluate(args.bundle_id) if args.bundle_id else evaluate_all()
        elif args.command == "list-tools": payload = mcp_tools()
        else: return serve_stdio()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0
    except (BrainError, KeyError, TypeError, ValueError, OSError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
