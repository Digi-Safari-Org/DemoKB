##  Lab 2.1: Refactoring and Standardizing Code with Copilot Chat

####  Objectives:
- Learn to refactor monolithic functions into smaller, reusable components using Copilot Chat.
- Practice enforcing enterprise-level standards, such as consistent logging conventions.
- Understand how simulated knowledge base templates can guide standardized prompting across teams.

---

###  Instructions:

####  Part 1: Refactor a Monolithic Function

1. Begin with a Python function that performs multiple unrelated responsibilities, such as validation, ID generation, and database operations.

2. Use Copilot Chat to break the large function into smaller, logically grouped helper functions (e.g., one for email validation, another for generating user IDs, etc.).

3. Review the refactored suggestions from Copilot and apply them to improve code modularity.

4. Replace any `print()` statements with reusable logging logic (see Part 2).

5. **Add test cases** at the end of the script (in a `__main__` block) to verify that:
   - Each helper function works as expected
   - The overall `process_user_data()` function behaves correctly for different operations (add, update, invalid)
   - Logging is triggered in the correct format for each operation

---

####  Part 2: Apply Enterprise Logging Standards

1. Start with Python functions that contain inconsistent or unstructured log messages.

2. Assume your organization follows a strict logging format:  
   All logs must begin with `[APP_NAME] - [MODULE_NAME] -` followed by the actual message.

3. Define a reusable logging function like `log_message(message, level)` to encapsulate this format.

4. Replace all existing print/logging statements with calls to `log_message()`.

5. **Test the logging output** by running your refactored code and ensuring each log appears in the correct format.
