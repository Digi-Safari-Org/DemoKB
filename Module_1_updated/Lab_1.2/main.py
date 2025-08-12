# Write Python functions to calculate the total price of an order given a list of items.

# 1. Define a function `calculate_item_total_price` that:
#    - Takes an `item` dictionary with a `'price'` key (float) and a `quantity_ordered` (int).
#    - Returns the total price for that item as `price * quantity_ordered`.
#    - Include a PEP-257 compliant docstring describing parameters and return type.
#    - Use Python 3 type annotations.

# 2. Define a function `calculate_order_total` that:
#    - Takes a list of item dictionaries, each containing `'price'` (float) and `'quantity'` (int).
#    - Uses `calculate_item_total_price` to sum the total cost for all items.
#    - Include a proper docstring and type annotations.

# 3. At the bottom, add a `__main__` block with sample data:
#    - Create a list of sample items with prices and quantities.
#    - Print the total order price formatted to two decimal places.

# Make sure variable and function names follow Python snake_case naming conventions and the code is clean and readable.




def calculate_item_total_price(item: dict, quantity_ordered: int) -> float:
    """
    Calculate the total price for a single item based on its price and quantity ordered.

    Args:
        item (dict): A dictionary containing at least the key 'price' (float).
        quantity_ordered (int): The number of units ordered.

    Returns:
        float: The total price for the item.
    """
    price: float = item["price"]
    return price * quantity_ordered

def calculate_order_total(items: list[dict]) -> float:
    """
    Calculate the total price for an order given a list of items.

    Args:
        items (list of dict): Each dict contains 'price' (float) and 'quantity' (int).

    Returns:
        float: The total price for the entire order.
    """
    total: float = 0.0
    for item in items:
        total += calculate_item_total_price(item, item["quantity"])
    return total

if __name__ == "__main__":
    sample_items = [
        {"price": 19.99, "quantity": 2},
        {"price": 5.49, "quantity": 5},
        {"price": 3.50, "quantity": 1}
    ]
    total_price = calculate_order_total(sample_items)
    print(f"Total order price: ${total_price:.2f}")