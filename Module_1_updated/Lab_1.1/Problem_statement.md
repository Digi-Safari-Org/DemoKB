# Lab 1.1: Contextual Prompting for Code Reordering and Signature Upgrades in Large Python Repos

### Objectives:
    - Learn to write detailed, contextual prompts for Copilot Chat leveraging large internal repo context.

    - Practice reordering complex function code for readability and efficiency.

    - Upgrade function signatures to improve type safety and usability.

    - Emphasize how Copilot Chat in GitHub UI or IDE can access multi-file context for better suggestions.

### Instructions:

Part 1: Code Reordering for Readability
1. You are given a Python function that contains mixed responsibilities and out-of-order statements, making it hard to read and maintain.

2. Using Copilot Chat, prompt it to reorder the statements logically into:

   - Input validation

   - Data processing

   - Output formatting

3. Provide Copilot with a detailed comment block describing the expected function behavior and input/output types for better suggestions.

Part 2: Signature Upgrade with Type Annotations and Default Arguments

1. Upgrade the function signature to use Python 3 type annotations for all parameters and return types.

2. Introduce default argument values where applicable.

3. Use Copilot Chat contextual prompts to suggest idiomatic Python signatures consistent with your enterprise’s coding standards.

Part 3: Using Copilot Chat with Multi-File Context

1. Assume this function depends on a utility function defined in another file in the repo.

2. Use Copilot Chat inside your IDE or GitHub UI with access to the entire project context to improve and simplify your implementation using that utility function.

```python
def process_order(data):
    # TODO: process order and return summary string
    summary = ""
    if "items" in data:
        for item in data["items"]:
            summary += f"{item['name']} x {item['qty']}, "
    if not data.get("customer_id"):
        return "Error: Missing customer ID"
    if "discount" in data:
        discount = data["discount"]
    else:
        discount = 0
    total = sum([item["price"]*item["qty"] for item in data.get("items", [])])
    total -= discount
    return summary + f"Total: ${total}"
```