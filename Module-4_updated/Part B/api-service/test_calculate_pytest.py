# Copilot: generate a pytest file test_calculate_pytest.py that:
# - imports post_calculate from api_helpers
# - imports PYTEST_PAYLOADS from test_data_api
# - uses @pytest.mark.parametrize to test multiple payloads
# - uses Arrange-Act-Assert in docstrings (Google-style)
# - asserts response.status_code == 200 and json()['result'] matches expected



import pytest
from api_helpers import post_calculate
from test_data_api import PYTEST_PAYLOADS
from api_helpers import get_calculate
from api_helpers import delete_calculate

@pytest.mark.parametrize("a, b, expected", PYTEST_PAYLOADS)
def test_post_calculate(a, b, expected):
    """Test /calculate API with various payloads.

    Arrange:
        Prepare input values a and b.
    Act:
        Send POST request using post_calculate(a, b).
    Assert:
        Response status code is 200 and result matches expected.
    """
    response = post_calculate(a, b)
    assert response.status_code == 200
    assert response.json().get("result") == expected
   

