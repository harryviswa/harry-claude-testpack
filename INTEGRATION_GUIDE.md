# Integration Guide

## Drop-in usage
1. Copy the .claude directory into your repository root.
2. Add the MCP manifest to your project configuration if your environment supports it.
3. Install Python requirements from requirements.txt.
4. Install Playwright dependencies from playwright/package.json.

## Customizing the scaffold
- Add new skills under .claude/skills/.
- Add new commands under .claude/commands/.
- Add new hooks under .claude/hooks/.
- Create UI page objects under playwright/page-objects/.
- Add API helpers under api_tests/helpers/.

## CI/CD notes
- Run pytest in the repository root.
- Run Playwright tests from the playwright folder.
- Store environment variables such as BASE_URL and API_BASE_URL in your CI secrets.
