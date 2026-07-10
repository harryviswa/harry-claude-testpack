from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def scaffold_project(target_dir: Path | str) -> None:
    target = Path(target_dir).resolve()
    target.mkdir(parents=True, exist_ok=True)

    write_file(
        target / ".claude" / "commands" / "add-test.md",
        """
        # /add-test

        Generate UI and API tests for the current repository.

        ## Workflow
        1. Inspect the existing app structure.
        2. Create or update page objects for UI flows.
        3. Add pytest-based API tests and helpers.
        4. Ensure assertions are reusable and CI-friendly.
        """,
    )

    write_file(
        target / ".claude" / "skills" / "ui-navigation" / "SKILL.md",
        """
        ---
        name: ui-navigation
        description: Reusable Playwright-based UI navigation and component interaction skills.
        ---
        """,
    )

    write_file(
        target / ".claude" / "skills" / "api-testing" / "SKILL.md",
        """
        ---
        name: api-testing
        description: Reusable pytest-based API automation skills.
        ---
        """,
    )

    write_file(
        target / ".claude" / "skills" / "test-data-setup" / "SKILL.md",
        """
        ---
        name: test-data-setup
        description: Utilities to generate deterministic test data and fixtures.
        ---
        """,
    )

    write_file(
        target / "requirements.txt",
        """
        pytest>=8.0.0
        requests>=2.31.0
        pytest-cov>=4.0.0
        """,
    )

    write_file(
        target / "playwright" / "playwright.config.ts",
        """
        import { defineConfig } from '@playwright/test';

        export default defineConfig({
          testDir: './tests',
          timeout: 30000,
          use: {
            baseURL: process.env.BASE_URL || 'http://localhost:3000',
            headless: true,
            trace: 'on-first-retry',
          },
        });
        """,
    )

    write_file(
        target / "playwright" / "package.json",
        """
        {
          "name": "playwright-ui-scaffold",
          "private": true,
          "scripts": {
            "test": "playwright test"
          },
          "devDependencies": {
            "@playwright/test": "^1.54.0"
          }
        }
        """,
    )

    write_file(
        target / "api_tests" / "conftest.py",
        """
        import pytest
        import requests

        @pytest.fixture
def api_client() -> requests.Session:
            session = requests.Session()
            session.headers.update({"Accept": "application/json"})
            return session
        """,
    )

    write_file(
        target / "README.md",
        """
        # Test Automation Scaffold

        Install with:
        pip install claude-test-scaffold

        Then run:
        claude-test-scaffold /path/to/your/repo
        """,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Claude test automation scaffold into a repository")
    parser.add_argument("target", nargs="?", default=".", help="Target repository path")
    args = parser.parse_args()
    scaffold_project(args.target)
    print(f"Scaffold installed in {Path(args.target).resolve()}")


if __name__ == "__main__":
    main()
