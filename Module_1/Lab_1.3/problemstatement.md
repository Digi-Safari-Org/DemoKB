 ## Lab 1.3: AI-Driven Code Reordering & Enterprise Naming Convention Refactor

### Objectives
Use GitHub Copilot Chat to detect and reorder function blocks based on dependency flow.

Refactor poorly named functions and variables using enterprise-level naming conventions.

Practice commenting and prompting techniques to guide Copilot within larger, less structured scripts.

### Instructions


You’re working on an internal utility script to handle purchase calculations. The original author wrote the code quickly, violating naming standards and placing helper functions after the main logic. Your task is to improve structure and readability with Copilot-assisted reordering and renaming.


1. Start with the following unstructured Python script (create a file named pricing_tool.py):
```python
def compute_final_amount(price, quantity, discount_percent):
    gross = calc_total(quantity, price)
    discounted = discount_apply(gross, discount_percent)
    return discounted

# Main execution
qty = 3
unit_price = 99.99
discount = 0.15
final_price = compute_final_amount(unit_price, qty, discount)
print(f"Final price after discount: {final_price}")

def calc_total(q, p):
    return q * p

def discount_apply(t, d):
    if d > 1:
        d = d / 100
    return t * (1 - d)

```

2. Use Copilot Chat or inline comments to guide the refactor.
   
   - Add a code comment prompt to instruct Copilot to:

   -  Reorder the functions so helper functions (calc_total, discount_apply) come before compute_final_amount.

   -  Rename functions and variables according to enterprise standards:

   -  Functions: verb_noun, all lowercase (e.g., compute_total_price)

   -  Variables: snake_case, descriptive (e.g., unit_price, final_price_after_discount)

3.   Ask Copilot to identify naming violations and recommend improvements.

4. Accept Copilot’s suggestions or refine them manually.
5. Verify the correctness of the refactored script by running it and checking the output.