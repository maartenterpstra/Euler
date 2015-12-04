from decimal import *


def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif not (n & 1):
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2

    return True

maxLen = -1
maxNum = -1
limit = 1000

for i in [x for x in xrange(2, limit + 1) if isPrime(x)][::-1]:
    if maxLen > i:
        break
    found = [0] * i
    val = 1
    pos = 0
    while found[val] == 0 and not(val == 0):
        found[val] = pos
        val = (val * 10) % i
        pos = pos + 1

    length = pos - found[val]
    if length > maxLen:
        maxLen = length
        maxNum = i

print maxNum, maxLen
