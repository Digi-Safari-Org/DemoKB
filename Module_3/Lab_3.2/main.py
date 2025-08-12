

##  `solution_Lab3.3.py`


# TODO: Fix insecure deserialization vulnerability.
# - Replace pickle with a safe alternative like json.
# - Validate structure of the input data.
# - Ensure malicious payloads cannot execute arbitrary code.
# - Challenge: Use pydantic or voluptuous for schema validation.

import base64
import json
from typing import Any

# Secure replacement function
def process_user_data_secure(encoded_data: str) -> Any:
    """
    Safely processes user-provided base64-encoded data using JSON deserialization.
    """
    try:
        decoded_data = base64.b64decode(encoded_data).decode("utf-8")
        data = json.loads(decoded_data)
        
        if not isinstance(data, dict) or "user" not in data or "role" not in data:
            raise ValueError("Invalid payload structure.")
        if data["role"] not in ["guest", "admin", "editor"]:
            raise ValueError("Invalid role.")
        
        print(f"Safely processed data: {data}")
        return data
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as e:
        print(f"Security Error: {e}")
        return None

#  Example: Malicious Payload (simulated, for testing only – won't work now)
# import pickle, os
# class Exploit:
#     def __reduce__(self):
#         return (os.system, ('echo HACKED!',))
# malicious = Exploit()
# malicious_payload = base64.b64encode(pickle.dumps(malicious)).decode('utf-8')

#  Now this malicious payload will fail as JSON can't deserialize it

#  Benign Payload Example
import base64
benign_data = {"user": "alice", "role": "guest"}
benign_payload = base64.b64encode(json.dumps(benign_data).encode("utf-8")).decode("utf-8")

# Run test
if __name__ == "__main__":
    print("Benign Test:")
    process_user_data_secure(benign_payload)

    print("\nSimulated Malicious Test:")
    # Simulated attack – this input will be invalid due to json decoding
    fake_attack = base64.b64encode(b"rm -rf /").decode("utf-8")
    process_user_data_secure(fake_attack)
