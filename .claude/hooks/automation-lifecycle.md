# Automation Lifecycle Hooks

## Hook points
- beforeEach: prepare fixtures, environment variables, and isolated state
- afterEach: capture screenshots or logs and reset temporary data
- beforeAll: initialize shared resources
- afterAll: generate a summary report and publish artifacts

## Default behavior
Every automation run should call the reporting hook at the end to produce a reusable summary.
