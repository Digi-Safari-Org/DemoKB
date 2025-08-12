# Module 4: Automated Testing with Copilot (Advanced Workflow Challenge)

### Objective

- Generate **unit, integration, and regression** tests.

- Use **parameterized test generation**.

- Eliminate redundant test creation across frameworks by reusing data/helpers.

- Perform **cross-framework test integration** (PyTest + unittest).

- Use **Knowledge Bases** to ensure consistent structure, naming, and docstrings.

- Review generated test code via **audit trails** and **Pull Requests**.

---


## **Part A – Function-Level Testing**


### Scenario

You are working in the `order_service/` module of an e-commerce platform. The `order_calculator.py` file contains:



```python

def calculate_discount(price, discount_percentage):

    return price - (price * discount_percentage / 100)



def calculate_tax(price, tax_rate):

    return price + (price * tax_rate / 100)



def final_price(price, discount_percentage, tax_rate):

    discounted = calculate_discount(price, discount_percentage)

    return calculate_tax(discounted, tax_rate)
```



### Tasks

1. Create unit tests for:

    - calculate_discount
    - calculate_tax
    - final_price

- Use PyTest parameterization.

2. Integration Tests

    - Create integration tests for discount + tax workflows.

3. Regression Tests

    - Create regression tests for the historical bug:


    - final_price(100, 100, 10) → Expected: 0.0 (was 10.0 before bug fix)

4. Avoid redundant definitions:

    - Move test parameters into test_data.py.

    - Import test_data.py in both PyTest and unittest tests.

5. Consistency via Knowledge Base

    - Follow naming conventions.

    - Use Google-style docstrings.

    - Apply Arrange-Act-Assert format.

6. Pull Request Simulation

    - Generate a PR description summarizing coverage.

    - Include a checklist for reviewers.
---

# Part B – API Endpoint Testing
### Scenario
You have a Flask API /calculate endpoint in app.py:

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    total = data["a"] + data["b"]
    return jsonify({"result": total})

if __name__ == "__main__":
    app.run()
```
### Tasks

1. Integration Tests

   - Create integration tests for /calculate using:

       - PyTest + requests library.

       - unittest + requests library.

2. Parameterized Cases

   - Parameterize tests for multiple payloads.

3. Avoid Redundancy

   - Create api_helpers.py with a post_calculate(a, b) helper.

4. Consistency via Knowledge Base

   - Test names must start with test_.

   - Use Google-style docstrings.

   - Apply Arrange-Act-Assert format.

5. Pull Request Simulation

   - Generate an audit summary listing:

     - Framework coverage.

     - Parameterized cases.

     - Helper reuse.



