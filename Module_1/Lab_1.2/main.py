
# Reorder the functions so that dependencies are defined first.
# Ensure all function names follow the 'verb_noun' snake_case convention.
# Rename 'calculate_total' to 'compute_product_total'


def compute_product_total(price, quantity):
    return price * quantity

def apply_discount(total, discount_percent):
    # Assume discount_percent is between 0 and 1
    return total * (1 - discount_percent)

# Main logic
item_price = 100
item_quantity = 2
discount = 0.1
final_amount = apply_discount(compute_product_total(item_price, item_quantity), discount)
print(f"Final amount: {final_amount}")