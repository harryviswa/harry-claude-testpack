from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


def write_file(path: Path, content: str, overwrite: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def scaffold_project(target_dir: Path | str) -> None:
    target = Path(target_dir).resolve()
    target.mkdir(parents=True, exist_ok=True)

    write_file(
        target / ".claude" / "commands" / "add-test.md",
        """
        # /add-test

        Goal: Add or extend UI and API test automation for this repository.

        Inputs:
        - target page/flow or API endpoint
        - existing project and test structure
        - expected behavior and acceptance criteria

        Output:
        - Playwright page object class or UI flow test
        - pytest test class/module
        - API helper object and fixtures
        - reusable selectors, assertions, and setup logic

        Rules:
        - Preserve existing README and settings files.
        - Generate page objects for UI flows.
        - Generate helper objects for API requests and test data.
        - Keep tests deterministic, reusable, and CI-friendly.
        """,
    )

    write_file(
        target / ".claude" / "commands" / "generate-ui-test.md",
        """
        # /generate-ui-test

        Goal: Create a Playwright UI test class and supporting page object for a user flow.

        Inputs:
        - target page or component
        - user action and expected outcome
        - existing app/test structure

        Output:
        - page object class with locators/actions
        - UI test or spec file
        - assertions for visible UI behavior

        Rules:
        - Use resilient locators and wait for stable state.
        - Create reusable page object methods.
        - Assert visible behavior, not internal implementation.
        - Keep the test flow clear and modular.
        """,
    )

    write_file(
        target / ".claude" / "commands" / "generate-api-test.md",
        """
        # /generate-api-test

        Goal: Create a pytest API test class and supporting request helper for an endpoint contract.

        Inputs:
        - endpoint, method, and expected status/body
        - auth, headers, or request context
        - existing API test conventions

        Output:
        - pytest test module or test class
        - request helper object or fixture
        - assertions for status, response shape, and contract

        Rules:
        - Prefer fixtures and helper objects over inline request code.
        - Cover a happy path and one error case.
        - Keep test data deterministic and easy to reuse.
        """,
    )

    write_file(
        target / ".claude" / "commands" / "generate-report.md",
        """
        # /generate-report

        Goal: Generate a concise automation report after each test run.

        Inputs:
        - test results and failure details
        - generated artifacts or logs

        Output:
        - pass/fail summary
        - key failure notes
        - next action suggestions

        Rules:
        - Keep it concise and evidence-based.
        - Include actionable follow-up steps.
        """,
    )

    write_file(
        target / ".claude" / "commands" / "run-ui-tests.md",
        """
        # /run-ui-tests

        Run the Playwright UI test suite for the current repository.
        """,
    )

    write_file(
        target / ".claude" / "commands" / "run-api-tests.md",
        """
        # /run-api-tests

        Run the pytest-based API test suite for the current repository.
        """,
    )

    write_file(
        target / ".claude" / "hooks" / "automation-lifecycle.md",
        """
        # Automation Lifecycle Hooks

        - beforeEach: prepare fixtures and environment state
        - afterEach: capture logs or screenshots
        - afterAll: generate a summary report
        """,
    )

    write_file(
        target / ".claude" / "hooks" / "reporting" / "report-generator.py",
        """
        from pathlib import Path
        from datetime import datetime

        def generate_report(test_results=None, output_path="artifacts/automation-report.md"):
            output = Path(output_path)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(
                f"# Automation Report\\n\\n- Generated: {datetime.utcnow().isoformat()}\\n- Passed: {test_results.get('passed', 0) if test_results else 0}\\n- Failed: {test_results.get('failed', 0) if test_results else 0}\\n",
                encoding="utf-8",
            )
            return output
        """,
    )

    write_file(
        target / ".claude" / "CLAUDE.md",
        """
        # Claude Automation Setup

        Commands:
        - /add-test
        - /generate-ui-test
        - /generate-api-test
        - /generate-report

        Hooks:
        - automation-lifecycle
        - reporting/report-generator
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
        target / "scripts" / "run_automation.py",
        """
        from pathlib import Path
        import subprocess
        import sys

        def main() -> int:
            root = Path(__file__).resolve().parents[1]
            for target in ["api_tests", "tests"]:
                result = subprocess.run([sys.executable, "-m", "pytest", "-q", target], cwd=root)
                if result.returncode != 0:
                    return result.returncode
            return 0

        if __name__ == "__main__":
            raise SystemExit(main())
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
        overwrite=False,
    )

    write_file(
        target / ".vscode" / "settings.json",
        """
        {
          "files.exclude": {
            "**/__pycache__": true,
            "**/.pytest_cache": true
          }
        }
        """,
        overwrite=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Claude test automation scaffold into a repository")
    parser.add_argument("target", nargs="?", default=".", help="Target repository path")
    args = parser.parse_args()
    scaffold_project(args.target)
    print(f"Scaffold installed in {Path(args.target).resolve()}")


if __name__ == "__main__":
    main()
