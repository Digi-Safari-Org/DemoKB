# legacy_payment_client.py

class LegacyPaymentAPI:
    def authenticate_user(self, username, password):
        print(f"Legacy: Authenticating {username}...")
        if username == "admin" and password == "pass":
            return {"status": "success", "token": "old_token_123"}
        return {"status": "failed"}

    def process_transaction_v1(self, token, amount, currency):
        print(f"Legacy: Processing V1 transaction for {amount} {currency} with token {token}...")
        if token == "old_token_123" and amount > 0:
            return {"status": "completed", "transaction_id": "TXN_LEGACY_456"}
        return {"status": "failed"}


# Legacy client logic
api = LegacyPaymentAPI()
auth_response = api.authenticate_user("admin", "pass")
if auth_response["status"] == "success":
    transaction_response = api.process_transaction_v1(auth_response["token"], 100.00, "USD")
    print(f"Legacy Transaction Result: {transaction_response}")
