import math


def mysqrt(a):
    if (a == 1):
        return 1
    else:
        x = a - 1

    while True:
        
        y = ((x + a / x) / 2)
        print(y)
        break
        if abs(x - y) < 0.001:
            print(y)
            break
        else:
            x = y

    return y


def test_square_root():
    print("{: >20} {: >20} {: >20} {: >20}".format(
        'a', 'mysqrt', 'math.sqrt', 'diff'))
    for i in range(1, 10):
        print("{: >20} {: >20} {: >20} {: >20}".format(
            i, mysqrt(i), math.sqrt(i), mysqrt(i) - math.sqrt(i)))


test_square_root()
