def findNumberSum(power):
	return sum([int(x) for x in list(str(2**power))])

print findNumberSum(1000)