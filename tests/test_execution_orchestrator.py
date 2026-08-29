import tempfile
import unittest
from pathlib import Path

from automation import execution_orchestrator as eo


class ExecutionOrchestratorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.state_dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_start_persists_and_routes_design_resources(self):
        task = eo.start_task(
            "Create a UI/UX design and design-system handoff for a web app",
            state_dir=self.state_dir,
            plan_only=True,
        )
        loaded = eo.load_task(task["task_id"], self.state_dir)
        self.assertEqual(loaded["checkpoint"], "planning-complete")
        self.assertEqual(loaded["scenario_id"], "agentic-design-handoff")
        self.assertIn("design", [a["id"] for a in loaded["selected_adapters"]])
        sources = [item["source"] for item in loaded["knowledge_plan"]["sources"]]
        self.assertIn("open-design", sources)

    def test_state_change_never_dispatches_without_approval(self):
        task = eo.start_task("Update code in a GitHub repository", state_dir=self.state_dir)
        action = eo.request_action(task["task_id"], "github", "write-file", {"path": "README.md"}, state_dir=self.state_dir)
        self.assertEqual(action["status"], "waiting-approval")
        self.assertEqual(eo.dispatch_manifest(task["task_id"], state_dir=self.state_dir)["requests"], [])
        eo.approve_action(task["task_id"], action["action_id"], "release-owner", state_dir=self.state_dir)
        manifest = eo.dispatch_manifest(task["task_id"], state_dir=self.state_dir)
        self.assertEqual(len(manifest["requests"]), 1)
        self.assertEqual(manifest["requests"][0]["action_id"], action["action_id"])

    def test_secret_material_is_rejected_from_persisted_payload(self):
        task = eo.start_task("Inspect repository", state_dir=self.state_dir)
        with self.assertRaises(eo.OrchestrationError):
            eo.request_action(task["task_id"], "github", "read-file", {"api_key": "should-never-persist"}, state_dir=self.state_dir)

    def test_read_only_action_records_evidence_and_resumes(self):
        task = eo.start_task("Run browser UI tests", state_dir=self.state_dir)
        action = eo.request_action(task["task_id"], "browser", "run-ui-test", {"url": "https://example.invalid"}, state_dir=self.state_dir)
        self.assertEqual(action["status"], "ready")
        eo.mark_dispatched(task["task_id"], action["action_id"], state_dir=self.state_dir)
        eo.record_result(task["task_id"], action["action_id"], success=True, evidence=["ui-suite-pass"], state_dir=self.state_dir)
        resumed = eo.load_task(task["task_id"], self.state_dir)
        self.assertIn("ui-suite-pass", resumed["evidence"])
        self.assertEqual(resumed["actions"][0]["status"], "succeeded")

    def test_recovery_is_bounded_and_state_changes_need_fresh_approval(self):
        task = eo.start_task("Update a GitHub repository", state_dir=self.state_dir)
        action = eo.request_action(task["task_id"], "github", "write-file", {"path": "README.md"}, state_dir=self.state_dir)
        eo.approve_action(task["task_id"], action["action_id"], "owner", state_dir=self.state_dir)
        eo.record_result(task["task_id"], action["action_id"], success=False, evidence=["ci-failed"], state_dir=self.state_dir)
        proposal = eo.recovery_proposal(task["task_id"], action["action_id"], state_dir=self.state_dir)
        self.assertTrue(proposal["requires_fresh_approval"])
        retry = eo.materialize_recovery(task["task_id"], proposal["proposal_id"], state_dir=self.state_dir)
        self.assertEqual(retry["status"], "waiting-approval")
        self.assertEqual(retry["approval_status"], "pending")
        eo.recovery_proposal(task["task_id"], action["action_id"], state_dir=self.state_dir)
        with self.assertRaises(eo.OrchestrationError):
            eo.recovery_proposal(task["task_id"], action["action_id"], state_dir=self.state_dir)

    def test_plan_only_generic_task_can_be_independently_verified(self):
        task = eo.start_task("Research a reversible architecture option", state_dir=self.state_dir, plan_only=True, scenario_id=None)
        self.assertIsNone(task["scenario_id"])
        result = eo.verify_task(task["task_id"], state_dir=self.state_dir)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(eo.load_task(task["task_id"], self.state_dir)["status"], "complete")

    def test_tier_a_requires_human_release_after_verifier(self):
        task = eo.start_task(
            "Implement and prepare a production code change",
            state_dir=self.state_dir,
            risk_tier="A",
            scenario_id="production-code-change",
        )
        action = eo.request_action(task["task_id"], "github", "write-file", {"path": "app.py"}, state_dir=self.state_dir)
        eo.approve_action(task["task_id"], action["action_id"], "owner", state_dir=self.state_dir)
        eo.record_result(task["task_id"], action["action_id"], success=True, evidence=["commit-created", "ci-green"], state_dir=self.state_dir)
        criteria = [
            "tests-pass",
            "security-checks-pass",
            "acceptance-criteria-proven",
            "rollback-defined",
            "state-changing-actions-approved",
            "independent-verifier-pass",
        ]
        for criterion in criteria:
            eo.record_criterion(task["task_id"], criterion, passed=True, evidence=[f"evidence:{criterion}"], state_dir=self.state_dir)
        result = eo.verify_task(task["task_id"], state_dir=self.state_dir)
        self.assertEqual(result["status"], "HUMAN_REVIEW")
        eo.release_approve(task["task_id"], "release-owner", state_dir=self.state_dir)
        self.assertEqual(eo.load_task(task["task_id"], self.state_dir)["status"], "complete")

    def test_control_plane_aggregates_tasks(self):
        eo.start_task("Design a dashboard", state_dir=self.state_dir, plan_only=True)
        eo.start_task("Inspect a self-hosted option", state_dir=self.state_dir, plan_only=True)
        control = eo.control_plane(self.state_dir)
        self.assertEqual(control["task_count"], 2)
        self.assertEqual(control["privacy"], "Task state is local by default and sanitized before persistence; credentials are never stored.")


if __name__ == "__main__":
    unittest.main()
