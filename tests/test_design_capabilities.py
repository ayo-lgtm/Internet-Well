import json
import unittest
from pathlib import Path

from automation import agent_brain, execution_orchestrator


ROOT = Path(__file__).resolve().parents[1]


class DesignCapabilityTests(unittest.TestCase):
    def test_brand_design_system_routes_to_complete_bundle(self):
        goals = (
            "build a brand identity with logo app icons typography colors and design tokens",
            "create a logo and brand guidelines",
            "replace the placeholder favicon and PWA icons",
            "set up typography colors and design tokens",
            "document our component design system",
        )
        for goal in goals:
            with self.subTest(goal=goal):
                self.assertEqual(
                    agent_brain.recommend_stack(goal)["bundle"],
                    "brand-design-system",
                )

        result = agent_brain.recommend_stack(goals[0])
        ids = {item["id"] for item in result["preferred_resources"]}
        self.assertTrue(
            {
                "brand-yml",
                "design-tokens-format",
                "style-dictionary",
                "lucide",
                "fontsource",
                "color-js",
                "svgo",
                "storybook",
            }
            <= ids
        )

    def test_design_adapter_exposes_brand_resources(self):
        adapters = execution_orchestrator.adapter_registry()["adapters"]
        design = next(item for item in adapters if item["id"] == "design")
        self.assertTrue(
            {
                "brand-yml",
                "design-tokens-format",
                "style-dictionary",
                "lucide",
                "fontsource",
                "color-js",
                "svgo",
                "storybook",
            }
            <= set(design["resources"])
        )

    def test_registry_and_brand_contract_cover_each_design_layer(self):
        expected = {
            "brand-yml.md",
            "color-js.md",
            "design-tokens-format.md",
            "fontsource.md",
            "lucide.md",
            "storybook.md",
            "style-dictionary.md",
            "svgo.md",
        }
        self.assertTrue(
            expected
            <= {path.name for path in (ROOT / "registry" / "design").glob("*.md")}
        )

        contract = (ROOT / "docs" / "BRAND-SYSTEM.md").read_text(encoding="utf-8")
        for heading in (
            "## Brand foundation",
            "## Logo and mark system",
            "## App icons and favicons",
            "## Color system",
            "## Typography system",
            "## Interface iconography",
            "## Design tokens",
            "## Component documentation",
            "## Acceptance gates",
        ):
            self.assertIn(heading, contract)

    def test_token_template_is_dtcg_shaped_and_semantic(self):
        tokens = json.loads(
            (ROOT / "templates" / "brand-system" / "tokens.tokens.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(tokens["color"]["$type"], "color")
        self.assertIn("$value", tokens["color"]["brand"]["primary"])
        self.assertEqual(
            tokens["color"]["text"]["primary"]["$value"],
            "{color.neutral.900}",
        )
        self.assertEqual(tokens["typography"]["$type"], "typography")


if __name__ == "__main__":
    unittest.main()
