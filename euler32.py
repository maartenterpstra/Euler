# Check if number is pandigital by checking if each number of 1 through 9 occurs exactly once
def isPandigital(i, j, prod):
	hist = [0] * 9
	num = ''.join([str(i), str(j), str(prod)])
	
	if len(num) != 9 or num.find('0') != -1:
		return False
	for x in num:
		hist[int(x) - 1]+=1

	return all(h == 1 for h in hist)

prods = []
for i in xrange(2, 2000):
	for j in xrange(i+1, 2000):
		prod = i*j
		# if prod is higher than 10000 the number is too large to be pandigital
		# because the length would greater than 10 numbers -> pidgeon hole principle
		if prod > 10000:
			break
		if isPandigital(i, j, prod) and not prod in prods:
			prods.append(i*j)

print sum(prods)