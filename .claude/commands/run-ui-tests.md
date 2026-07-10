# /run-ui-tests

Goal: Run the Playwright UI suite for the current repo.

Inputs:
- target test suite or file
- environment configuration

Output:
- test execution result
- failures with context
- report summary

Rules:
- Use the repo's Playwright config.
- Report failures clearly and concisely.
