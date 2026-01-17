def strength(password: str) -> str:
    """
    Returns: 'weak', 'medium', or 'strong'

    Rules (simple but realistic):
    - weak: length < 6
    - medium: length >= 6 AND (has a digit OR has an uppercase)
    - strong: length >= 10 AND has a digit AND has an uppercase
    """
    if len(password) < 6:
        return "weak"

    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)

    if len(password) >= 10 and has_digit and has_upper:
        return "strong"

    if has_digit or has_upper:
        return "medium"

    return "weak"
