#  Reorder the function definitions so that helper functions appear before their usage in compute_final_amount.
#  Rename all functions to follow enterprise naming: verb_noun, lowercase, snake_case.
#  Standardize all variable names using snake_case and clear semantics.
#  Add validation to ensure discount_percentage is within 0–1 range or convert percentages over 1.


def compute_total_price(quantity, price_per_unit):
    return quantity * price_per_unit

def apply_discount(total_price, discount_percentage):
    # Normalize percentage values > 1 (e.g., 15 → 0.15)
    if discount_percentage > 1:
        discount_percentage = discount_percentage / 100
    return total_price * (1 - discount_percentage)

def compute_final_amount(unit_price, quantity, discount_percentage):
    gross_total = compute_total_price(quantity, unit_price)
    final_total = apply_discount(gross_total, discount_percentage)
    return final_total

# ✅ Main Logic
if __name__ == "__main__":
    quantity_ordered = 3
    unit_price = 99.99
    discount_rate = 15  # Can be 15 or 0.15
    final_price_after_discount = compute_final_amount(unit_price, quantity_ordered, discount_rate)
    print(f"Final price after discount: {final_price_after_discount:.2f}")
