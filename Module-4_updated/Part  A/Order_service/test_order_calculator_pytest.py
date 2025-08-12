# Write a pytest test file to test calculate_discount and calculate_tax from order_calculator.py.

# 1. Import:
#    from order_calculator import calculate_discount, calculate_tax
#    from test_data import PRODUCTS, PYTEST_PARAMETERS, INTEGRATION_SCENARIOS, REGRESSION_INPUTS

# 2. Create:
#    - test_discount_calculation_pytest() → assert discounts are applied correctly.
#    - test_tax_calculation_pytest() → assert tax is applied correctly.

# 3. Use @pytest.mark.parametrize for:
#    - test_cart_final_price_pytest(items, discount, expected_total) from PYTEST_PARAMETERS
#    - test_cart_final_price_integration(cart_items, discount, expected_total) from INTEGRATION_SCENARIOS

# 4. Add a regression test class:
#    - class TestOrderCalculatorRegression:
#        def test_regression_cases(self):
#            Loop over REGRESSION_INPUTS and assert final taxed price is correct.


import pytest
import unittest
from order_calculator import calculate_discount, calculate_tax, final_price
from test_data import (
    PRODUCTS,
    PYTEST_PARAMETERS,
    INTEGRATION_SCENARIOS,
    REGRESSION_CASES
)



# --------- PyTest Parameterized Unit Tests ---------

@pytest.mark.parametrize("product", PRODUCTS)
def test_calculate_tax_unit(product):
    price = product["price"]
    tax_rate = product["tax_rate"] * 100  # convert to percent
    expected = price + (price * product["tax_rate"])
    assert calculate_tax(price, tax_rate) == pytest.approx(expected)

@pytest.mark.parametrize("product", PRODUCTS)
def test_calculate_discount_unit(product):
    price = product["price"]
    discount = 10  # 10% discount for test
    expected = price - (price * discount / 100)
    assert calculate_discount(price, discount) == pytest.approx(expected)

# --------- PyTest Parameterized Integration Tests ---------

@pytest.mark.parametrize("items, discount, expected_total", PYTEST_PARAMETERS)
def test_cart_final_price_pytest(items, discount, expected_total):
    # items: list of (price, tax_rate)
    total = 0.0
    for price, tax_rate in items:
        discounted = calculate_discount(price, discount * 100)  # discount as percent
        total += calculate_tax(discounted, tax_rate * 100)
    assert total == pytest.approx(expected_total)

@pytest.mark.parametrize("cart_items, discount, expected_total", INTEGRATION_SCENARIOS)
def test_cart_final_price_integration(cart_items, discount, expected_total):
    total = 0.0
    for item in cart_items:
        discounted = calculate_discount(item["price"], discount * 100)
        total += calculate_tax(discounted, item["tax_rate"] * 100)
    assert total == pytest.approx(expected_total)

# --------- unittest Regression Tests ---------

class TestOrderCalculatorRegression(unittest.TestCase):
  def test_regression_cases(self):
    for case in REGRESSION_CASES:
        discounted = calculate_discount(case["price"], case["discount"] * 100)
        taxed = calculate_tax(discounted, case["tax_rate"] * 100)
        self.assertAlmostEqual(taxed, case["expected"], places=2)

