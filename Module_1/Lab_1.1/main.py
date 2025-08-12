# In user_management.py, add a function `validate_enterprise_email(email)`
# This function should ensure the email ends with '@yourcompany.com'
# and has at least one period before the '@' symbol.

# Use the ENTERPRISE_DOMAIN from config.py for validation
# The function should return True for valid emails, False otherwise

from config import ENTERPRISE_DOMAIN

def validate_enterprise_email(email):
    # Ensure email ends with ENTERPRISE_DOMAIN
    # Ensure email contains at least one '.' before the '@'
    
    if not email.endswith(f"@{ENTERPRISE_DOMAIN}"):
        return False

    local_part = email.split('@')[0]
    if '.' not in local_part:
        return False

    return True

# Test the function with sample input
if __name__ == "__main__":
    print(validate_enterprise_email("test.user@yourcompany.com"))       # Expected: True
    print(validate_enterprise_email("invalid@gmail.com"))               # Expected: False
    print(validate_enterprise_email("nodot@yourcompany.com"))           # Expected: False
