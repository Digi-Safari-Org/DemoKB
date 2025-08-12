# api_service/test_data_api.py
"""
Shared payloads for the /calculate endpoint tests.
Each tuple: (a, b, expected_result)
"""

PYTEST_PAYLOADS = [
    (1, 2, 3),
    (10, 5, 15),
    (-1, 1, 0),
    (0, 0, 0),
]

UNITTEST_PAYLOADS = [
    (2, 3, 5),
    (100, -20, 80),
    (7, 8, 15),
]
