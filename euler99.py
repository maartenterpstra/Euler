import math

def amountOfNums(base, exp):
	return int(math.floor(1 + exp*math.log(base)))

maxNums = (-1, -1)
lines = [line.strip() for line in open('base_exp.txt')]
for i in range(len(lines)):
	line = lines[i].split(',')
	base = int(line[0])
	exp = int(line[1])

	num = amountOfNums(base, exp)
	if num > maxNums[1]:
		maxNums = (i + 1, num)

print maxNums