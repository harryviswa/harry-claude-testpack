---
name: api-testing
description: Claude-native pytest guidance for API test generation and execution.
---

Goal: Create and maintain reliable API automation.

Inputs:
- endpoint and method
- expected response shape
- auth or headers if needed

Output:
- test module
- helpers/fixtures
- assertions for contract and behavior

Rules:
- Prefer helpers/fixtures over inline requests.
- Validate status codes, bodies, and schema expectations.
- Cover one happy path and one error path per endpoint.
- Keep tests deterministic and easy to extend.
