from src.password_checker import strength

def test_strength():
    assert strength("123") == "weak"
    assert strength("123456") == "medium"
    assert strength("1234567890") == "strong"
