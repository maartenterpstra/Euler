def isFifthPowerOfDigits(n, power = 5):
	return sum(map(lambda x: x ** power, [int(i) for i in str(n)])) == n

print sum([i for i in xrange(2, 2*10 ** 5) if isFifthPowerOfDigits(i)])