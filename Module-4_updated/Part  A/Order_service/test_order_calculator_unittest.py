
# Create a unittest-based test file for calculate_discount and calculate_tax.

# 1. Import:
#    import unittest
#    from order_calculator import calculate_discount, calculate_tax
#    from test_data import REGRESSION_INPUTS

# 2. Create a TestCase subclass:
#    - test_discount_calculation_unittest → test discount logic
#    - test_tax_calculation_unittest → test tax logic
#    - test_regression_cases → iterate over REGRESSION_INPUTS and assert final taxed price matches expected.

# Run with:
# python -m unittest discover -s order_service -p "test_order_calculator_unittest.py"

# order_service/test_order_calculator_unittest.py
import unittest
from order_calculator import calculate_discount, calculate_tax
from test_data import (
  
    REGRESSION_CASES
)



class TestOrderCalculator(unittest.TestCase):

    def test_regression_cases(self):
        for case in REGRESSION_CASES:
            discounted = calculate_discount(case["price"], case["discount"] * 100)
            taxed = calculate_tax(discounted, case["tax_rate"] * 100)
            self.assertAlmostEqual(taxed, case["expected"], places=2)

if __name__ == "__main__":
    unittest.main()
