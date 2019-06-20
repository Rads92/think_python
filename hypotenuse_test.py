from hypotenuse import (
    hypotenuse,
    is_between,
    factorial,
    fibonacci,
    ack,
    is_palidrome,
    is_power
)


def test_hypotenuse():
    assert hypotenuse(4, 3) == 5


def test_is_between_false():
    assert is_between(1, -2, 4) == False


def test_is_between_true():
    assert is_between(1, 2, 4) == True


def test_factorial_3():
    assert factorial(3) == 6


def test_factorial_0():
    assert factorial(0) == 1


def test_factorial_1():
    assert factorial(1) == 1


def test_fibonacci_0():
    assert fibonacci(0) == 0


def test_fibonacci_1():
    assert fibonacci(1) == 1


def test_fibonacci_2():
    assert fibonacci(2) == 1


def test_fibonacci_3():
    assert fibonacci(3) == 2


def test_fibonacci_4():
    assert fibonacci(4) == 3


def test_fibonacci_5():
    assert fibonacci(5) == 5


def test_fibonacci_6():
    assert fibonacci(6) == 8


def test_fibonacci_7():
    assert fibonacci(7) == 13


def test_ack_m_0_n_0():
    assert ack(0, 0) == 1


def test_ack_m_0_n_1():
    assert ack(0, 1) == 2


def test_ack_m_1_n_0():
    assert ack(1, 0) == 2


def test_ack_m_2_n_0():
    assert ack(2, 0) == 3


def test_ack_m_3_n_4():
    assert ack(3, 4) == 125


def test_is_palidrome():
    words = ['redivider', 'sos', 'bob', 'otto']

    for word in words:
        assert is_palidrome(word) == True


def test_empty_string():
    assert(is_palidrome('')) == True


def test_not_palidrome():
    assert(is_palidrome('radek')) == False


def test_is_power_81():
    assert(is_power(81,3)) == True

def test_is_power_64():
    assert(is_power(64,4)) == True
def test_is_power_60():
    assert(is_power(60,4)) == False