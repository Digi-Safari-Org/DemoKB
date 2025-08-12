# Lab 1.2: Enforcing Enterprise Naming Conventions and Using Copilot Chat Agents for Large Project Context

### Objectives:
    - Learn to write prompts that enforce enterprise naming conventions.

    - Use Copilot Chat to rename variables and functions across a file/project consistently.

    - Practice creating descriptive, standard-compliant function names and docstrings.

    - Understand differences in Copilot Chat usage in GitHub UI vs IDE with large repo context.

### Instructions:
Part 1: Rename variables and functions for consistency

1. You have a Python module with inconsistent variable names (e.g., itm, qtyOrdered, calcPrice) that violate your enterprise naming standards (snake_case, descriptive names).

2. Use Copilot Chat with a detailed prompt to rename variables and functions consistently across the file.

3. Verify that renamed variables follow snake_case and are self-explanatory.

Part 2: Standardize function names and add docstrings

1. Your functions currently lack proper names and docstrings.

2. Ask Copilot Chat to rename ambiguous functions to enterprise-standard descriptive names and add PEP-257 compliant docstrings including parameter and return types.


Part 3: Using Copilot Chat Agent with multi-file context
1. The functions interact with other modules in the repo.

2. Use Copilot Chat in the IDE or GitHub UI where it has full project context to update references to renamed functions/variables across files.

3. Observe how suggestions vary based on environment and context availability.


```python
def calcPrice(itm, qtyOrdered):
    price = itm["p"]
    totalPrice = price * qtyOrdered
    return totalPrice

def process(itmList):
    totalCost = 0
    for itm in itmList:
        totalCost += calcPrice(itm, itm["qty"])
    return totalCost

```