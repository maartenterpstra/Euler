from fractions import Fraction, gcd
from decimal import Decimal
import math

FracLimit = Fraction(3, 7)
maxFrac = Fraction(0, 1)

maxN = 1
limit = 10**6 + 1

for d in range(1, limit):
    for n in range(maxN, int(math.ceil(d * 3.0 / 7.0)) + 1):
        if gcd(n, d) == 1:
            f = Fraction(n, d)
            if f < FracLimit and f > maxFrac:
                maxFrac = f
                maxN = n
print(maxN)
