# main_app.py

# I have a product name and price:
# name = "   deluxe Chair\n"
# price = 129.95

# Format the product name and price using helpers from utils.py
# - sanitize the name
# - convert it to uppercase
# - format the price with a currency symbol

from utils import sanitize_input, convert_to_uppercase, format_currency

def display_product(name: str, price: float) -> str:
    clean_name = convert_to_uppercase(sanitize_input(name))
    formatted_price = format_currency(price)
    return f"{clean_name} - {formatted_price}"

# ✅ Tests
if __name__ == "__main__":
    assert display_product("   deluxe Chair\n", 129.95) == "DELUXE CHAIR - $129.95"
    assert sanitize_input(" \tLaptop\n") == "Laptop"
    assert convert_to_uppercase("chair") == "CHAIR"
    
    try:
        format_currency("invalid")
    except Exception as e:
        print("[Expected Error]", e)
