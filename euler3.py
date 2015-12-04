def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def listPrimes(upper):
    return [x for x in range(2, upper + 1) if isPrime(x)]


def getPrimeFactor(n):
    return max([x for x in range(2, int(n**0.5) + 1) if n %
                x == 0 and isPrime(x)])

print(getPrimeFactor(600851475143))
