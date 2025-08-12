from telemetry import log_data


def process_orders(orders):
    processed = []
    for order in orders:
        # no explanation what this does
        if order.get("amount") > 1000:
            order["priority"] = True
            log_data(order)  # telemetry logging
        processed.append(order)
    return processed


if __name__ == "__main__":
    sample_orders = [
        {"id": 1, "amount": 500},
        {"id": 2, "amount": 2000},
        {"id": 3, "amount": 1500}
    ]
    results = process_orders(sample_orders)
    print(results)
