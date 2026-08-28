import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProboComplianceTests(unittest.TestCase):
    def run_cli(self, *args: str) -> dict:
        env = os.environ.copy()
        env["INTERNET_WELL_ROOT"] = str(ROOT)
        proc = subprocess.run(
            [sys.executable, "-m", "automation.probo_compliance", *args],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return json.loads(proc.stdout)

    def test_manifest_is_immutably_pinned_and_non_attesting(self):
        data = self.run_cli("show")
        self.assertRegex(data["pin"], r"^[0-9a-f]{40}$")
        self.assertEqual(data["license"], "MIT")
        self.assertEqual(data["supported_use"]["attestation"], "independent-cpa-required")
        self.assertIn("no-self-attestation", data["restrictions"])

    def test_soc2_readiness_defaults_to_security_only(self):
        data = self.run_cli("soc2-readiness")
        self.assertEqual(data["framework"], "SOC 2")
        self.assertEqual(data["report_type"], "Type I")
        self.assertEqual(data["trust_services_criteria"], ["security"])
        self.assertEqual(data["attestation_authority"], "independent-licensed-cpa-firm")
        self.assertIn("do-not-fabricate-evidence", data["evidence_rules"])

    def test_auditor_handoff_never_submits_or_attests(self):
        data = self.run_cli("auditor-handoff", "--company", "Example Co")
        self.assertEqual(data["submission"], "not-performed")
        self.assertEqual(data["attestation"], "not-performed")
        self.assertIn("licensed-cpa-firm", data["auditor_due_diligence"])
        self.assertIn("control-matrix", data["package"])

    def test_evidence_template_excludes_secret_material(self):
        data = self.run_cli("evidence-template")
        self.assertEqual(data["classification"], "confidential-audit-evidence")
        self.assertIn("exclude-secrets-and-private-keys", data["privacy"])
        self.assertIn("source_system", data["required_fields"])


if __name__ == "__main__":
    unittest.main()
