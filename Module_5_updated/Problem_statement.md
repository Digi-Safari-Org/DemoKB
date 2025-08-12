# Lab 5.1: API/SDK Upgrade with Cross-Repo Code Reuse

## Objective
- Refactor a legacy client API usage to a modernized SDK version.
- Discover and reuse helper utilities from a separate enterprise repository via GitHub Copilot Enterprise cross-repo suggestions.
- Practice maintaining enterprise-grade naming conventions and error handling during refactoring.

## Context
Your project is upgrading from `LegacyDataAPI` to `ModernDataSDK`. The legacy API uses procedural calls and flat data structures, while the modern SDK uses object-oriented design, nested responses, and payload dictionaries.

Additionally, an enterprise utilities repository contains helper functions for request validation and response parsing that you should incorporate instead of rewriting.

---

## Instructions

### Part 1: Legacy Code Review
- Create a file named `legacy_data_client.py`.
- Implement sample legacy client usage:
  - `legacy_authenticate()` returns a token string.
  - `legacy_fetch_data(id)` returns flat dictionaries.
  - Manual inline parsing and validation of responses.

### Part 2: Explore Enterprise Utilities Repo
- Simulate or create a separate repo called `enterprise_utils` containing:
  - `validate_response(data: dict) -> bool`
  - `extract_data_field(data: dict, field: str) -> Any`
  - Other helper functions for request payload formatting.
- Use GitHub Copilot Enterprise's **cross-repo suggestion** feature to discover and import these utility functions while refactoring.

### Part 3: Refactor to Modern SDK
- Replace legacy API calls with `ModernDataSDK` usage:
  - Use `login()` method returning a `session_id`.
  - Use `fetch_data(payload: dict)` returning nested response objects.
- Replace manual validation with the `validate_response()` utility from the enterprise repo.
- Extract required data fields using `extract_data_field()`.
- Maintain enterprise naming conventions and add typing annotations where appropriate.
- -Note : Output format must remain backward-compatible with the legacy client for integration safety

### Part 4: Error Handling & Logging
- Add robust error handling for scenarios such as failed login or missing expected fields.
- Use Python’s built-in `logging` module to log failures following standardized enterprise logging formats.

### Part 5: Test & Verify
- Write test cases verifying:
  - Successful login and data fetch.
  - Proper handling of invalid responses.
  - Correct use of reusable utilities.
- Verify that the refactored code produces identical functional results but with cleaner and reusable logic.

---