import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "automation"))

from founder_os_engine import detect_project, select_resources, load_catalog


class FounderOSEngineTests(unittest.TestCase):
    def test_catalog_is_large_and_unique(self):
        repos = load_catalog()
        self.assertGreaterEqual(len(repos), 60)
        slugs = [repo["slug"].lower() for repo in repos]
        self.assertEqual(len(slugs), len(set(slugs)))
        for repo in repos:
            self.assertTrue(repo["capabilities"])
            self.assertIn(repo["role"], {
                "production-tool", "platform", "framework", "reference-implementation",
                "agent-runtime", "research-tool", "first-party-fixture"
            })

    def test_detects_lexura_like_project_without_restoring_removed_features(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "package.json").write_text(json.dumps({
                "dependencies": {
                    "next": "latest", "react": "latest", "@supabase/supabase-js": "latest",
                    "openai": "latest"
                }
            }), encoding="utf-8")
            (root / "README.md").write_text(
                "Multilingual legal intake that helps people understand legal issues and prepares an attorney package."
                " Universal mode only. No case marketplace. No guaranteed outcomes. No paid priority review.",
                encoding="utf-8"
            )
            assessment = detect_project(root)
            products = {item["name"] for item in assessment["product_types"]}
            self.assertIn("ai-saas", products)
            self.assertIn("legal-tech", products)
            self.assertEqual("high", assessment["risk_class"])
            self.assertIn("legal-review", assessment["required_capabilities"])
            serialized = json.dumps(assessment).lower()
            self.assertNotIn("restore marketplace", serialized)
            self.assertNotIn("guaranteed win", serialized)

    def test_selects_validated_tools_before_candidate_duplicates(self):
        assessment = {
            "risk_class": "moderate",
            "required_capabilities": ["browser-testing", "secret-detection", "dependency-scanning"]
        }
        result = select_resources(assessment, "launch security", [], 8)
        names = {item["name"] for item in result["selected_resources"]}
        self.assertIn("Playwright", names)
        self.assertTrue(names.intersection({"Gitleaks", "Trivy", "OSV-Scanner"}))
        self.assertTrue(all("evidence_status" in item for item in result["selected_resources"]))

    def test_trading_goal_preserves_human_review_and_no_authorization(self):
        assessment = {"risk_class": "high", "required_capabilities": []}
        result = select_resources(assessment, "trading system research and paper trading", [], 10)
        selected = result["selected_resources"]
        self.assertTrue(any(item["name"] in {"LEAN", "Freqtrade", "NautilusTrader"} for item in selected))
        self.assertTrue(all(item["requires_human_review"] for item in selected))
        self.assertTrue(any("does not authorize" in warning.lower() for warning in result["warnings"]))


if __name__ == "__main__":
    unittest.main()
