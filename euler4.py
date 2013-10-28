import itertools

def palin(s):
	return s == s[::-1]

r = range(100, 1000)
print max([q * r for (q, r) in itertools.product(r, r) if palin(str(q*r))])