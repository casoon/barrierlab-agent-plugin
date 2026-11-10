"""Engine invariants of the digest, over real `barrierlab --json` output."""

import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import digest  # noqa: E402


def load(name):
    return json.loads((ROOT / "tests" / "fixtures" / name).read_text(encoding="utf-8"))


class Digest(unittest.TestCase):
    def setUp(self):
        self.report = load("page.json")
        self.lines = (ROOT / "examples" / "page.html").read_text(encoding="utf-8").split("\n")
        self.text = digest.digest(self.report, self.lines, "examples/page.html")

    def test_every_finding_appears_once(self):
        for finding in self.report["findings"]:
            self.assertEqual(self.text.count(f"`{digest.key(finding)}`"), 1, digest.key(finding))

    def test_keys_are_unique_within_the_report(self):
        keys = [digest.key(finding) for finding in self.report["findings"]]
        self.assertEqual(len(keys), len(set(keys)))

    def test_every_rule_that_did_not_run_appears_with_its_reason(self):
        not_run = [run for run in self.report["rule_runs"] if "not_run" in run]
        self.assertEqual(len(not_run), 3)
        for run in not_run:
            self.assertIn(f"`{run['rule_id']}`", self.text)
            self.assertIn(run["reason"], self.text)

    def test_counts_are_the_engine_summary(self):
        self.assertIn("5 failed · 8 need review · 23 not checked · 3 rules did not run", self.text)
        self.assertNotIn("Warning", self.text)

    def test_sections_keep_their_order(self):
        order = [self.text.index(title) for title in ("## 1. Failed", "## 2. Needs review", "## 3. Not checked", "## 4. Plan")]
        self.assertEqual(order, sorted(order))

    def test_source_line_and_evidence_are_quoted(self):
        self.assertIn('source: `<img src="team.jpg">`', self.text)
        self.assertIn("contrast_ratio = 2.59", self.text)

    def test_best_practice_is_a_recommendation(self):
        section = self.text[self.text.index("`landmarks/main-missing`") :].split("\n")[0]
        self.assertIn("recommendation (best practice), not a violation", section)

    def test_a_summary_that_disagrees_is_reported_not_corrected(self):
        self.report["summary"]["fail"] = 4
        text = digest.digest(self.report)
        self.assertIn("lists 5 `fail` findings, its summary says 4", text)
        self.assertIn("4 failed", text)

    def test_check_names_what_a_finished_report_lost(self):
        self.assertEqual(digest.missing(self.report, self.text), [])
        cut = self.text.replace("`images/alt-missing@14:3`", "the image").replace("`focus/obscured-enhanced`", "")
        self.assertEqual(digest.missing(self.report, cut), ["images/alt-missing@14:3", "focus/obscured-enhanced"])

    def test_unusable_inputs_come_first(self):
        text = digest.digest(load("linked.json"))
        self.assertIn("stylesheet_unavailable: `site.css`", text)
        self.assertLess(text.index("## Inputs the engine could not use"), text.index("## 1. Failed"))

    def test_the_example_reports_are_the_digest_output(self):
        """examples/*.report.md is what the project site shows."""
        for name in ("page", "linked"):
            source = f"examples/{name}.html"
            lines = (ROOT / source).read_text(encoding="utf-8").split("\n")
            expected = digest.digest(load(f"{name}.json"), lines, source) + "\n"
            self.assertEqual((ROOT / "examples" / f"{name}.report.md").read_text(encoding="utf-8"), expected, name)


if __name__ == "__main__":
    unittest.main()
