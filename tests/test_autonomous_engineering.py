import tempfile
import unittest
from pathlib import Path

from automation import autonomous_engineering as ae


class AutonomousEngineeringTests(unittest.TestCase):
    def test_minimum_team_has_independent_verifier(self):
        roles = [r.id for r in ae.select_roles("Fix this repository")]
        self.assertIn("chief-of-staff", roles)
        self.assertIn("engineer", roles)
        self.assertIn("qa", roles)
        self.assertIn("verifier", roles)
        self.assertIn("engineer", ae.ROLE_BY_ID["verifier"].independent_from)

    def test_production_ui_goal_adds_cross_functional_roles(self):
        roles = [r.id for r in ae.select_roles("Launch the production UI with auth and privacy review")]
        for required in ("product", "ux", "security", "compliance", "release"):
            self.assertIn(required, roles)

    def test_verifier_depends_on_review_evidence(self):
        graph = ae.build_task_graph("Launch a secure production web app")
        verifier = next(n for n in graph["nodes"] if n["role"] == "verifier")
        review_roles = {n["role"] for n in graph["nodes"] if n["id"] in verifier["depends_on"]}
        self.assertTrue({"qa", "security", "release"} <= review_roles)

    def test_model_routes_have_fallbacks(self):
        policy = ae.model_routing_policy("Implement and test a repository change")
        self.assertGreaterEqual(len(policy["routes"]["engineer"]), 3)
        self.assertEqual(policy["routes"]["engineer"][0]["provider"], "codex")

    def test_team_wraps_governed_orchestrator(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = ae.build_team(
                "Prepare a production UI release",
                state_dir=Path(tmp),
                plan_only=True,
            )
            self.assertEqual(len(result["task_id"]), 20)
            self.assertEqual(result["risk_tier"], "A")
            self.assertTrue(result["governance"]["independent_verification"])
            self.assertEqual(result["governance"]["state_changes"], "explicit approval through execution_orchestrator")


if __name__ == "__main__":
    unittest.main()
