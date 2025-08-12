##  Lab 2.2: Index-Aware Prompting and Cross-File Code Reuse

####  Objectives:
- Practice using structured prompts to guide Copilot in discovering and reusing functions from other files in a large enterprise codebase.
- Refactor and expand utility functions to make them Copilot-indexable via rich docstrings and type hints.
- Improve your ability to reuse code contextually using Copilot Chat or inline completions.
- Verify the integrity and usability of helper utilities through structured tests.

---

###  Instructions:

###  Part 1: Create and Structure a Utility Module (`utils.py`)

1. Create a Python file called `utils.py` and define at least **three helper functions**:
    - `format_currency(amount: float, currency_symbol: str = "$") -> str`: returns a formatted currency string.
    - `sanitize_input(value: str) -> str`: trims whitespace and removes illegal characters (like `\n`, `\t`).
    - `convert_to_uppercase(value: str) -> str`: returns the uppercased version of a string, used for standardizing product codes.

2. For each function:
    - Add **complete type hints**
    - Add **rich docstrings** using standard documentation format (Args, Returns, Example)

---

###  Part 2: Simulate Enterprise Prompting via `main_app.py`

1. Create another file called `main_app.py`.
2. Add prompt-style comments (as you would do when using Copilot Chat) to describe the following:
    - You want to display a product name and price
    - The product name should be cleaned and uppercased
    - The price should be formatted with a currency symbol
3. Instead of manually writing imports, **use only comments** and see if Copilot suggests:
    - Importing the correct utility functions
    - Using them in the correct order

---

###  Part 3: Validate Behavior with Assertions

1. Instead of just printing output, write **at least 3 assertion tests** to verify:
    - The sanitized and uppercased product name matches expectations
    - The currency is formatted as expected
    - Invalid values like empty strings or incorrect types raise meaningful errors (add `try/except` if needed)

2. Add a test runner block using `if __name__ == "__main__":` and run the validations.

---


