import json
import subprocess
import sys
import unittest
from unittest.mock import patch

from automation import agent_brain, upstream_verifier


class AgentBrainTests(unittest.TestCase):
    def test_catalog_additions_are_discoverable_without_approval(self):
        for name, slug in [("FreeHire", "strelov1/freehire"),
                           ("Plannotator", "backnotprop/plannotator"),
                           ("VoiceStudio", "debpalash/VoiceStudio")]:
            with self.subTest(name=name):
                results = agent_brain.find_capability(name)["results"]
                candidate = next((r for r in results if r.get("slug") == slug), None)
                self.assertIsNotNone(candidate)
                self.assertEqual(candidate["evidence_status"], "research-candidate-unverified")
                self.assertEqual(candidate["evidence_score"], 0)
                self.assertFalse(candidate["execution_authorized"])
                self.assertTrue(candidate["license"])
                self.assertIn("verify-license-and-security", candidate["restrictions"])

    def test_recommendations_expose_candidates_separately_from_bundle(self):
        result = agent_brain.recommend_stack("build a production web app with Plannotator")
        self.assertIn("backnotprop/plannotator", {r["slug"] for r in result["candidate_resources"]})
        self.assertNotIn("catalog:backnotprop/plannotator", {r["id"] for r in result["preferred_resources"]})

    def test_candidate_search_retains_risks_and_limits(self):
        result = agent_brain.find_capability("VoiceStudio", limit=1)["results"]
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["risk"], "medium-data")
        self.assertEqual(result[0]["recommendation"], "voice-tool-personal-use")
        self.assertEqual(agent_brain.find_capability("zzzz-no-such-resource-987")["results"], [])

    def test_catalog_cannot_bypass_restricted_graph_resource(self):
        restricted = {"nodes": [{"id": "restricted-voice", "kind": "restricted-reference",
                                 "source": "https://github.com/debpalash/VoiceStudio"}]}
        with patch.object(agent_brain, "graph", return_value=restricted):
            self.assertEqual(agent_brain.find_capability("VoiceStudio")["results"], [])

    def test_graph_loads_and_scores(self):
        g = agent_brain.graph()
        self.assertGreaterEqual(len(g["nodes"]), 10)
        self.assertTrue(all(agent_brain.evidence_score(n) > 0 for n in g["nodes"]))

    def test_autonomous_agent_routes(self):
        result = agent_brain.recommend_stack("build a persistent autonomous agent that keeps working until done")
        self.assertEqual(result["bundle"], "autonomous-agent")
        ids = {x["id"] for x in result["preferred_resources"]}
        self.assertIn("autonomous-loop", ids)
        self.assertIn("event-driven-autonomous-loop", ids)

    def test_product_launch_routes(self):
        result = agent_brain.recommend_stack("launch my startup with a launch video")
        self.assertEqual(result["bundle"], "product-launch-campaign")
        ids = {x["id"] for x in result["preferred_resources"]}
        self.assertEqual(ids, {"places-to-post-your-startup", "openmontage"})
        self.assertIn("external", result["restriction"].lower())

    def test_trading_bundle_is_research_bounded(self):
        result = agent_brain.recommend_stack("autonomous trading research agent")
        self.assertEqual(result["bundle"], "autonomous-trading-research")
        self.assertIn("paper", result["restriction"].lower())

    def test_restricted_reference_excluded(self):
        results = agent_brain.find_capability("adversarial evaluation reference")["results"]
        self.assertNotIn("qwen38-uncensored", {x["id"] for x in results})

    def test_all_bundles_evaluate(self):
        result = agent_brain.evaluate_all()
        self.assertTrue(result["passed"], json.dumps(result, indent=2))

    def test_mcp_tools_exist(self):
        names = {x["name"] for x in agent_brain.mcp_tools()}
        self.assertEqual(names, {"find_capability", "recommend_stack", "find_api", "get_skill", "plan_implementation", "evaluate_bundle"})

    def test_mcp_stdio_round_trip(self):
        request = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}) + "\n"
        proc = subprocess.run([sys.executable, "-m", "automation.agent_brain", "serve"], input=request, text=True, capture_output=True, timeout=10)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout.strip())
        self.assertEqual(payload["id"], 1)
        self.assertGreaterEqual(len(payload["result"]["tools"]), 6)

    def test_upstream_verifier_is_non_mutating_by_default(self):
        result = upstream_verifier.verify(network=False)
        self.assertFalse(result["network_checked"])
        self.assertIn("never silently updates", result["policy"].lower())
        self.assertGreaterEqual(len(result["resources"]), 10)
        self.assertTrue(all("checks" in row for row in result["resources"]))
        self.assertFalse(any(row.get("upgrade_candidate", {}).get("automatic_update") for row in result["resources"]))


if __name__ == "__main__":
    unittest.main()
