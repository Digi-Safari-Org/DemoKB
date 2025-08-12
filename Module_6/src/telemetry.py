
# Explain the selected function as documentation for a project wiki. Provide:
# - Short summary
# - Purpose
# - Inputs (types and example)
# - Outputs (types and example)
# - Example call with expected output
# - Complexity and edge cases / gotchas
# Format as markdown suitable to save in docs/FunctionReference.md.

# Copilot: add a detailed docstring describing telemetry use, what fields are sent,
# how to redact PII, environment variables to disable telemetry, and security approval process


import json
import os

def log_data(data):
    """
    Send telemetry for an order.

    Behavior:
    - Serializes `data` to JSON and sends to the telemetry sink (currently printed).
    - This function MUST NOT send PII or sensitive fields (name, email, ssn). Redact these fields before calling.
    - To disable telemetry entirely, set environment variable `DISABLE_TELEMETRY=1`.
    - Telemetry endpoint and credentials must be approved and stored in secure config (do not hardcode).
    - Retention: telemetry should follow org retention policy; do not store raw PII.

    Parameters
    ----------
    data : dict
        Dictionary containing order information. Expected keys: `id` (int), `amount` (number), etc.

    Security
    --------
    - Any change to telemetry behavior requires Security review and PR approval.
    """
    if os.getenv("DISABLE_TELEMETRY", "0") == "1":
        return
    # Minimal redaction example (remove 'customer_name' if present)
    safe_data = dict(data)
    for key in ["customer_name", "email", "ssn"]:
        if key in safe_data:
            safe_data[key] = "<REDACTED>"
    payload = json.dumps(safe_data)
    print(f"Sending telemetry: {payload}")
