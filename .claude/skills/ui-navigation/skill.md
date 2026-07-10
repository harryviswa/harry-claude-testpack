---
name: ui-navigation
description: Claude-native Playwright guidance for UI test generation and execution.
---

Goal: Create and maintain reliable UI automation.

Inputs:
- target page or component
- user flow
- expected UI state

Output:
- page object or flow test
- assertions for visible behavior

Rules:
- Prefer page objects for reusable flows.
- Use resilient selectors and user-visible assertions.
- Wait for stable state before interactions.
- Keep tests focused on behavior, not implementation details.
