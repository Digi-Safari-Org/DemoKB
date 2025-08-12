# Copilot: create a unittest file test_calculate_unittest.py that:
# - imports unittest and post_calculate from api_helpers
# - imports UNITTEST_PAYLOADS from test_data_api
# - defines class TestCalculateEndpoint(unittest.TestCase)
# - implements test_calculate_cases that loops payloads and uses subTest to assert response



import unittest
from api_helpers import post_calculate
from test_data_api import UNITTEST_PAYLOADS

class TestCalculateEndpoint(unittest.TestCase):
    def test_calculate_cases(self):
        """
        Test /calculate API with various payloads using subTest.
        """
        for a, b, expected in UNITTEST_PAYLOADS:
            with self.subTest(a=a, b=b, expected=expected):
                response = post_calculate(a, b)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json().get("result"), expected)

if __name__ == "__main__":
    unittest.main()