#  Copilot Prompt Used:
# Write parameterized pytest tests for add, divide, and is_even in math_utils.py.
# Also include exception handling tests for invalid input and use mocking for log_and_add.

import pytest
from unittest.mock import Mock
from math_utils import add, divide, is_even, log_and_add

# ---- Parameterized Tests ----

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (1_000_000, 2_000_000, 3_000_000),
], ids=["positive", "negative", "zeros", "large_numbers"])
def test_add(a, b, expected):
    assert add(a, b) == expected, f"Expected {a} + {b} = {expected}"

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (10, 0, None),
    (-20, 5, -4),
], ids=["normal_division", "divide_by_zero", "negative_division"])
def test_divide_valid(a, b, expected):
    assert divide(a, b) == expected, f"Expected divide({a}, {b}) = {expected}"

@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
], ids=["even", "odd", "zero", "negative_even"])
def test_is_even(n, expected):
    assert is_even(n) == expected

# ---- Exception Handling ----

@pytest.mark.parametrize("a,b", [
    ("10", 2),
    (10, "2"),
    (None, 5),
], ids=["string_a", "string_b", "none_input"])
def test_divide_invalid_types(a, b):
    with pytest.raises(TypeError, match="Operands must be numeric"):
        divide(a, b)

# ---- Mocking Logger ----

def test_log_and_add_with_mock():
    mock_logger = Mock()
    result = log_and_add(3, 4, mock_logger)
    assert result == 7
    mock_logger.log.assert_called_once_with("Adding 3 and 4 = 7")
