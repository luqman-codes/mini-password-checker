from src.password_checker import strength

def test_strength():
    # weak: too short
    assert strength("abc") == "weak"

    # weak: long enough but no digit/uppercase
    assert strength("abcdefgh") == "weak"

    # medium: length ok + digit
    assert strength("abcd1234") == "medium"

    # medium: length ok + uppercase
    assert strength("Abcdefgh") == "medium"

    # strong: length >= 10 + digit + uppercase
    assert strength("Abcdef12345") == "strong"
