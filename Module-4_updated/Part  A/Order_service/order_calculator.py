def calculate_discount(price, discount_percentage):
    return price - (price * discount_percentage / 100)

def calculate_tax(price, tax_rate):
    return price + (price * tax_rate / 100)

def final_price(price, discount_percentage, tax_rate):
    discounted = calculate_discount(price, discount_percentage)
    return calculate_tax(discounted, tax_rate)