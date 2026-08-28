from automation import execution_orchestrator as eo


def test_new_task_is_plan_only_and_checkpointed():
    task = eo.new_task("build and verify a production web app")
    assert task["status"] == "planned"
    assert task["authorization"]["execution_authorized"] is False
    assert task["checkpoint_hash"]
    assert task["brain_plan"]


def test_state_changing_execution_blocked_without_authorization():
    task = eo.new_task("update a repository")
    task = eo.select_adapters(task, ["github"])
    task = eo.execute(task, {"github": lambda *_: {"status": "success", "evidence": ["commit"]}})
    assert task["status"] == "blocked"
    assert "missing_execution_authority" in eo.execution_preflight(task)["blockers"]


def test_authorized_execution_verifies_and_completes():
    task = eo.new_task("update a repository", success_criteria=["change_verified"])
    task = eo.select_adapters(task, ["github"])
    task = eo.authorize(task, scopes=["repository:ayo/repo:branch:feature"])
    task = eo.execute(task, {"github": lambda *_: {"status": "success", "evidence": ["ci-green", "diff-reviewed"]}})
    task = eo.verify(task)
    assert task["verification"]["status"] == "PASS"
    task = eo.complete(task)
    assert task["status"] == "completed"


def test_tier_a_requires_recorded_human_approval():
    task = eo.new_task("production deploy", risk_tier="A")
    task = eo.select_adapters(task, ["vercel"])
    try:
        eo.authorize(task, scopes=["production-deploy"])
        assert False, "expected approval requirement"
    except eo.OrchestrationError:
        pass
    task = eo.authorize(task, scopes=["production-deploy"], approval="release-owner-approved")
    assert task["authorization"]["execution_authorized"] is True


def test_checkpoint_integrity_roundtrip(tmp_path):
    path = tmp_path / "task.json"
    task = eo.new_task("resume me")
    eo.save_task(task, path)
    loaded = eo.load_task(path)
    assert loaded["task_id"] == task["task_id"]


def test_control_plane_exposes_operational_state():
    task = eo.new_task("inspect ui and verify design")
    task = eo.select_adapters(task, ["design", "browser"])
    cp = eo.control_plane(task)
    assert cp["stage"] == "select"
    assert cp["adapters"] == ["design", "browser"]
    assert "trace" in cp
