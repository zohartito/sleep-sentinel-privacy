"""Offline audit regressions. Run with: python3 -B -m unittest discover -v."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parent


class WorkflowAuditTests(unittest.TestCase):
    def setUp(self):
        self.review = (ROOT / ".github/workflows/claude-pr-review.yml").read_text()

    def test_ssp_01_review_capabilities_are_comment_only(self):
        checks = {
            "no tag-mode progress tools": "track_progress: false" in self.review,
            "explicit workflow token": "github_token: ${{ github.token }}" in self.review,
            "read-only contents": bool(re.search(r"(?m)^      contents: read\s*(?:#.*)?$", self.review)),
            "review comments": bool(re.search(r"(?m)^      pull-requests: write\s*(?:#.*)?$", self.review)),
            "no OIDC token exchange": "id-token:" not in self.review,
        }
        for label, satisfied in checks.items():
            with self.subTest(policy=label):
                self.assertTrue(satisfied, label)

        allowed = re.search(r'--allowedTools "([^"]+)"', self.review)
        self.assertIsNotNone(allowed, "Review must explicitly allow only comment/read tools")
        self.assertEqual(set(allowed.group(1).split(",")), {
            "mcp__github_inline_comment__create_inline_comment",
            "Bash(gh pr diff:*)", "Bash(gh pr view:*)", "Bash(gh pr comment:*)",
        })
        denied = re.search(r'--disallowedTools "([^"]+)"', self.review)
        self.assertIsNotNone(denied, "Review must explicitly deny editing and git mutation tools")
        self.assertTrue({
            "Edit", "Write", "NotebookEdit", "Bash(git:*)", "Bash(rm:*)",
            "Bash(gh api:*)", "Bash(gh pr checkout:*)", "Bash(gh pr edit:*)",
            "Bash(gh pr merge:*)",
        }.issubset(set(denied.group(1).split(","))))

    def test_ssp_02_reviewer_is_disabled_without_verified_executable(self):
        self.assertRegex(
            self.review, r"(?m)^    if: \$\{\{ false \}\}$",
            "The review job must stay disabled while it relies on the remote installer",
        )

    def test_ssp_n2_token_comment_does_not_claim_action_cannot_push(self):
        self.assertNotIn("CANNOT push", self.review)


if __name__ == "__main__":
    unittest.main()
