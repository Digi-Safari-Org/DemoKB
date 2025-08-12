# TODO: Create a reusable utility module with clean, type-annotated helper functions
# - Each function should include rich docstrings (Args, Returns, Examples)
# - Use type hints for better Copilot indexing and suggestion quality
# - Functions will be reused across multiple files (e.g., main_app.py)
# - Include: format_currency, sanitize_input, convert_to_uppercase
# - Ensure the functions are atomic, testable, and readable

def format_currency(amount: float | str, currency_symbol: str = "$") -> str:
    """
    Formats a numeric amount as a currency string.

    Args:
        amount (float | str): The numeric value to format (int, float, or numeric string).
        currency_symbol (str): The symbol for the currency (default: "$").

    Returns:
        str: The formatted currency string, e.g., "$123.45".

    Example:
        >>> format_currency(99.9)
        '$99.90'
        >>> format_currency("100")
        '$100.00'
    """
    try:
        numeric_amount = float(amount)
    except (TypeError, ValueError):
        raise TypeError("Amount must be a numeric type or numeric string ")

    return f"{currency_symbol}{numeric_amount:.2f}"



def sanitize_input(value: str) -> str:
    """
    Cleans a string by trimming whitespace and removing newlines/tabs.

    Args:
        value (str): Raw user input.

    Returns:
        str: Sanitized string without whitespace, newlines, or tabs.
    """
    return value.strip().replace("\n", "").replace("\t", "")


def convert_to_uppercase(value: str) -> str:
    """
    Converts a string to uppercase.

    Args:
        value (str): Input string.

    Returns:
        str: Uppercased version of the input.
    """
    return value.upper()
