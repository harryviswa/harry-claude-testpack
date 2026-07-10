from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from claude_test_scaffold.cli import scaffold_project


def test_scaffold_project_creates_claude_assets(tmp_path):
    target = tmp_path / "demo_repo"
    target.mkdir()

    scaffold_project(target)

    assert (target / ".claude" / "commands" / "add-test.md").exists()
    assert (target / ".claude" / "skills" / "ui-navigation" / "SKILL.md").exists()
    assert (target / "requirements.txt").exists()
    assert (target / "playwright" / "playwright.config.ts").exists()
