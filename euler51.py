from bisect import bisect_left


def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):     # Mark factors non-prime
                a[n] = False

# sqrt(1000000000) = 31622
__primes = list(sieve(31622))


def isPrime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit:
            return True
        if n % p == 0:
            return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6):  # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

primeList = (x for x in range(100, 10 ** 6) if isPrime(x))


def testPrimes(testPrimes, searchLen=8):
    for prime in testPrimes:
        primeStr = str(prime)
        uniqueChars = set(list(primeStr))
        for uniqueChar in uniqueChars:
            primeList = []
            for replacementChar in range(ord('0'), ord('9') + 1):
                replaced = int(primeStr.replace(
                    uniqueChar, chr(replacementChar)))
                # second check needed because of trailing zeros
                if isPrime(replaced) and len(str(replaced)) == len(primeStr):
                    primeList.append(replaced)

            if len(primeList) == searchLen:
                print(primeList)
                return min(primeList)
print(testPrimes(primeList))
