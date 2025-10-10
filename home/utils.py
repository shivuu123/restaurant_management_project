import re

def calculate_total_price(order_items):
    if not order_items:
        return 0.0
    return round(sum(item.get('quatity', 0) * item.get('price', 0) for item in order_items), 2)

def is_valid_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.
    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(email_regex, email))
