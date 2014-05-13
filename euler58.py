from decimal import Decimal
import threading


def isPrime(n):
	if n < 2: return False
	if n == 2: return True
	if not n & 1: return False

	limit = int(n**0.5) + 1
	for i in xrange(3, limit, 2):
		if n % i == 0:
			return False

	return True

n = 1
primes = 0
score = Decimal(1)

while score > Decimal(0.1):
	n += 2
	primes += len(filter(lambda n: isPrime(n), [n*n, n*n - n + 1, n*n - 2*n + 2, n*n - 3*n + 3]))
	numsOnDiagonals = 2*n - 1
	score = Decimal(primes)/Decimal(numsOnDiagonals)

print n, score