# Copilot prompt:
# Create enterprise utility helpers used by multiple services.
# Implement three functions:
# 1) validate_response(data: dict, required_keys=None) -> bool
#    - Return True only if `data` is a dict and contains all required_keys (default ["status","data"])
# 2) extract_data_field(data: dict, field: str)
#    - Support dot-separated paths like "data.item.id". Raise KeyError if path missing.
# 3) format_fetch_payload(item_id: int, options: dict = None) -> dict
#    - Return a payload dict matching shape {"request": {"id": item_id, "options": options or {}}}
# Keep code simple and well-documented.




from typing import Any, Dict, List, Optional

def validate_response(data: dict, required_keys: Optional[List[str]] = None) -> bool:
    """
    Returns True if `data` is a dict and contains all required_keys.
    Default required_keys: ["status", "data"]
    """
    if required_keys is None:
        required_keys = ["status", "data"]
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)

def extract_data_field(data: dict, field: str) -> Any:
    """
    Extracts a nested field from a dict using a dot-separated path.
    Example: extract_data_field({"data": {"item": {"id": 1}}}, "data.item.id") -> 1
    Raises KeyError if any part of the path is missing.
    """
    parts = field.split(".")
    current = data
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            raise KeyError(f"Missing field: {part}")
        current = current[part]
    return current

def format_fetch_payload(item_id: int, options: Optional[Dict] = None) -> Dict:
    """
    Returns a payload dict: {"request": {"id": item_id, "options": options or {}}}
    """
    return {"request": {"id": item_id,
                        "options": options or {}}}