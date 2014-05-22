from fractions import Fraction, gcd
from decimal import Decimal
from operator import mul 
from bisect import bisect_left

def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
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
		if p > limit: return True
		if n % p == 0: return False
	# fall back on trial division if n > 1 billion
	for f in range(31627, limit, 6): # 31627 is the next prime
		if n % f == 0 or n % (f + 4) == 0:
			return False
	return True

def factorize(n):
    for prime in __primes:
        if prime > n: return
        exponent = 0
        while n % prime == 0:
            exponent, n = exponent + 1, n / prime
        if exponent != 0:
            yield prime, exponent


def totient(n):
	return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in factorize(n)), 1)


limit = 10**6
phi = range(0, limit + 1)
count = 0
for d in range(2, limit + 1):
	if phi[d] == d:
		for j in range(d, limit + 1, d):
			phi[j] = phi[j] / d * (d - 1)
	count += phi[d]
	
print count