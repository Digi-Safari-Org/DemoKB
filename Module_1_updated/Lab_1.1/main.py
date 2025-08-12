from typing import Any, Dict, List, Optional

def calculate_total(items: List[Dict[str, Any]], discount: float = 0.0) -> float:
    """
    Calculates the total price for a list of items, applying an optional discount.

    Args:
        items (List[Dict[str, Any]]): List of item dictionaries with 'price' and 'qty'.
        discount (float, optional): Discount to subtract from total. Defaults to 0.0.

    Returns:
        float: The final total after discount.
    """
    total = sum(item["price"] * item["qty"] for item in items)
    return total - discount

def process_order(
    data: Dict[str, Any]
) -> str:
    """
    Processes an order and returns a summary string.

    Args:
        data (Dict[str, Any]): Order data with keys:
            - customer_id (str): The customer ID (required).
            - items (List[Dict[str, Any]]): List of items, each with 'name', 'qty', and 'price'.
            - discount (float, optional): Discount to apply to the total.

    Returns:
        str: Summary string listing items and the final total, or an error message if customer_id is missing.
    """
    if not data.get("customer_id"):
        return "Error: Missing customer ID"

    items: List[Dict[str, Any]] = data.get("items", [])
    discount: float = float(data.get("discount", 0.0))

    summary = ""
    for item in items:
        summary += f"{item['name']} x {item['qty']}, "

    total = calculate_total(items, discount)
    return summary + f"Total: ${total:.2f}"

if __name__ == "__main__":
    test_data = {
        "customer_id": "C123",
        "items": [
            {"name": "Widget", "qty": 2, "price": 10.0},
            {"name": "Gadget", "qty": 1, "price": 15.5}
        ],
        "discount": 5.0
    }
    result = process_order(test_data)
    print(result)