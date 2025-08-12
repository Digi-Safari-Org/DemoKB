##  Lab 4.1: Unit Testing with Copilot and Pytest

###  Objective:
- Use GitHub Copilot to generate **parameterized unit tests** for a utility module using Pytest.
- Extend testing to include **mocking**, **exception handling**, and **invalid input validation**.
- Ensure test modularity, clarity, and coverage against edge cases.
- Enforce consistent test structure using prompt templates or knowledge base conventions.

---

###  Instructions:

####  Part 1: Review the Utility Code

You are given a Python module `math_utils.py`:

```python
def add(a, b):
    return a + b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numeric.")
    return a / b if b != 0 else None

def is_even(n):
    return n % 2 == 0

def log_and_add(a, b, logger):
    result = add(a, b)
    logger.log(f"Adding {a} and {b} = {result}")
    return result
```

---

####  Part 2: Write Parameterized Tests Using Copilot

1. Create a file called `test_math_utils.py`.

2. Use Copilot to generate parameterized test functions for:
   - `add(a, b)` – Test positives, negatives, large values.
   - `divide(a, b)` – Test division, zero division, and invalid types.
   - `is_even(n)` – Test range of values including negative and zero.

3. Add **assertion messages** and **test IDs** to clearly indicate each test case scenario.

---

####  Part 3: Add Exception Handling Tests

Ask Copilot to generate test cases that:

- Assert that `divide("10", 2)` or `divide(10, "2")` raises a `TypeError`
- Use `pytest.raises` to validate exception messages

---

####  Part 4: Add Mocking (Advanced)

Assume a new function exists in `math_utils.py`:

```python
def log_and_add(a, b, logger):
    result = add(a, b)
    logger.log(f"Adding {a} and {b} = {result}")
    return result
```

Use `unittest.mock.Mock` to test:
- That the logger's `log()` method is called with the correct message.
- That the result is correct and logger interaction is properly validated.

---
