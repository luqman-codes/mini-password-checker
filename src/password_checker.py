def strength(password: str) -> str:
    """
    Returns: 'weak', 'medium', or 'strong'
    Simple rules:
    - weak: length < 6
    - medium: length 6-9
    - strong: length >= 10
    """
    if len(password) < 6:
        return "weak"
    if len(password) < 10:
        return "medium"
    return "strong"
