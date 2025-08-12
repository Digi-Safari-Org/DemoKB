
# Copilot: create a small helper module api_helpers.py with a function post_calculate(a, b)
# - Use requests to POST JSON {"a": a, "b": b} to BASE_URL/env API_BASE_URL (default http://127.0.0.1:5000)
# - Return the requests.Response object
# - Include a short Google-style docstring

import os
import requests

BASE_URL = os.environ.get("API_BASE_URL", "http://127.0.0.1:5000")

def post_calculate(a: int, b: int) -> requests.Response:
    """
    Sends a POST request to the /calculate endpoint with integers a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        requests.Response: The HTTP response object from the API.
    """
    url = f"{BASE_URL}/calculate"
    payload = {"a": a, "b": b}
    response = requests.post(url, json=payload)
    return response