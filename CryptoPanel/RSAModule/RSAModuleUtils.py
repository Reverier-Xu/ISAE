def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def inverse(a, b):
    return egcd(a, b)[1] % b
