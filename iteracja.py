import math


def mysqrt(a):
    x = a

    while True:
        y = ((x + (a / x)) / 2)
        if abs(x - y) < 0.00001:
            break
        else:
            x = y

    return y


def test_square_root():
    print("{: >2} {: >20} {: >20} {: >25}".format('a', 'mysqrt', 'math.sqrt',
                                                  'diff'))
    for i in range(1, 10):
        result = mysqrt(i)
        print("{: >2} {: >20} {: >20} {: >25}".format(i, result, math.sqrt(i),
                                                      result - math.sqrt(i)))


# test_square_root()
def silnia(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def eval_loop():
    while True:
        a = input('podaj dzialanie \n')
        if a == 'gotowe':
            print('gotowe')
            break

        print(eval(a))


def calculate_skladnik(n):
    return (silnia(4 * n) * (1103 + 26390 * n) / ((silnia(n)**4) * (396**
                                                                    (4 * n))))


def estimate_pi():
    k = (2 * math.sqrt(2)) / 9801
    n = 0
    granica = 10**(-15)
    result = 0

    while True:
        skladnik = calculate_skladnik(n)

        if skladnik < granica:
            break
        else:
            result += skladnik
            n += 1

    return 1 / (k * result)
