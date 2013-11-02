def factorial(n, res=1):
	return res if n <= 1 else factorial(n-1, n * res)

def numPaths(n):
	facN = factorial(n)
	return factorial(2*n)/(facN * facN)

print numPaths(20)