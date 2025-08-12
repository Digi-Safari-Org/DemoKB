def run_payment_flow(username: str, password: str, amount: float, currency: str, customer_id: str):
    """
    Executes a modern payment flow using the ModernPaymentAPI.
    """
    api = ModernPaymentAPI()
    auth_result = api.login(username, password)

    if not auth_result.get("success"):
        print("Authentication failed. Aborting payment.")
        return

    session_id = auth_result["session_id"]

    payment_details = {
        "amount": amount,
        "currency": currency,
        "customer_id": customer_id
    }

    transaction_result = api.execute_payment(session_id, payment_details)
    transaction_info = transaction_result.get("transaction", {})

    if transaction_info.get("status") == "approved":
        print(f"✅ Payment Approved! Transaction ID: {transaction_info.get('id')}")
    else:
        print("❌ Payment Failed or Declined.")


# Example usage
if __name__ == "__main__":
    run_payment_flow("admin", "pass", 100.00, "USD", "C123")
