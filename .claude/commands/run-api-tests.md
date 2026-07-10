# /run-api-tests

Goal: Run the pytest API suite for the current repo.

Inputs:
- target tests or endpoint scope
- environment configuration

Output:
- test execution result
- failures with context
- report summary

Rules:
- Use the repo's pytest config if present.
- Report failures clearly and concisely.
