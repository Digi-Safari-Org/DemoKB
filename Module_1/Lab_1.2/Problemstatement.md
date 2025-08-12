##  Lab 1.2: Prompts for Code Reordering and Naming Conventions

####  Objective:

- Utilize GitHub Copilot to reorder code blocks and suggest names that align with standard enterprise naming conventions.

####  Instructions:

1. Start with the following Python code where the functions are not ordered logically:
    
    ```python
    def calculate_total(price, quantity):
        return price * quantity

    def apply_discount(total, discount_percent):
        # Assume discount_percent is between 0 and 1
        return total * (1 - discount_percent)

    # Main logic
    item_price = 100
    item_quantity = 2
    discount = 0.1
    final_amount = apply_discount(calculate_total(item_price, item_quantity), discount)
    print(f"Final amount: {final_amount}")
    ```

2. Add a prompt to guide Copilot in reordering the functions so that helper or dependency functions are defined before the functions that use them.

3. Add a prompt to guide Copilot to apply enterprise naming conventions to all function names.

4. Observe the changes suggested by Copilot and modify them if necessary to match expected standards.

5. Run the updated script to verify that the reordering and naming updates work as intended.
