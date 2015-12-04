from decimal import Decimal
from math import ceil, log


def isqrt(n):
    res = 0
    # smallest power of 4 >= the argument
    bit = 4**int(ceil(log(n, 4))) if n else 0
    while bit:
        if n >= res + bit:
            n -= res + bit
            res = (res >> 1) + bit
        else:
            res >>= 1
        bit >>= 2
    return res


def findLength(n):
    count = 1
    m0 = 0
    d0 = 1
    a0 = int(n ** 0.5)

    mi = d0 * a0 - m0
    di = (n - mi * mi) / d0
    ai = int((a0 + mi) / di)
    while ai != 2 * a0:
        count += 1
        mi = di * ai - mi
        di = (n - mi * mi) / di
        ai = int((a0 + mi) / di)

    return count

count = 0
limit = 10000
items = (i for i in range(2, limit + 1) if isqrt(i) ** 2 != i)
print("Generated items")
for i in items:
    if findLength(i) & 1:
        count += 1

print(count)
