class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def partition(n, maxVal = None):
	if n == 0:
		return 1
		
	sum = 0
	maxVal = n if maxVal == None else maxVal
	minVal = min(maxVal, n)
	for i in range(minVal, 0, -1):
		sum += partition(n - i, i)

	return sum 

partition = Memoize(partition)
print (partition(100) - 1)