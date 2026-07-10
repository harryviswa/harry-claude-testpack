---
name: test-data-setup
description: Claude-native guidance for deterministic test data and fixtures.
---

Goal: Create isolated, reusable test data.

Inputs:
- target scenario
- required data shape
- cleanup needs

Output:
- fixtures or payload builders
- deterministic seed data

Rules:
- Generate minimal, deterministic fixtures.
- Keep setup local to the test or fixture scope.
- Reset or clean up state where needed.
- Prefer realistic payloads over overly complex data.
