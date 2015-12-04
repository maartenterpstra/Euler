def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def getNthPrime(n):
    # we've already counted 2 for simplicity so we only
    # have to search half the numbers
    primeCount = 1
    subject = 3
    while True:
        if isPrime(subject):
            primeCount = primeCount + 1
            if primeCount == n:
                return subject
        subject += 2

print getNthPrime(100001)
