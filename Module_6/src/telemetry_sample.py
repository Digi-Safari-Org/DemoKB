import json

def log_data(data):
    # Sends order data to an external telemetry service
    payload = json.dumps(data)
    print(f"Sending telemetry: {payload}")
