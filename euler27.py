def isPrime(n):
	if n < 2: 
		return False
	elif n == 2:
		return True
	elif not (n & 1):
		return False

	i = 3
	while i*i <= n:
		if n % i == 0:
			return False
		i = i + 2

	return True

maxPrimes = 0
maxProd = 0
maxA = 0
maxB = 0
limits = 1000

l = [x for x in xrange(1-limits, limits) if isPrime(abs(x))]
for a in l:
	for b in l:
		n = 0
		primeCount = 0

		while isPrime(n*n + a*n + b):
			n = n + 1
			primeCount = primeCount + 1

		if primeCount > maxPrimes:
			maxPrimes = primeCount
			maxProd = a * b
			maxA = a
			maxB = b

print "n^2 {0} {1}n {2} {3} produces primes for {4} consecutive values of n".format("-" if maxA < 0 else "+", abs(maxA), "-" if maxB < 0 else "+", abs(maxB), maxPrimes)
print "The product of {0} and {1} is {2}".format(maxA, maxB, maxProd)