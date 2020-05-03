__AUTHOR__ = 'JayxV'

from functools import reduce
import random
import gmpy2


def d2s(d):
    s = hex(d)[2:]
    if len(s) % 2 != 0:
        s += '0' + s

    flag = ""
    for i in range(0, len(s), 2):
        flag += chr(int(s[i:i + 2], 16))
    return flag


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def inverse(a, b):
    return egcd(a, b)[1] % b


def mapx(x, n):
    x = (pow(x, n - 1, n) + 3) % n
    return x


def rsa_rabin(c, p, q):
    n = p * q
    c_p = pow(c, (p + 1) / 4, p)
    c_q = pow(c, (q + 1) / 4, q)
    a = inverse(p, q)
    b = inverse(q, p)
    x = (b * q * c_p + a * p * c_q) % n
    y = (b * q * c_p - a * p * c_q) % n

    return d2s(x), d2s(n - x), d2s(y), d2s(n - y)


def rsa_p(n, e, c):  # Pollard's rho algorithm
    x1 = x2 = 1
    while True:
        x1 = mapx(x1, n)
        x2 = mapx(mapx(x2, n), n)
        p = gcd(x1 - x2, n)
        if p == n:
            return "fail"
        elif p != 1:
            q = n / p
            d = inverse(e, (p - 1) * (q - 1))
            m = pow(c, d, n)
            return d2s(m)


def rsa_dpdq(c, p, q, dp, dq):  # reveal dp&dq
    mp = pow(c, dp, p)
    mq = pow(c, dq, q)
    inv_p = inverse(p, q)
    inv_q = inverse(q, p)
    try:
        m = (mp * p * inv_p + mq * q * inv_q) % (p * q)
        return d2s(m)
    except BaseException:
        m = (((mp - mq) * inv_q) % p) * q + mq
        d2s(m)


def rsa_dp(n, e, c, dp):  # reveal dp
    for i in range(1, e):
        if (dp * e - 1) % i == 0:
            if n % (((dp * e - 1) / i) + 1) == 0:
                p = ((dp * e - 1) / i) + 1
                q = n / (((dp * e - 1) / i) + 1)
                phi = (p - 1) * (q - 1)
                d = inverse(e, phi)
                m = pow(c, d, n)
                return d2s(m)


def rsa_n(n, e1, e2, c1, c2):  # use the same module
    s = egcd(e1, e2)
    s1 = s[1]
    s2 = s[2]

    if s1 < 0:
        s1 = - s1
        c1 = inverse(c1, n)
    elif s2 < 0:
        s2 = - s2
        c2 = inverse(c2, n)

    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return d2s(m)


def CRT(mi, ai):
    M = reduce(lambda x, y: x * y, mi)
    ai_ti_mi = [a * (M / m) * inverse(M / m, m) for (m, a) in zip(mi, ai)]
    return d2s(reduce(lambda x, y: x + y, ai_ti_mi) % M)


def rsa_broad(n, e, c):
    m = gmpy2.iroot(int(CRT(n, c)), int(e))[0]
    return d2s(m)


def getpq(c, n, e, d):
    p = 1
    q = 1
    while p == 1 and q == 1:
        k = d * e - 1
        g = random.randint(0, n)
        while p == 1 and q == 1 and k % 2 == 0:
            k /= 2
            y = pow(g, k, n)
            if y != 1 and gcd(y - 1, n) > 1:
                p = gcd(y - 1, n)
                q = n / p

    return p, q
