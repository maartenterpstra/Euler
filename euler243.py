from fractions import Fraction, gcd
from decimal import Decimal

upperLim = Decimal(Decimal(15499) / Decimal(94744))
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def findUpper(upperLim):
    d, s = 1, 1
    for p in primes:
        d *= p
        s *= (p - 1)
        for i in range(2, p):
            if s * i / (d * i - 1.0) < upperLim:
                return d * i

print(findUpper(upperLim))
