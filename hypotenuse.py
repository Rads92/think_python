

def hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5


def is_between(x, y, z):
    return x <= y <= z


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)

    return ack(m - 1, ack(m, n - 1))


def palidrome(word):
    pass


def is_palidrome(word):
    if len(word) == 0:
        return True
    first_letter = word[0]
    last_letter = word[-1]

    return first_letter == last_letter and is_palidrome(word[1:-1])


def is_power(a, b):
    if a == b:
        return True

    if a % b != 0:
        return False

    return is_power(a/b, b)