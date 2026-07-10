# Claude Automation Scaffolding

This workspace contains a modular test automation scaffold for UI and API testing.

## Included assets
- Claude skills for UI navigation, API testing, and test-data setup
- Claude commands for generating and running automation suites
- Hook definitions for automation lifecycle events
- MCP manifest definitions for skills, commands, hooks, file operations, and test generation
- Playwright TypeScript page objects and flow tests
- Python pytest API testpacks with helpers and fixtures
- AI-driven generation utilities for component, schema, and assertion analysis

## Quick start
1. Install Python dependencies: `pip install -r requirements.txt`
2. Install Playwright dependencies: `cd playwright && npm install && npx playwright install`
3. Run API tests: `pytest -q`
4. Run UI tests: `cd playwright && npx playwright test`

## Architecture principles
- Modular and reusable test components
- SOLID-oriented design
- CI/CD-ready structure
- Easy extension for new UI flows and API endpoints
