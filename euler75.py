from fractions import gcd
from math import sqrt


def ExactlyOneRightSidedTriangle(limit=1500000):
    iters = int(sqrt(limit / 2))
    sums = [0] * (limit + 1)
    count = 0
    for m in range(2, iters):
        for n in range(1, m):
            if ((m - n) & 1) and gcd(m, n) == 1:
                a = (m * m - n * n)
                b = 2 * m * n
                c = (m * m + n * n)
                s = a + b + c
                while s <= limit:
                    sums[s] += 1
                    if sums[s] == 1:
                        count += 1
                    if sums[s] == 2:
                        count -= 1
                    s += a + b + c

    return count

print(ExactlyOneRightSidedTriangle())
