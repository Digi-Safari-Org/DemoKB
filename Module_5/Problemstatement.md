##  Lab 5.1: Simulated API & SDK Upgrade

###  Objective:
- Leverage **GitHub Copilot ** to refactor legacy client code to align with a modernized SDK/API structure.
- Practice enterprise-grade modernization techniques such as:
  - Method renaming
  - Data structure transformation
  - Encapsulation and dependency abstraction
- Simulate a real-world SDK migration by replacing flat procedural logic with structured, object-oriented interactions.

---

###  Context:
You are working on a Python codebase that uses an outdated `LegacyPaymentAPI` client. This client uses:
- Procedural, verbose method names
- Flat dictionary responses
- Manual parameter passing

Your organization is now adopting a new `ModernPaymentAPI`, which features:
- Intuitive, concise method names
- Nested and structured return values
- Payload-based input (dictionaries)
- Typed and encapsulated design patterns

---

###  Instructions:

####  Part 1: Understand the Legacy Code

1. Create a file named `legacy_payment_client.py`.
2. Paste the legacy API class and client logic (provided separately by the instructor or lab environment).
3. Review the use of:
   - `authenticate_user()` and `process_transaction_v1()`
   - Flat dictionary checks like `if response["status"] == "success"`

---

####  Part 2: Understand the Modern API (Simulated)

- Familiarize yourself with the new API concept:
  - `login()` returns a nested structure with `success` and `session_id`
  - `execute_payment()` accepts a dictionary with amount, currency, and customer_id
  - Returns nested `transaction` objects with `id` and `status`

Note: You do not need to implement the new API, only simulate refactoring the legacy code to use it.

---

####  Part 3: Prompt Copilot to Refactor

1. Use **Copilot inline comments** or **Copilot Chat**.

2. write the prompt above the legacy client codeto:

   -  Refactor the legacy client code to use the ModernPaymentAPI.

   -  Instead of authenticate_user, use the login method which returns a session_id inside the success block.

   -  Replace process_transaction_v1 with execute_payment, which accepts a payment_details dictionary.

   -  Update how the transaction status and ID are retrieved — these are now located inside a nested transaction object.

Then guide Copilot to:
- Rename and restructure method calls
- Change from token-based to session-based logic
- Replace individual arguments with the `payment_details` dictionary

---

####  Bonus Tips:
Ask Copilot to:
- Validate required keys like `session_id` or `transaction["id"]`
- Add error handling and fail-safe branches
- Use enterprise naming standards (`session_id`, `payment_details`, `transaction_info`)

---

####  Part 4: Optional Enhancements

Enhance the refactor by:
- Adding `"customer_id"` to `payment_details`
- Using Python’s built-in `logging` module to log failure cases
- Wrapping the modernized flow in a function `run_payment_flow()` with proper type annotations

