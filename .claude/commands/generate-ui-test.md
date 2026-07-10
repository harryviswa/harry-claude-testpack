# /generate-ui-test

Goal: Create a Playwright UI test for a page, component, or flow.

Inputs:
- target page/component
- user action
- expected outcome

Output:
- page object
- flow test
- assertions

Rules:
- Prefer resilient selectors.
- Assert visible behavior, not implementation details.
- Use waits for stable state.
