from fractions import gcd
from decimal import Decimal
def getNoverPhiN(n):
	PhiN = len([i for i in range(1, n) if gcd(i, n) == 1])
	return Decimal(Decimal(n) / Decimal(PhiN))

maxVal = Decimal(0.0)
maxI = 0
for i in range(2, 1000001):
	frac = getNoverPhiN(i)
	if frac > maxVal:
		maxVal = frac
		maxI = i

print i, maxVal