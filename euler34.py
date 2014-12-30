def factorial(n):
	if n <= 1:
		return 1

	return n * factorial(n - 1)

fac = [factorial(x) for x in range(10)]

def isFactoriolDigitSum(n):
	return sum(map(lambda x: fac[x], [int(i) for i in str(n)])) == n

print sum([x for x in xrange(3, 10 ** 5) if isFactoriolDigitSum(x)])