from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from claude_test_scaffold.cli import scaffold_project


def test_scaffold_project_creates_claude_assets(tmp_path):
    target = tmp_path / "demo_repo"
    target.mkdir()

    scaffold_project(target)

    assert (target / ".claude" / "CLAUDE.md").exists()
    assert (target / ".claude" / "commands" / "add-test.md").exists()
    assert (target / ".claude" / "commands" / "generate-report.md").exists()
    assert (target / ".claude" / "hooks" / "automation-lifecycle.md").exists()
    assert (target / ".claude" / "hooks" / "reporting" / "report-generator.py").exists()
    assert (target / ".claude" / "skills" / "ui-navigation" / "SKILL.md").exists()
    assert (target / "requirements.txt").exists()
    assert (target / "playwright" / "playwright.config.ts").exists()
    assert (target / "scripts" / "run_automation.py").exists()


def test_scaffold_project_preserves_existing_readme_and_settings(tmp_path):
    target = tmp_path / "demo_repo"
    target.mkdir()
    readme = target / "README.md"
    settings = target / ".vscode" / "settings.json"
    settings.parent.mkdir(parents=True)
    readme.write_text("# Existing Project\n", encoding="utf-8")
    settings.write_text('{"existing": true}\n', encoding="utf-8")

    scaffold_project(target)

    assert readme.read_text(encoding="utf-8").startswith("# Existing Project")
    assert settings.read_text(encoding="utf-8").strip() == '{"existing": true}'
