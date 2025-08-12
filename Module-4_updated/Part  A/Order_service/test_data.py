PRODUCTS = [
    {"name": "Laptop", "price": 1000.0, "tax_rate": 0.18},
    {"name": "Smartphone", "price": 500.0, "tax_rate": 0.12},
    {"name": "Tablet", "price": 300.0, "tax_rate": 0.1}
]

# These match the code's math (discount first, then tax)
PYTEST_PARAMETERS = [
    ([(1000, 0.18), (500, 0.12)], 0.1, 1566.0),
    ([(300, 0.1)], 0.2, 264.0),
    ([(500, 0.12), (150, 0.1)], 0.05, 688.75)
]

INTEGRATION_SCENARIOS = [
    ([PRODUCTS[0], PRODUCTS[1]], 0.05, 1653.0),
    ([PRODUCTS[2]], 0.1, 297.0)
]

REGRESSION_CASES = [
    {"price": 1000, "discount": 0.1, "tax_rate": 0.18, "expected": 1062.0},
    {"price": 500, "discount": 0.05, "tax_rate": 0.12, "expected": 532.0}
]
