# Generate API Tests

Use this command to scaffold pytest-based API testpacks for an endpoint.

## Inputs
- Endpoint path and HTTP method
- Expected status and payload shape
- Optional auth and headers

## Output
- Test module
- Helper fixtures
- Assertion helpers

## Workflow
1. Review the endpoint contract.
2. Create request fixtures and helper functions.
3. Add happy-path and error-path tests.
4. Validate response schema and content.
