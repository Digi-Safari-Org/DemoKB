
# Copilot prompt:
# Create ModernClientAdapter that wraps ModernDataSDK and uses enterprise_utils helpers.
# Requirements:
# - constructor: __init__(self, username: str, password: str) -> None
# - login(self) -> str : calls ModernDataSDK.login, stores session, logs info
# - get_item(self, item_id: int, options: dict=None) -> dict
#     - ensure logged in (call login() if no session)
#     - build payload via enterprise_utils.format_fetch_payload
#     - call sdk.fetch_data(payload)
#     - validate response using enterprise_utils.validate_response
#     - extract id/name/value via enterprise_utils.extract_data_field and map back to flat dict:
#         {"id": id, "name": name, "value": value}
# - add robust logging (use Python logging module) and raise helpful exceptions on failure
# The goal: when tests call ModernClientAdapter.get_item(item_id) it should return identical flat dict as legacy_get_item.

import logging
from typing import Optional, Dict, Any
from modern_sdk.sdk import ModernDataSDK
from enterprise_utils.helpers import (
    format_fetch_payload,
    validate_response,
    extract_data_field,
)

logger = logging.getLogger("enterprise.modern_client_adapter")

class ModernClientAdapter:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self._session: Optional[str] = None
        self._sdk = ModernDataSDK()

    def login(self) -> str:
        try:
            self._session = self._sdk.login(self.username, self.password)
            logger.info("Login successful. Session: %s", self._session)
            return self._session
        except Exception as e:
            logger.error("Login failed: %s", e)
            raise RuntimeError(f"ModernClientAdapter login failed: {e}")

    def get_item(self, item_id: int, options: Optional[Dict] = None) -> Dict[str, Any]:
        # Ensure logged in
        if not self._session:
            self.login()
        payload = format_fetch_payload(item_id, options)
        try:
            response = self._sdk.fetch_data(payload)
            if not validate_response(response):
                logger.error("Invalid response structure: %s", response)
                raise ValueError("Invalid response from ModernDataSDK")
            item_id_val = extract_data_field(response, "data.item.id")
            name = extract_data_field(response, "data.item.attributes.name")
            value = extract_data_field(response, "data.item.attributes.value")
            logger.info("Fetched item: id=%s, name=%s, value=%s", item_id_val, name, value)
            return {"id": item_id_val, "name": name, "value": value}
        except Exception as e:
            logger.error("Failed to fetch item %s: %s", item_id, e)
            raise RuntimeError(f"ModernClientAdapter get_item failed: {e}")