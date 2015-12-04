from math import ceil, log10


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def truncated_right(n):
    l = []
    while n > 10:
        n /= 10
        l.append(n)

    return l


def truncated_left(n):
    l = []
    i = pow(10, ceil(log10(n)) - 1)
    while n % i > 0:
        n %= i
        i /= 10
        l.append(int(n))

    return l

limit = int(1e6)
primes = (x for x in range(11, limit + 1) if isPrime(x))

s = 0
found = 0
for p in primes:
    trunks = truncated_right(p) + truncated_left(p)
    truncable = all(isPrime(h) for h in trunks)

    if truncable:
        found += 1
        s += p
        print(p)

    # it said there are only 11 such primes
    if found == 11:
        break

print("")
print(s)
