# is num 1 through n pandigital?
def isPandigital(num, n=9):
	nums = {}
	if num < 10 ** (n - 1) or num > 10 ** (n):
		return False

	numskeys = nums.keys();
	while num > 0:
		digit = num % 10
		if digit in numskeys:
			return False

		nums[digit] = 1
		num /= 10
		numskeys = numskeys + [digit]

	for p in xrange(1, n+1):
		if p not in numskeys:
			return False

	return True

def isPrime(x):
	if x < 2: return False
	if x == 2: return True
	if x % 2 == 0: return False

	for p in xrange(3, int(x ** 0.5) + 1, 2):
		if x % p == 0:
			return False


	return True

m = 0
for x in xrange(3, int(1e7), 2):
	if isPandigital(x, len(str(x))):
		if isPrime(x):
			m = x


print m