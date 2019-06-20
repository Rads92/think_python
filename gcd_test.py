from gcd import gcd


def test_gcd_42_56():
    assert gcd(42, 56) == 14
def test_gcd_18_84():
    assert gcd(18, 84) == 6
def test_gcd_48_180():
    assert gcd(48, 180) == 12
def test_gcd_192_348():
    assert gcd(192, 348) == 12