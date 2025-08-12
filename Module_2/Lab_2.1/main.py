# TODO: Refactor the process_user_data function to follow enterprise coding standards.
# - Break it into smaller helper functions: email validation, user ID generation, logging, etc.
# - Replace all print/logging with a reusable log_message() function.
# - Ensure logs follow the format: [APP_NAME] - [MODULE_NAME] - message.
# - Include test cases in __main__ to verify all behaviors: add, update, and unknown operations.
# - All helper functions must be reusable and cleanly separated for clarity and reuse.

import logging

# Logging setup
APP_NAME = "MyApp"
MODULE_NAME = "DataProcessor"

logging.basicConfig(level=logging.INFO)

def log_message(message, level="info"):
    formatted = f"[{APP_NAME}] - [{MODULE_NAME}] - {message}"
    if level == "info":
        logging.info(formatted)
    elif level == "warning":
        logging.warning(formatted)
    else:
        logging.debug(formatted)

# Helper function to validate email
def is_valid_email(email):
    return "@" in email

# Helper function to generate user ID
def generate_user_id(email):
    return f"user_{hash(email)}"

# Add user function
def add_user(user_info):
    if not is_valid_email(user_info.get('email', '')):
        log_message("Invalid email format.", level="warning")
        return False

    user_info['user_id'] = generate_user_id(user_info['email'])
    log_message(f"Adding user {user_info['name']} with ID {user_info['user_id']} to DB.")
    return True

# Update user function
def update_user(user_info):
    user_info['last_login'] = "2025-07-01"
    log_message(f"Updating last login for user {user_info['name']}.")
    return True

# Main function refactored
def process_user_data(user_info, operation_type):
    if operation_type == "add":
        return add_user(user_info)
    elif operation_type == "update":
        return update_user(user_info)
    else:
        log_message("Unknown operation type.", level="warning")
        return False

# Additional functions to test log standardization
def perform_calculation(a, b):
    log_message("Starting calculation.")
    result = a + b
    log_message(f"Calculation complete: {result}")
    return result

def fetch_data(url):
    log_message(f"Failed to fetch data from {url}", level="warning")
    return None

# Testing the functions
if __name__ == "__main__":
    user = {"name": "Alice", "email": "alice@example.com"}

    process_user_data(user, "add")
    process_user_data(user, "update")
    process_user_data(user, "delete")  # Invalid operation

    perform_calculation(10, 5)
    fetch_data("https://example.com/api")
