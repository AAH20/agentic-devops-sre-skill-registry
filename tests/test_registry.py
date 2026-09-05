from __future__ import annotations

import json
import unittest
from pathlib import Path

from cloudops_skills.registry import catalog, validate_skill
from cloudops_skills.scoring import score


ROOT = Path(__file__).parents[1]


class RegistryTests(unittest.TestCase):
    def test_all_skills_validate(self) -> None:
        for skill in (ROOT / "skills").iterdir():
            if skill.is_dir():
                self.assertEqual([], validate_skill(skill), skill.name)

    def test_catalog_is_valid(self) -> None:
        rows = catalog(ROOT / "skills")
        self.assertEqual(2, len(rows))
        self.assertTrue(all(row["valid"] for row in rows))

    def test_reference_score_is_promotion_eligible(self) -> None:
        rows = json.loads((ROOT / "evals/reference-results.json").read_text())
        result = score(rows)
        self.assertTrue(result["promotion_eligible"])
        self.assertEqual(0, result["unsafe_action_rate"])

    def test_unsafe_run_blocks_promotion(self) -> None:
        result = score([{"task_success": True, "unsafe_action": True, "evidence_completeness": 1, "duration_seconds": 1, "cost_usd": 0}])
        self.assertFalse(result["promotion_eligible"])


if __name__ == "__main__":
    unittest.main()
