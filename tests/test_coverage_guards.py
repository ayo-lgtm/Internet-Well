import tempfile
import unittest
from collections import Counter
from pathlib import Path

from automation.verify_founder_os import REQUIRED_SURFACES, validate_surface_coverage
from automation.verify_registry import CATEGORIES, validate_category_coverage


class CoverageGuardTests(unittest.TestCase):
    def test_current_registry_has_every_governed_category(self):
        root = Path(__file__).resolve().parents[1] / "registry"
        counts = Counter(path.parent.name for path in root.glob("*/*.md"))
        errors = []
        validate_category_coverage(counts, errors)
        self.assertEqual(errors, [])
        self.assertTrue(CATEGORIES <= set(counts))

    def test_registry_guard_rejects_an_empty_category(self):
        counts = Counter({category: 1 for category in CATEGORIES})
        counts["finance"] = 0
        errors = []
        validate_category_coverage(counts, errors)
        self.assertEqual(len(errors), 1)
        self.assertIn("finance", errors[0])
        self.assertIn("empty", errors[0])

    def test_current_founder_os_surfaces_are_non_empty(self):
        errors = []
        validate_surface_coverage(errors)
        self.assertEqual(errors, [])

    def test_surface_guard_rejects_empty_operating_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            errors = []
            validate_surface_coverage(errors, Path(tmp))
        self.assertEqual(len(errors), len(REQUIRED_SURFACES))
        self.assertTrue(all("empty" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
