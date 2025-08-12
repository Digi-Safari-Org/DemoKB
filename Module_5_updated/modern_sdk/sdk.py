# Copilot prompt:
# Implement a mock ModernDataSDK class to simulate an upgraded vendor SDK.
# The class should provide:
# - __init__(self)
# - login(self, username: str, password: str) -> str
#     - If username=="admin" and password=="password" return a session string like "SESSION-<timestamp>"
#     - Otherwise raise ValueError("Login failed: invalid credentials")
# - fetch_data(self, payload: dict) -> dict
#     - Expect payload like {"request": {"id": <int>, "options": {...}}}
#     - If payload missing required fields, return {"status": "error", "error": "invalid_payload"}
#     - Otherwise return nested response like:
#         {
#           "status": "ok",
#           "meta": {"timestamp": ...},
#           "data": {
#             "item": {
#               "id": <id>,
#               "attributes": {"name": "Item-<id>", "value": id*10}
#             }
#           }
#         }
# Keep this as a pure-Python mock (no network calls).





import time
from typing import Dict, Any

class ModernDataSDK:
    def __init__(self) -> None:
        pass

    def login(self, username: str, password: str) -> str:
        """
        Simulates authentication. Returns a session string if credentials are correct.
        """
        if username == "admin" and password == "password":
            session = f"SESSION-{int(time.time())}"
            return session
        raise ValueError("Login failed: invalid credentials")

    def fetch_data(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulates fetching data. Expects payload with structure:
        {"request": {"id": <int>, "options": {...}}}
        """
        if (
            not isinstance(payload, dict)
            or "request" not in payload
            or not isinstance(payload["request"], dict)
            or "id" not in payload["request"]
        ):
            return {"status": "error", "error": "invalid_payload"}

        item_id = payload["request"]["id"]
        timestamp = int(time.time())
        return {
            "status": "ok",
            "meta": {"timestamp": timestamp},
            "data": {
                "item": {
                    "id": item_id,
                    "attributes": {
                        "name": f"Item-{item_id}",
                        "value": item_id * 10
                    }
                }
            }
        }