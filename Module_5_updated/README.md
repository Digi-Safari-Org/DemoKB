# Lab 5.1 — API/SDK Upgrade with Cross-Repo Code Reuse

## Objective
Refactor the legacy client to use a ModernDataSDK and enterprise utilities. Use GitHub Copilot Enterprise cross-repo suggestions to create the missing modules.

## Provided files
- legacy/legacy_data_client.py  (legacy API you will replace)
- tests/test_refactor.py        (automated tests to validate your refactor)

## What you must implement (using Copilot)
Create the following files (by using Copilot prompts ):
- enterprise_utils/helpers.py
- modern_sdk/sdk.py
- refactor/modern_data_client.py
- main.py (optional demo)

## How to use Copilot in this lab
1. In VS Code, create the target file (e.g. enterprise_utils/helpers.py).
2. Paste the Copilot prompt provided for that file as a top comment.
3. Trigger Copilot suggestions or Copilot Chat to generate code.
4. Review and edit the suggestion, run tests, iterate.

## Run tests
From the project root:
