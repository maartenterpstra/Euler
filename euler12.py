def getNthTriangleNumber(n):
	return ((n + 1) * n)/2

def getLengthFactors(n):
	#Why times 2?!
	return 2*len([x for x in range(1, int(n**0.5) + 1) if n % x == 0])


def getTriangleNumbers():
	i = 1;
	while True:
		yield getNthTriangleNumber(i)
		i += 1

print next(x for x in getTriangleNumbers() if getLengthFactors(x) > 500)