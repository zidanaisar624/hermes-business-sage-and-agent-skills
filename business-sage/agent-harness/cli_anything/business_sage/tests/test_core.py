"""Automated E2E & unit regression tests for `cli-anything-business-sage` (`bsage`)."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

_HARNESS_ROOT = Path(__file__).resolve().parents[3]
if str(_HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(_HARNESS_ROOT))

CLI_PATH = Path(__file__).resolve().parents[1] / "cli_anything_business_sage.py"


def run_cli(*args: str, env_override: dict | None = None) -> dict:
    env = os.environ.copy()
    if env_override:
        env.update(env_override)
    out = subprocess.check_output(
        [sys.executable, str(CLI_PATH), "--json", *args],
        text=True,
        encoding="utf-8",
        env=env,
    )
    return json.loads(out)


class TestBusinessSageCLI(unittest.TestCase):
    def test_unit_economics_and_respectful_role(self) -> None:
        r1 = run_cli(
            "unit-economics",
            "--price", "200000",
            "--variable-cost", "80000",
            "--monthly-fixed-cost", "12000000",
            "--cac", "120000",
        )
        self.assertEqual(r1["status"], "ok")
        self.assertEqual(r1["contribution_margin_per_unit"], 120000.0)
        self.assertEqual(r1["break_even_units_per_month"], 100)
        self.assertIn("NOT a replacement", r1["advisory_role"])

    def test_indonesia_tax_scenarios_pp_20_2026(self) -> None:
        r2 = run_cli(
            "indonesia-tax-legal",
            "--annual-turnover-idr", "400000000",
            "--annual-net-profit-idr", "80000000",
            "--entity-type", "wp_op",
        )
        self.assertEqual(r2["status"], "ok")
        self.assertEqual(r2["tax_comparison_pp_20_2026_idr"]["wp_orang_pribadi_umkm"], 0.0)
        self.assertIn("koperasi_umkm_window", r2["tax_comparison_pp_20_2026_idr"])

    def test_bass_diffusion_trend_and_zero_rupiah(self) -> None:
        r3 = run_cli("predict-trend", "--sector", "AI Workflow", "--current-adoption-pct", "10")
        self.assertEqual(r3["status"], "ok")
        self.assertIn("OPTIMAL ENTRY WINDOW", r3["lifecycle_phase"])

        r4 = run_cli(
            "zero-rupiah-plan",
            "--skill-or-network", "Automation",
            "--target-market", "UMKM Klinik",
            "--target-monthly-profit-idr", "10000000",
        )
        self.assertEqual(r4["status"], "ok")
        self.assertEqual(len(r4["blueprints"]), 3)

    def test_eternal_student_ledger_onboard_and_synergy(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env = {"BUSINESS_SAGE_HOME": tmp}
            r_app = run_cli("onboard-app", "--app", "python", env_override=env)
            self.assertEqual(r_app["status"], "ok")
            r_learn = run_cli(
                "phd-learn",
                "--topic", "Negative CCC Validation",
                "--insight", "50% upfront DP eliminates working-capital interest risk",
                env_override=env,
            )
            self.assertEqual(r_learn["status"], "ok")
            self.assertEqual(r_learn["total_phd_insights"], 1)

        r_syn = run_cli("synergy")
        self.assertEqual(r_syn["status"], "ok")
        self.assertEqual(r_syn["total_collaborative_skills"], 49)


if __name__ == "__main__":
    unittest.main(verbosity=2)
