

def gcd(a, b):
    if b == 0:
        return a

    else:
        reminder = a % b
        return gcd(b, reminder)
