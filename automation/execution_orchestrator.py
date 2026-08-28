#!/usr/bin/env python3
"""Internet-Well v0.6 Execution Orchestrator.

Closed-loop task coordination across Agent Brain planning, explicit authorization,
adapter execution, reliability verification, bounded recovery, durable checkpoints,
and control-plane reporting. The orchestrator never invents credentials or execution
authority; state-changing adapter calls require explicit scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from automation import agent_brain, agent_reliability

ROOT = Path(__file__).resolve().parents[1]
POLICY_REL = Path("integrations/orchestration/execution-policy.json")
ADAPTERS_REL = Path("integrations/orchestration/adapters.json")


class OrchestrationError(RuntimeError):
    pass


def _roots():
    configured = os.environ.get("INTERNET_WELL_ROOT")
    if configured:
        yield Path(configured).expanduser().resolve()
    yield ROOT
    yield Path(sys.prefix)
    yield Path(sys.base_prefix)


def _resolve(rel: Path) -> Path:
    for root in _roots():
        candidate = root / rel
        if candidate.is_file():
            return candidate
    raise OrchestrationError(f"Unable to locate orchestration data: {rel}")


def _load(rel: Path) -> dict[str, Any]:
    data = json.loads(_resolve(rel).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise OrchestrationError(f"Expected object in {rel}")
    return data


def policy() -> dict[str, Any]:
    return _load(POLICY_REL)


def adapter_registry() -> dict[str, Any]:
    return _load(ADAPTERS_REL)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _task_id(goal: str) -> str:
    return hashlib.sha256(f"{goal}|{_now()}".encode()).hexdigest()[:20]


def _checkpoint_hash(task: dict[str, Any]) -> str:
    material = {k: v for k, v in task.items() if k != "checkpoint_hash"}
    return hashlib.sha256(json.dumps(material, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def new_task(goal: str, *, risk_tier: str = "B", success_criteria: list[str] | None = None) -> dict[str, Any]:
    if risk_tier not in policy()["risk_tiers"]:
        raise OrchestrationError(f"Unknown risk tier: {risk_tier}")
    brain_plan = agent_brain.plan_implementation(goal)
    trace = agent_reliability.new_trace(goal)
    task = {
        "version": "0.6.0",
        "task_id": _task_id(goal),
        "goal": goal,
        "risk_tier": risk_tier,
        "stage": "plan",
        "status": "planned",
        "created_at": _now(),
        "updated_at": _now(),
        "success_criteria": list(success_criteria or ["goal_observable_result_verified"]),
        "brain_plan": brain_plan,
        "selected_adapters": [],
        "authorization": {"execution_authorized": False, "approved_scopes": [], "approvals": []},
        "attempts": 0,
        "history": [],
        "trace": trace,
        "verification": None,
        "regressions": [],
    }
    return checkpoint(task, "task-created")


def checkpoint(task: dict[str, Any], reason: str) -> dict[str, Any]:
    task["updated_at"] = _now()
    task.setdefault("history", []).append({"at": task["updated_at"], "stage": task.get("stage"), "status": task.get("status"), "reason": reason})
    task["checkpoint_hash"] = _checkpoint_hash(task)
    return task


def save_task(task: dict[str, Any], path: str | Path) -> Path:
    task = checkpoint(task, "checkpoint-saved")
    dest = Path(path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(task, indent=2, sort_keys=True), encoding="utf-8")
    return dest


def load_task(path: str | Path) -> dict[str, Any]:
    task = json.loads(Path(path).read_text(encoding="utf-8"))
    expected = task.get("checkpoint_hash")
    if not expected or expected != _checkpoint_hash(task):
        raise OrchestrationError("Task checkpoint integrity verification failed")
    return task


def select_adapters(task: dict[str, Any], adapter_ids: list[str]) -> dict[str, Any]:
    known = {a["id"]: a for a in adapter_registry()["adapters"]}
    unknown = [x for x in adapter_ids if x not in known]
    if unknown:
        raise OrchestrationError(f"Unknown adapters: {', '.join(unknown)}")
    task["selected_adapters"] = [known[x] for x in adapter_ids]
    task["stage"] = "select"
    task["status"] = "adapters-selected"
    agent_reliability.add_event(task["trace"], stage="select", action="select-adapters", status="success", evidence=adapter_ids)
    return checkpoint(task, "adapters-selected")


def authorize(task: dict[str, Any], *, scopes: list[str], approval: str | None = None) -> dict[str, Any]:
    if not scopes:
        raise OrchestrationError("Execution authorization requires at least one explicit scope")
    auth = task["authorization"]
    auth["execution_authorized"] = True
    auth["approved_scopes"] = sorted(set(scopes))
    if approval:
        auth.setdefault("approvals", []).append({"approval": approval, "at": _now()})
    tier = policy()["risk_tiers"][task["risk_tier"]]
    if tier["human_approval_required"] and not auth.get("approvals"):
        auth["execution_authorized"] = False
        raise OrchestrationError("Human approval is required for this risk tier")
    task["stage"] = "authorize"
    task["status"] = "authorized"
    agent_reliability.add_event(task["trace"], stage="authorize", action="record-authorization", status="success", evidence=auth["approved_scopes"], approval=approval)
    return checkpoint(task, "execution-authorized")


def _adapter_is_state_changing(adapter: dict[str, Any]) -> bool:
    return adapter.get("state_changing") is True or adapter.get("state_changing") == "depends-on-tool"


def execution_preflight(task: dict[str, Any]) -> dict[str, Any]:
    blockers: list[str] = []
    auth = task.get("authorization", {})
    if not auth.get("execution_authorized"):
        blockers.append("missing_execution_authority")
    if any(_adapter_is_state_changing(a) for a in task.get("selected_adapters", [])) and not auth.get("approved_scopes"):
        blockers.append("missing_execution_scope")
    tier = policy()["risk_tiers"][task["risk_tier"]]
    if tier["human_approval_required"] and not auth.get("approvals"):
        blockers.append("missing_required_approval")
    return {"passed": not blockers, "blockers": blockers}


def execute(task: dict[str, Any], handlers: dict[str, Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]]) -> dict[str, Any]:
    preflight = execution_preflight(task)
    if not preflight["passed"]:
        task["status"] = "blocked"
        task["stage"] = "authorize"
        agent_reliability.add_event(task["trace"], stage="authorize", action="execution-preflight", status="failed", evidence=preflight["blockers"])
        return checkpoint(task, "execution-blocked")

    task["stage"] = "execute"
    task["status"] = "running"
    task["attempts"] += 1
    results = []
    for adapter in task.get("selected_adapters", []):
        handler = handlers.get(adapter["id"])
        if handler is None:
            results.append({"adapter": adapter["id"], "status": "not-configured"})
            agent_reliability.add_event(task["trace"], stage="execute", action=adapter["id"], status="failed", evidence=["adapter-handler-not-configured"])
            continue
        try:
            result = handler(task, adapter)
            status = str(result.get("status", "success"))
            results.append({"adapter": adapter["id"], **result})
            agent_reliability.add_event(task["trace"], stage="execute", action=adapter["id"], status="success" if status in {"success", "passed"} else "failed", evidence=[str(x) for x in result.get("evidence", [])])
        except Exception as exc:  # adapters are untrusted boundaries
            results.append({"adapter": adapter["id"], "status": "failed", "error": type(exc).__name__})
            agent_reliability.add_event(task["trace"], stage="execute", action=adapter["id"], status="failed", evidence=[type(exc).__name__])
    task["execution_results"] = results
    task["status"] = "executed"
    return checkpoint(task, "execution-finished")


def build_reliability_run(task: dict[str, Any]) -> dict[str, Any]:
    success = all(r.get("status") in {"success", "passed"} for r in task.get("execution_results", [])) and bool(task.get("execution_results"))
    criteria = {c: {"passed": success, "evidence": ["adapter-results"] if success else []} for c in task["success_criteria"]}
    metrics = task["trace"].get("metrics", {})
    return {
        "criteria": criteria,
        "metrics": {
            "policy_violations": 0,
            "unverified_claims": 0,
            "hallucinated_claims": 0,
            "tool_failures": metrics.get("tool_failures", 0),
            "required_tests_failed": 0 if success else 1,
            "cost": metrics.get("cost", 0),
            "latency_ms": metrics.get("latency_ms", 0),
        },
        "evidence": [r for r in task.get("execution_results", []) if r.get("evidence")],
        "agent_status": task.get("status"),
        "required_approval_missing": policy()["risk_tiers"][task["risk_tier"]]["human_approval_required"] and not bool(task["authorization"].get("approvals")),
    }


def verify(task: dict[str, Any]) -> dict[str, Any]:
    task["stage"] = "verify"
    run = build_reliability_run(task)
    scenario_data = {
        "id": "orchestrated-task",
        "risk_tier": task["risk_tier"],
        "criteria": task["success_criteria"],
        "thresholds": {"min_score": 85, "max_policy_violations": 0, "max_unverified_claims": 0, "human_review_required": task["risk_tier"] == "A"},
    }
    result = agent_reliability.verify_completion(scenario_data, run)
    task["verification"] = result
    task["status"] = "verified" if result["status"] == "PASS" else result["status"].lower()
    task["trace"]["final_state"] = task["status"]
    agent_reliability.add_event(task["trace"], stage="verify", action="independent-verifier", status="success" if result["status"] == "PASS" else "failed", evidence=[result["status"]])
    return checkpoint(task, "verification-finished")


def should_retry(task: dict[str, Any]) -> bool:
    if not task.get("verification") or task["verification"]["status"] != "FAIL":
        return False
    hard = set(task["verification"].get("hard_failures", []))
    if "policy_violation" in hard or "unauthorized_state_change" in hard or "secret_exposure" in hard:
        return False
    limit = int(policy()["risk_tiers"][task["risk_tier"]]["max_retries"])
    return task.get("attempts", 0) <= limit


def recover(task: dict[str, Any], recovery_handler: Callable[[dict[str, Any]], dict[str, Any]] | None = None) -> dict[str, Any]:
    task["stage"] = "recover"
    if not should_retry(task):
        task["status"] = "recovery-stopped"
        return checkpoint(task, "retry-not-permitted")
    recovery = recovery_handler(task) if recovery_handler else {"status": "planned", "evidence": ["manual-recovery-required"]}
    task.setdefault("recovery", []).append(recovery)
    task["status"] = "recovery-ready"
    return checkpoint(task, "recovery-prepared")


def complete(task: dict[str, Any]) -> dict[str, Any]:
    verification = task.get("verification") or {}
    if verification.get("status") != "PASS":
        raise OrchestrationError("Cannot complete task until independent verifier returns PASS")
    task["stage"] = "complete"
    task["status"] = "completed"
    task["trace"]["final_state"] = "completed"
    return checkpoint(task, "task-completed")


def control_plane(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "task_id": task["task_id"],
        "goal": task["goal"],
        "risk_tier": task["risk_tier"],
        "stage": task["stage"],
        "status": task["status"],
        "attempts": task.get("attempts", 0),
        "adapters": [a["id"] for a in task.get("selected_adapters", [])],
        "authorization": {"authorized": task["authorization"].get("execution_authorized"), "scopes": task["authorization"].get("approved_scopes", []), "approvals": len(task["authorization"].get("approvals", []))},
        "verification": task.get("verification"),
        "trace": agent_reliability.trajectory_summary(task["trace"]),
        "last_checkpoint": task.get("checkpoint_hash"),
    }


def _print(value: Any) -> None:
    print(json.dumps(value, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description="Internet-Well Execution Orchestrator v0.6")
    sub = parser.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new"); n.add_argument("goal"); n.add_argument("--risk", default="B", choices=["A", "B", "C"]); n.add_argument("--criterion", action="append", default=[]); n.add_argument("--out")
    s = sub.add_parser("select"); s.add_argument("task_json"); s.add_argument("adapters", nargs="+"); s.add_argument("--out")
    a = sub.add_parser("authorize"); a.add_argument("task_json"); a.add_argument("--scope", action="append", required=True); a.add_argument("--approval"); a.add_argument("--out")
    v = sub.add_parser("verify"); v.add_argument("task_json"); v.add_argument("--out")
    c = sub.add_parser("control-plane"); c.add_argument("task_json")
    r = sub.add_parser("resume"); r.add_argument("task_json")
    args = parser.parse_args()

    if args.cmd == "new":
        task = new_task(args.goal, risk_tier=args.risk, success_criteria=args.criterion or None)
    elif args.cmd == "select":
        task = select_adapters(load_task(args.task_json), args.adapters)
    elif args.cmd == "authorize":
        task = authorize(load_task(args.task_json), scopes=args.scope, approval=args.approval)
    elif args.cmd == "verify":
        task = verify(load_task(args.task_json))
    elif args.cmd == "control-plane":
        _print(control_plane(load_task(args.task_json))); return
    elif args.cmd == "resume":
        _print(control_plane(load_task(args.task_json))); return
    else:
        raise OrchestrationError("Unsupported command")

    out = getattr(args, "out", None)
    if out:
        save_task(task, out)
    _print(task)


if __name__ == "__main__":
    main()
