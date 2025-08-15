# Lab 2.1: Refactoring and Standardizing Code with Copilot Chat (JavaScript)

### Objectives

- Learn to refactor monolithic functions into smaller, reusable components using Copilot Chat.

- Practice enforcing enterprise-level standards, such as consistent logging conventions.

- Understand how simulated knowledge base templates can guide standardized prompting across teams.

### Instructions
Part 1: Refactor a Monolithic Function

1. Begin with a JavaScript function that performs multiple unrelated responsibilities, such as:

- Input validation (e.g., email or user data)

- User ID generation

- Database operations (simulated using arrays or JSON files)

2. Use GitHub Copilot Chat to break the large function into smaller, logically grouped helper functions, for example:

- validateEmail(email) → validates email format

- generateUserId() → generates unique user ID

- saveUserToDB(user) → adds or updates user in database

3. Review the refactored suggestions from Copilot and apply them to improve code modularity.

4. Replace any console.log() statements with reusable logging logic (see Part 2).

5. Add test cases at the bottom of the script to verify that:

- Each helper function works as expected.

- The overall processUserData() function behaves correctly for different operations (add, update, invalid).

- Logging is triggered in the correct format for each operation.

Part 2: Apply Enterprise Logging Standards

1. Assume your organization follows a strict logging format:
```js
[APP_NAME] - [MODULE_NAME] - [LEVEL] - Actual message
```

2. Define a reusable logging function:

```js
function logMessage(moduleName, level, message) {
  console.log(`[MY_APP] - ${moduleName} - ${level} - ${message}`);
}
```

3. Replace all existing console.log() statements in your helper and main functions with calls to logMessage().

4. Test the logging output by running your refactored code and ensuring each log appears in the correct format.