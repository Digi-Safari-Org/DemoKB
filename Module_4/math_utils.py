def add(a, b):
    return a + b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numeric.")
    return a / b if b != 0 else None

def is_even(n):
    return n % 2 == 0

def log_and_add(a, b, logger):
    result = add(a, b)
    logger.log(f"Adding {a} and {b} = {result}")
    return result
