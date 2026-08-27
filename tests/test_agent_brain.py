import json
import subprocess
import sys
import unittest

from automation import agent_brain


class AgentBrainTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
