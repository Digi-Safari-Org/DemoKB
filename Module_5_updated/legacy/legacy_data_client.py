# legacy/legacy_data_client.py
import time

def legacy_authenticate(username: str, password: str) -> str:
    if username == "admin" and password == "password":
        return f"LEGACY-TOKEN-{int(time.time())}"
    raise ValueError("Invalid credentials for legacy auth")

def legacy_fetch_data(item_id: int) -> dict:
    return {
        "id": item_id,
        "name": f"Item-{item_id}",
        "value": item_id * 10,
    }

def legacy_get_item(item_id: int, username: str, password: str) -> dict:
    token = legacy_authenticate(username, password)
    print("Using token:", token)

    raw = legacy_fetch_data(item_id)
    if "id" not in raw or "name" not in raw:
        raise KeyError("Missing fields in legacy fetch response")

    result = {
        "id": raw["id"],
        "name": raw["name"],
        "value": raw.get("value", 0),
    }
    return result

if __name__ == "__main__":
    print(legacy_get_item(3, "admin", "password"))
