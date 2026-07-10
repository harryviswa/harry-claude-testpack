# /add-test

Goal: Create or extend UI and API test automation for the current repo.

Inputs:
- app structure or target page/endpoint
- existing test patterns if present

Output:
- UI page objects or flow tests
- API pytest tests and helpers
- reusable assertions

Rules:
- Prefer small, reusable components.
- Keep tests deterministic and CI-safe.
- Avoid brittle selectors and over-mocking.
