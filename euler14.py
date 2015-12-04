knownLengths = [-1] * 1000000


def add_item(list, item):
    list.append(item)
    return list


def collatz(n, l):
    if n < 1000000 and knownLengths[n] != -1:
        return len(l) + knownLengths[n]
    l = add_item(l, n)
    if n == 1:
        return len(l)
    elif (n & 1) == 0:
        return collatz(n >> 1, l)
    else:
        return collatz(3 * n + 1, l)

Max = 0
maxVal = 1
for x in range(1, 1000000):
    myList = []
    lenlist = collatz(x, myList)
    knownLengths[x] = lenlist
    if(lenlist > Max):
        Max = lenlist
        maxVal = x

print(maxVal)
