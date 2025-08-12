##  Lab 3.3: Automated PR Description Generation for Complex Changes

###  Objective:
- Utilize GitHub Copilot to generate a comprehensive and well-structured Pull Request (PR) description for a significant code change, highlighting the problem, solution, testing, and impact.

---

###  Instructions:

####  Part 1: Understand the Refactor

Assume you have modernized a legacy module with the following changes:

- Migrated from synchronous to asynchronous programming using `asyncio` and `aiohttp`
- Implemented robust error handling with retry and backoff logic
- Improved API performance by batching requests (30% faster)
- Added comprehensive **unit and integration tests**

---

####  Part 2: Generate a PR Description Using Copilot

1. Create a file called `PR_description.md`.

2. Think through the following:
   - What the old code did and what the limitations were
   - What has changed in the new version (technically and architecturally)
   - What problems were solved and why these changes were necessary
   - What testing has been done and what reviewers should focus on

3. In that file, **write a clear Copilot prompt** that describes the context above and ask Copilot to generate a PR description.

4. Let Copilot generate the description, and then **refine it** as needed by:
   - Asking it to rephrase sections
   - Making the tone formal or concise
   - Adding missing sections like performance gains or testing coverage

---


