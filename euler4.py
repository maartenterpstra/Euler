def palin(s):
	return s == s[::-1]

def getList(a, b):
	l = []
	for x in range(a, b):
		for y in range(a, b):
			l.append((x, y))
	return l

print max([q * r for (q, r) in [(q, r) for q in range(100, 1000) for r in range(100, 1000)] if palin(str(q*r))])