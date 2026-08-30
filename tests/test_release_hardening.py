import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseHardeningTests(unittest.TestCase):
    def test_public_version_is_aligned(self):
        expected = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(expected, "0.5.0")
        self.assertIn(f'version = "{expected}"', (ROOT / "pyproject.toml").read_text())
        self.assertIn(f'VERSION = "{expected}"', (ROOT / "internet_well.py").read_text())
        for path in (
            ROOT / "integrations/agent-brain/capability-graph.json",
            ROOT / "integrations/agent-brain/mcp.json",
            ROOT / "bundles/agent-brain-bundles.json",
        ):
            self.assertEqual(json.loads(path.read_text())["version"], expected)

    def test_split_license_scope_is_explicit(self):
        scope = (ROOT / "LICENSES.md").read_text(encoding="utf-8")
        content_notice = (ROOT / "LICENSE-CONTENT").read_text(encoding="utf-8")
        self.assertIn("Apache License 2.0", scope)
        self.assertIn("CC-BY-4.0", scope)
        self.assertIn("Third-party", scope)
        self.assertIn("SPDX-License-Identifier: CC-BY-4.0", content_notice)
        self.assertIn("creativecommons.org/licenses/by/4.0/legalcode", content_notice)

    def test_required_status_contexts_match_unique_job_ids(self):
        rules = json.loads((ROOT / ".github/rulesets/main-protection.json").read_text())
        required_rule = next(rule for rule in rules["rules"] if rule["type"] == "required_status_checks")
        contexts = {
            item["context"] for item in required_rule["parameters"]["required_status_checks"]
        }
        expected = {
            "registry": ".github/workflows/verify-registry.yml",
            "hygiene": ".github/workflows/verify-public-repo-hygiene.yml",
            "public-launch": ".github/workflows/verify-public-launch.yml",
            "productization": ".github/workflows/verify-productization.yml",
            "evidence-contract": ".github/workflows/verify-identity-authorization.yml",
            "verify-agent-systems": ".github/workflows/verify-agent-systems.yml",
            "api-discovery": ".github/workflows/verify-api-discovery.yml",
            "agent-brain": ".github/workflows/verify-agent-brain.yml",
        }
        self.assertEqual(contexts, set(expected))
        for job_id, relative_path in expected.items():
            workflow = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertRegex(workflow, rf"(?m)^  {re.escape(job_id)}:$")

    def test_history_hygiene_workflow_uses_full_checkout(self):
        workflow = (ROOT / ".github/workflows/verify-public-repo-hygiene.yml").read_text()
        self.assertIn("fetch-depth: 0", workflow)
        self.assertIn("verify_git_history_hygiene.py", workflow)

    def test_agent_brain_ci_derives_current_version(self):
        workflow = (ROOT / ".github/workflows/verify-agent-brain.yml").read_text()
        self.assertIn("Path('VERSION').read_text().strip()", workflow)
        self.assertNotIn("graph()['version']=='0.4.0'", workflow)


if __name__ == "__main__":
    unittest.main()
