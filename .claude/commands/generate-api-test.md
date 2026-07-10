# /generate-api-test

Goal: Create a pytest API test for an endpoint or contract.

Inputs:
- endpoint and method
- expected status/body
- auth or headers if needed

Output:
- test module
- fixtures/helpers
- contract assertions

Rules:
- Cover one happy path and one error path.
- Validate status codes and response schema.
- Keep helpers reusable.
