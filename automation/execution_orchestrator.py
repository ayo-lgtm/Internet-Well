#!/usr/bin/env python3
"""Internet-Well Execution Orchestration v0.6.

Coordinates Agent Brain planning, governed knowledge routing, durable task state,
host capability adapters, approvals, bounded recovery, and independent reliability
verification. External systems are invoked by the host/agent runtime, never silently
by this module.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from automation import agent_brain, agent_reliability, knowledge_discovery

ROOT = Path(__file__).resolve().parents[1]
POLICY_REL = Path("integrations/orchestration/orchestration-policy.json")
ADAPTERS_REL = Path("integrations/orchestration/adapters.json")
DEFAULT_STATE_DIR = Path(os.environ.get("INTERNET_WELL_TASK_STATE", Path.home() / ".local" / "share" / "internet-well" / "tasks"))
SCHEMA_VERSION = "0.6.0"
SECRET_KEYS = {"password", "secret", "token", "api_key", "apikey", "access_token", "refresh_token", "credential", "credentials", "private_key"}


class OrchestrationError(RuntimeError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


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
    raise OrchestrationError(f"Unable to locate required orchestration data: {rel}")


def _load_json(rel: Path) -> dict[str, Any]:
    data = json.loads(_resolve(rel).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise OrchestrationError(f"Invalid JSON object: {rel}")
    return data


def policy() -> dict[str, Any]:
    return _load_json(POLICY_REL)


def adapter_registry() -> dict[str, Any]:
    data = _load_json(ADAPTERS_REL)
    if not data.get("adapters"):
        raise OrchestrationError("Adapter registry is empty")
    return data


def _task_id(goal: str) -> str:
    seed = f"{goal}|{_now()}|{os.getpid()}"
    return hashlib.sha256(seed.encode()).hexdigest()[:20]


def _action_id(task_id: str, adapter: str, action: str, ordinal: int) -> str:
    seed = f"{task_id}|{adapter}|{action}|{ordinal}|{_now()}"
    return hashlib.sha256(seed.encode()).hexdigest()[:18]


def _state_path(task_id: str, state_dir: Path = DEFAULT_STATE_DIR) -> Path:
    if not re.fullmatch(r"[a-f0-9]{20}", task_id):
        raise OrchestrationError("Invalid task id")
    return state_dir.expanduser().resolve() / f"{task_id}.json"


def _contains_secret_key(value: Any) -> bool:
    if isinstance(value, dict):
        for key, item in value.items():
            if str(key).casefold() in SECRET_KEYS:
                return True
            if _contains_secret_key(item):
                return True
    elif isinstance(value, list):
        return any(_contains_secret_key(item) for item in value)
    return False


def save_task(task: dict[str, Any], state_dir: Path = DEFAULT_STATE_DIR) -> Path:
    task = agent_reliability.sanitize(task)
    path = _state_path(task["task_id"], state_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    task["updated_at"] = _now()
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(task, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)
    return path


def load_task(task_id: str, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    path = _state_path(task_id, state_dir)
    if not path.is_file():
        raise OrchestrationError(f"Task not found: {task_id}")
    task = json.loads(path.read_text(encoding="utf-8"))
    if task.get("schema_version") != SCHEMA_VERSION:
        raise OrchestrationError("Unsupported task schema")
    return task


def list_tasks(state_dir: Path = DEFAULT_STATE_DIR) -> list[dict[str, Any]]:
    root = state_dir.expanduser().resolve()
    if not root.is_dir():
        return []
    items = []
    for path in sorted(root.glob("*.json")):
        try:
            task = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if task.get("schema_version") == SCHEMA_VERSION:
            items.append(task)
    return items


def infer_risk_tier(goal: str) -> str:
    text = goal.casefold()
    tier_a = ["production", "deploy", "merge", "release", "credential", "secret", "payment", "financial", "legal", "compliance", "soc 2", "soc2", "security", "delete", "database migration", "write to"]
    return "A" if any(term in text for term in tier_a) else "B"


def infer_scenario(goal: str) -> str | None:
    text = goal.casefold()
    if "soc 2" in text or "soc2" in text:
        return "soc2-readiness-architecture"
    if "crawl" in text or "scrap" in text or "web extraction" in text:
        return "authorized-web-extraction"
    if "mcp" in text:
        return "mcp-server-selection"
    if "local llm" in text or "ollama" in text:
        return "local-llm-runtime-selection"
    if any(term in text for term in ["ui", "ux", "design", "prototype", "design system"]):
        return "agentic-design-handoff"
    if any(term in text for term in ["code", "repository", "github", "deploy", "production", "release", "vercel", "railway", "supabase"]):
        return "production-code-change"
    return None


def _adapter_score(goal: str, adapter: dict[str, Any]) -> int:
    words = set(re.findall(r"[a-z0-9][a-z0-9+._-]*", goal.casefold()))
    hay = " ".join([adapter.get("id", ""), adapter.get("name", "")] + adapter.get("capabilities", []) + adapter.get("keywords", [])).casefold()
    score = sum(1 for word in words if len(word) > 2 and word in hay)
    for keyword in adapter.get("keywords", []):
        if keyword.casefold() in goal.casefold():
            score += 5
    return score


def select_adapters(goal: str, limit: int = 5) -> list[dict[str, Any]]:
    ranked = []
    for adapter in adapter_registry()["adapters"]:
        score = _adapter_score(goal, adapter)
        if score:
            ranked.append({"id": adapter["id"], "name": adapter["name"], "score": score, "capabilities": adapter.get("capabilities", []), "execution_boundary": adapter.get("execution_boundary")})
    ranked.sort(key=lambda item: (-item["score"], item["id"]))
    return ranked[:limit]


def start_task(goal: str, *, state_dir: Path = DEFAULT_STATE_DIR, risk_tier: str | None = None, scenario_id: str | None = None, plan_only: bool = False) -> dict[str, Any]:
    task_id = _task_id(goal)
    risk = risk_tier or infer_risk_tier(goal)
    scenario_id = scenario_id or infer_scenario(goal)
    trace = agent_reliability.new_trace(goal, scenario_id=scenario_id)
    agent_reliability.add_event(trace, stage="intake", action="accept-goal", status="success", evidence=["goal-recorded"])
    brain_plan = agent_brain.plan_implementation(goal)
    knowledge_plan = knowledge_discovery.plan(goal)
    adapters = select_adapters(goal)
    agent_reliability.add_event(trace, stage="planning", action="agent-brain-plan", status="success", evidence=[brain_plan.get("bundle") or "capability-ranking"])
    agent_reliability.add_event(trace, stage="discovery", action="knowledge-route", status="success", evidence=[item["source"] for item in knowledge_plan.get("sources", [])[:5]])
    task = {
        "schema_version": SCHEMA_VERSION,
        "task_id": task_id,
        "goal": goal,
        "risk_tier": risk,
        "scenario_id": scenario_id,
        "plan_only": bool(plan_only),
        "created_at": _now(),
        "updated_at": _now(),
        "status": "planned" if plan_only else "awaiting-actions",
        "stage": "planning-complete",
        "checkpoint": "planning-complete",
        "brain_plan": brain_plan,
        "knowledge_plan": knowledge_plan,
        "selected_adapters": adapters,
        "actions": [],
        "approvals": [],
        "criteria": {},
        "evidence": ["brain-plan-created", "knowledge-route-created"],
        "recovery": {"attempts": {}, "proposals": []},
        "verification": None,
        "release_approval": None,
        "trace": trace,
        "metrics": {"cost": 0.0, "latency_ms": 0, "tool_failures": 0},
        "boundaries": {"external_execution": "host-adapter-only", "credentials": "never persisted; use host-managed credential references", "state_changes": "explicit approval required", "completion": "independent verifier required"},
    }
    save_task(task, state_dir)
    return task


def _adapter(adapter_id: str) -> dict[str, Any]:
    for adapter in adapter_registry()["adapters"]:
        if adapter["id"] == adapter_id:
            return adapter
    raise OrchestrationError(f"Unknown adapter: {adapter_id}")


def _action_side_effect(adapter: dict[str, Any], action: str) -> str:
    if action in adapter.get("read_only_actions", []):
        return "read-only"
    if action in adapter.get("state_changing_actions", []):
        return "state-changing"
    return "unknown"


def request_action(task_id: str, adapter_id: str, action: str, payload: dict[str, Any] | None = None, *, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    adapter = _adapter(adapter_id)
    payload = dict(payload or {})
    if _contains_secret_key(payload):
        raise OrchestrationError("Credential material may not be persisted in task payloads; use a host-managed credential_ref")
    side_effect = _action_side_effect(adapter, action)
    if side_effect == "unknown":
        raise OrchestrationError(f"Action {action!r} is not declared for adapter {adapter_id}")
    ordinal = len(task["actions"]) + 1
    action_id = _action_id(task_id, adapter_id, action, ordinal)
    approval_required = side_effect == "state-changing" or bool(adapter.get("always_require_approval"))
    entry = {"action_id": action_id, "adapter": adapter_id, "action": action, "payload": agent_reliability.sanitize(payload), "side_effect": side_effect, "approval_required": approval_required, "approval_status": "pending" if approval_required else "not-required", "status": "waiting-approval" if approval_required else "ready", "created_at": _now(), "dispatched_at": None, "completed_at": None, "result": None, "evidence": []}
    task["actions"].append(entry)
    task["status"] = "waiting-approval" if approval_required else "ready-to-dispatch"
    task["stage"] = "execution-queue"
    agent_reliability.add_event(task["trace"], stage="execution-queue", action=f"request:{adapter_id}:{action}", status="success", evidence=[action_id])
    save_task(task, state_dir)
    return entry


def approve_action(task_id: str, action_id: str, approved_by: str, *, note: str = "", state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    target = next((a for a in task["actions"] if a["action_id"] == action_id), None)
    if not target:
        raise OrchestrationError("Action not found")
    if target["status"] not in {"waiting-approval", "ready"}:
        raise OrchestrationError(f"Action cannot be approved from status {target['status']}")
    record = {"action_id": action_id, "approved_by": approved_by, "note": note, "approved_at": _now()}
    task["approvals"].append(record)
    target["approval_status"] = "approved"
    target["status"] = "ready"
    task["status"] = "ready-to-dispatch"
    agent_reliability.add_event(task["trace"], stage="approval", action=f"approve:{action_id}", status="success", evidence=["human-approval-recorded"], approval=approved_by)
    save_task(task, state_dir)
    return record


def dispatch_manifest(task_id: str, *, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    ready = []
    for action in task["actions"]:
        if action["status"] != "ready":
            continue
        if action["approval_required"] and action["approval_status"] != "approved":
            continue
        adapter = _adapter(action["adapter"])
        ready.append({"task_id": task_id, "action_id": action["action_id"], "adapter": action["adapter"], "action": action["action"], "payload": action["payload"], "side_effect": action["side_effect"], "host_contract": adapter.get("host_contract"), "credential_boundary": adapter.get("credential_boundary")})
    return {"task_id": task_id, "requests": ready, "execution": "host-must-invoke-adapter", "warning": "Generating this manifest does not authorize any action beyond approvals already recorded in the task."}


def mark_dispatched(task_id: str, action_id: str, *, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    target = next((a for a in task["actions"] if a["action_id"] == action_id), None)
    if not target or target["status"] != "ready":
        raise OrchestrationError("Only ready actions may be marked dispatched")
    if target["approval_required"] and target["approval_status"] != "approved":
        raise OrchestrationError("Required approval missing")
    target["status"] = "dispatched"
    target["dispatched_at"] = _now()
    task["status"] = "in-progress"
    task["stage"] = "execution"
    agent_reliability.add_event(task["trace"], stage="execution", action=f"dispatch:{action_id}", status="success", evidence=["host-dispatch-recorded"])
    save_task(task, state_dir)
    return target


def record_result(task_id: str, action_id: str, *, success: bool, evidence: list[str], result: dict[str, Any] | None = None, cost: float = 0.0, latency_ms: int = 0, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    target = next((a for a in task["actions"] if a["action_id"] == action_id), None)
    if not target:
        raise OrchestrationError("Action not found")
    if target["status"] not in {"dispatched", "ready"}:
        raise OrchestrationError(f"Cannot record result from status {target['status']}")
    if target["approval_required"] and target["approval_status"] != "approved":
        raise OrchestrationError("Required approval missing")
    if not evidence:
        raise OrchestrationError("Observable evidence is required")
    target["status"] = "succeeded" if success else "failed"
    target["completed_at"] = _now()
    target["evidence"] = list(evidence)
    target["result"] = agent_reliability.sanitize(result or {})
    task["evidence"].extend(evidence)
    task["metrics"]["cost"] = round(float(task["metrics"].get("cost", 0)) + float(cost), 8)
    task["metrics"]["latency_ms"] = int(task["metrics"].get("latency_ms", 0)) + int(latency_ms)
    if not success:
        task["metrics"]["tool_failures"] = int(task["metrics"].get("tool_failures", 0)) + 1
        task["status"] = "failed"
    else:
        unfinished = [a for a in task["actions"] if a["status"] not in {"succeeded", "failed"}]
        task["status"] = "in-progress" if unfinished else "ready-to-verify"
    agent_reliability.add_event(task["trace"], stage="execution", action=f"result:{action_id}", status="success" if success else "failed", evidence=evidence, cost=cost, latency_ms=latency_ms)
    save_task(task, state_dir)
    return target


def record_criterion(task_id: str, criterion: str, *, passed: bool, evidence: list[str], state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    if passed and not evidence:
        raise OrchestrationError("Passing criteria require evidence")
    task = load_task(task_id, state_dir)
    task["criteria"][criterion] = {"passed": bool(passed), "evidence": list(evidence)}
    task["evidence"].extend(evidence)
    save_task(task, state_dir)
    return task["criteria"][criterion]


def recovery_proposal(task_id: str, action_id: str, *, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    failed = next((a for a in task["actions"] if a["action_id"] == action_id), None)
    if not failed or failed["status"] != "failed":
        raise OrchestrationError("Recovery requires a failed action")
    max_retries = int(policy().get("recovery", {}).get("max_retries_per_action", 2))
    attempts = task["recovery"]["attempts"]
    current = int(attempts.get(action_id, 0))
    if current >= max_retries:
        raise OrchestrationError("Recovery retry budget exhausted")
    attempts[action_id] = current + 1
    fresh_approval = failed["side_effect"] == "state-changing"
    proposal = {"proposal_id": hashlib.sha256(f"{action_id}|{current + 1}|{_now()}".encode()).hexdigest()[:16], "retry_of": action_id, "attempt": current + 1, "max_attempts": max_retries, "adapter": failed["adapter"], "action": failed["action"], "payload": failed["payload"], "requires_fresh_approval": fresh_approval, "auto_retry_eligible": failed["side_effect"] == "read-only" and bool(policy().get("recovery", {}).get("allow_read_only_auto_retry", True)), "diagnostic": "Review failure evidence/result, apply the smallest reversible correction, then re-run verification.", "created_at": _now()}
    task["recovery"]["proposals"].append(proposal)
    task["status"] = "recovery-proposed"
    agent_reliability.add_event(task["trace"], stage="recovery", action=f"propose-retry:{action_id}", status="success", evidence=[proposal["proposal_id"]])
    save_task(task, state_dir)
    return proposal


def materialize_recovery(task_id: str, proposal_id: str, *, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    proposal = next((p for p in task["recovery"]["proposals"] if p["proposal_id"] == proposal_id), None)
    if not proposal:
        raise OrchestrationError("Recovery proposal not found")
    new_action = request_action(task_id, proposal["adapter"], proposal["action"], proposal["payload"], state_dir=state_dir)
    task = load_task(task_id, state_dir)
    new_target = next(a for a in task["actions"] if a["action_id"] == new_action["action_id"])
    new_target["retry_of"] = proposal["retry_of"]
    new_target["recovery_proposal_id"] = proposal_id
    if proposal["requires_fresh_approval"]:
        new_target["approval_status"] = "pending"
        new_target["status"] = "waiting-approval"
    save_task(task, state_dir)
    return new_target


def _generic_verification(task: dict[str, Any]) -> dict[str, Any]:
    failed = [a for a in task["actions"] if a["status"] == "failed"]
    pending = [a for a in task["actions"] if a["status"] in {"waiting-approval", "ready", "dispatched"}]
    missing_approval = [a["action_id"] for a in task["actions"] if a["approval_required"] and a["approval_status"] != "approved"]
    if failed or pending or missing_approval:
        status = "FAIL"
    elif task["plan_only"]:
        status = "PASS" if task.get("brain_plan") and task.get("knowledge_plan") else "FAIL"
    elif not task["actions"]:
        status = "FAIL"
    elif not task.get("evidence"):
        status = "FAIL"
    else:
        status = "HUMAN_REVIEW" if task["risk_tier"] == "A" else "PASS"
    return {"scenario_id": None, "status": status, "score": 100.0 if status in {"PASS", "HUMAN_REVIEW"} else 0.0, "hard_failures": ["failed-action"] if failed else [], "missing_criteria": [], "pending_actions": [a["action_id"] for a in pending], "missing_approvals": missing_approval, "evidence_count": len(task.get("evidence", [])), "verifier_note": "Generic orchestration gate uses persisted observable task state; agent self-report is ignored."}


def verify_task(task_id: str, *, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    task["status"] = "verifying"
    save_task(task, state_dir)
    if task.get("scenario_id"):
        sc = agent_reliability.scenario(task["scenario_id"])
        run = {"criteria": task.get("criteria", {}), "evidence": task.get("evidence", []), "metrics": task.get("metrics", {}), "agent_status": task.get("status"), "required_approval_missing": any(a["approval_required"] and a["approval_status"] != "approved" for a in task["actions"]), "unauthorized_state_change": any(a["side_effect"] == "state-changing" and a["status"] in {"dispatched", "succeeded"} and a["approval_status"] != "approved" for a in task["actions"])}
        verification = agent_reliability.verify_completion(sc, run)
    else:
        verification = _generic_verification(task)
    task = load_task(task_id, state_dir)
    task["verification"] = verification
    task["trace"]["final_state"] = verification["status"].casefold()
    task["stage"] = "verification"
    task["checkpoint"] = "verification-complete"
    if verification["status"] == "PASS":
        task["status"] = "complete"
    elif verification["status"] == "HUMAN_REVIEW":
        task["status"] = "human-review"
    else:
        task["status"] = "failed"
        if task.get("scenario_id"):
            regression_run = {"criteria": task.get("criteria", {}), "evidence": task.get("evidence", []), "metrics": task.get("metrics", {}), "agent_status": "failed"}
            task["regression_case"] = agent_reliability.failure_to_regression(task["scenario_id"], regression_run, verification)
    agent_reliability.add_event(task["trace"], stage="verification", action="independent-completion-gate", status="success" if verification["status"] in {"PASS", "HUMAN_REVIEW"} else "failed", evidence=[verification["status"]])
    save_task(task, state_dir)
    return verification


def release_approve(task_id: str, approved_by: str, *, note: str = "", state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    if not task.get("verification") or task["verification"].get("status") != "HUMAN_REVIEW":
        raise OrchestrationError("Release approval is only valid after a HUMAN_REVIEW verifier result")
    record = {"approved_by": approved_by, "note": note, "approved_at": _now(), "verification_status": "HUMAN_REVIEW"}
    task["release_approval"] = record
    task["status"] = "complete"
    task["stage"] = "released"
    task["checkpoint"] = "released"
    task["trace"]["final_state"] = "complete"
    agent_reliability.add_event(task["trace"], stage="release", action="human-release-approval", status="success", evidence=["release-approved"], approval=approved_by)
    save_task(task, state_dir)
    return record


def next_step(task_id: str, *, state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    task = load_task(task_id, state_dir)
    waiting = [a for a in task["actions"] if a["status"] == "waiting-approval"]
    ready = [a for a in task["actions"] if a["status"] == "ready"]
    failed = [a for a in task["actions"] if a["status"] == "failed"]
    if task["status"] == "complete": recommendation = "done"
    elif waiting: recommendation = "obtain-action-approval"
    elif ready: recommendation = "dispatch-ready-actions-through-host-adapters"
    elif failed: recommendation = "create-bounded-recovery-proposal"
    elif task["status"] == "human-review": recommendation = "obtain-human-release-approval"
    elif task["plan_only"]: recommendation = "run-independent-verification"
    elif not task["actions"]: recommendation = "request-first-execution-action"
    else: recommendation = "run-independent-verification"
    return {"task_id": task_id, "status": task["status"], "checkpoint": task["checkpoint"], "recommendation": recommendation, "waiting_approvals": [a["action_id"] for a in waiting], "ready_actions": [a["action_id"] for a in ready], "failed_actions": [a["action_id"] for a in failed]}


def control_plane(state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    tasks = list_tasks(state_dir)
    summaries = []
    for task in tasks:
        summaries.append({"task_id": task["task_id"], "goal": task["goal"], "status": task["status"], "risk_tier": task["risk_tier"], "checkpoint": task["checkpoint"], "actions": len(task["actions"]), "approvals_waiting": len([a for a in task["actions"] if a["status"] == "waiting-approval"]), "failures": len([a for a in task["actions"] if a["status"] == "failed"]), "cost": task.get("metrics", {}).get("cost", 0.0), "latency_ms": task.get("metrics", {}).get("latency_ms", 0), "verification": (task.get("verification") or {}).get("status"), "updated_at": task.get("updated_at")})
    counts: dict[str, int] = {}
    for item in summaries:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    return {"schema_version": SCHEMA_VERSION, "task_count": len(summaries), "status_counts": counts, "tasks": sorted(summaries, key=lambda x: x.get("updated_at") or "", reverse=True), "privacy": "Task state is local by default and sanitized before persistence; credentials are never stored."}


def _json_arg(value: str | None) -> dict[str, Any]:
    if not value: return {}
    data = json.loads(value)
    if not isinstance(data, dict): raise OrchestrationError("JSON argument must be an object")
    return data


def _print(value: Any) -> None:
    print(json.dumps(value, indent=2, sort_keys=True))


def main() -> None:
    p = argparse.ArgumentParser(description="Internet-Well Execution Orchestration v0.6")
    p.add_argument("--state-dir", default=str(DEFAULT_STATE_DIR))
    sub = p.add_subparsers(dest="cmd", required=True)
    start = sub.add_parser("start"); start.add_argument("goal"); start.add_argument("--risk-tier", choices=["A", "B"]); start.add_argument("--scenario"); start.add_argument("--plan-only", action="store_true")
    sub.add_parser("list")
    status = sub.add_parser("status"); status.add_argument("task_id")
    nxt = sub.add_parser("next"); nxt.add_argument("task_id")
    req = sub.add_parser("request-action"); req.add_argument("task_id"); req.add_argument("adapter"); req.add_argument("action"); req.add_argument("--payload")
    approve = sub.add_parser("approve"); approve.add_argument("task_id"); approve.add_argument("action_id"); approve.add_argument("--by", required=True); approve.add_argument("--note", default="")
    manifest = sub.add_parser("dispatch-manifest"); manifest.add_argument("task_id")
    dispatched = sub.add_parser("mark-dispatched"); dispatched.add_argument("task_id"); dispatched.add_argument("action_id")
    result = sub.add_parser("record-result"); result.add_argument("task_id"); result.add_argument("action_id"); result.add_argument("--success", action="store_true"); result.add_argument("--evidence", action="append", required=True); result.add_argument("--result"); result.add_argument("--cost", type=float, default=0.0); result.add_argument("--latency-ms", type=int, default=0)
    criterion = sub.add_parser("criterion"); criterion.add_argument("task_id"); criterion.add_argument("name"); criterion.add_argument("--passed", action="store_true"); criterion.add_argument("--evidence", action="append", default=[])
    recover = sub.add_parser("recover"); recover.add_argument("task_id"); recover.add_argument("action_id")
    materialize = sub.add_parser("materialize-recovery"); materialize.add_argument("task_id"); materialize.add_argument("proposal_id")
    verify = sub.add_parser("verify"); verify.add_argument("task_id")
    release = sub.add_parser("release-approve"); release.add_argument("task_id"); release.add_argument("--by", required=True); release.add_argument("--note", default="")
    sub.add_parser("adapters")
    sub.add_parser("control-plane")
    args = p.parse_args(); state_dir = Path(args.state_dir)
    if args.cmd == "start": _print(start_task(args.goal, state_dir=state_dir, risk_tier=args.risk_tier, scenario_id=args.scenario, plan_only=args.plan_only))
    elif args.cmd == "list": _print(control_plane(state_dir))
    elif args.cmd == "status": _print(load_task(args.task_id, state_dir))
    elif args.cmd == "next": _print(next_step(args.task_id, state_dir=state_dir))
    elif args.cmd == "request-action": _print(request_action(args.task_id, args.adapter, args.action, _json_arg(args.payload), state_dir=state_dir))
    elif args.cmd == "approve": _print(approve_action(args.task_id, args.action_id, args.by, note=args.note, state_dir=state_dir))
    elif args.cmd == "dispatch-manifest": _print(dispatch_manifest(args.task_id, state_dir=state_dir))
    elif args.cmd == "mark-dispatched": _print(mark_dispatched(args.task_id, args.action_id, state_dir=state_dir))
    elif args.cmd == "record-result": _print(record_result(args.task_id, args.action_id, success=args.success, evidence=args.evidence, result=_json_arg(args.result), cost=args.cost, latency_ms=args.latency_ms, state_dir=state_dir))
    elif args.cmd == "criterion": _print(record_criterion(args.task_id, args.name, passed=args.passed, evidence=args.evidence, state_dir=state_dir))
    elif args.cmd == "recover": _print(recovery_proposal(args.task_id, args.action_id, state_dir=state_dir))
    elif args.cmd == "materialize-recovery": _print(materialize_recovery(args.task_id, args.proposal_id, state_dir=state_dir))
    elif args.cmd == "verify": _print(verify_task(args.task_id, state_dir=state_dir))
    elif args.cmd == "release-approve": _print(release_approve(args.task_id, args.by, note=args.note, state_dir=state_dir))
    elif args.cmd == "adapters": _print(adapter_registry())
    elif args.cmd == "control-plane": _print(control_plane(state_dir))


if __name__ == "__main__":
    main()
