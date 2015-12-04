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

primeList = [x for x in __primes if x < 9000]


# --------------------------------------
# Check if it is concatenatable into prime
# --------------------------------------
def isConcatPrime(p1, p2):
    if isPrime(int(str(p1) + str(p2))) and isPrime(int(str(p2) + str(p1))):
        return True
    return False

# --------------------------------------
# Generate Prime set
# --------------------------------------
primeSet = {}


def generatePrimeSet():
    for i in range(len(primeList)):
        concatSet = set()
        for j in range(i + 1, len(primeList)):
            if isConcatPrime(primeList[i], primeList[j]):
                concatSet.add(primeList[j])
        primeSet[primeList[i]] = concatSet

# --------------------------------------
# Continuous Intersection
# --------------------------------------


def continuousIntersection(path, intersect, depth, minSum=2147483647):
    if depth == 0:
        return sum(path)
    else:
        for p in intersect:
            s = continuousIntersection(
                path + [p], intersect & primeSet[p], depth - 1, minSum)
            minSum = min(s, minSum)
    return minSum

# --------------------------------------
# Glue all the pieces together
# --------------------------------------
generatePrimeSet()
minSum = 2147483647  # 2^31 - 1
for key in primeSet:
    minSum = min(minSum, continuousIntersection([key], primeSet[key], 4))
print(minSum)
