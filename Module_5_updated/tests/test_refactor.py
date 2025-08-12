# tests/test_refactor.py
import sys
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from legacy.legacy_data_client import legacy_get_item
from refactor.modern_data_client import ModernClientAdapter

def test_refactor_returns_same_flat_dict():
    item_id = 7
    username = "admin"
    password = "password"

    legacy_out = legacy_get_item(item_id, username, password)
    adapter = ModernClientAdapter(username, password)
    modern_out = adapter.get_item(item_id)

    assert legacy_out == modern_out

def test_invalid_login_raises():
    adapter = ModernClientAdapter("bad", "creds")
    try:
        adapter.get_item(1)
        assert False, "expected exception for bad credentials"
    except Exception:
        assert True
