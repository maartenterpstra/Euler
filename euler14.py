
def add_item(list, item):
    list.append(item)
    return list

def collatz(n, l):
	l = add_item(l, n)
	if n == 1:
		return len(l)
	elif n % 2 == 0:
		return collatz(n/2, l)
	else:
		return collatz(3*n + 1, l)

Max = 0
maxVal = 1
for x in range(1, 1000000):
	myList = []
	lenlist = collatz(x, myList)
	if(lenlist > Max):
		Max = lenlist
		maxVal = x

print maxVal