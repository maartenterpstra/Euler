from sets import Set
MAX = 20161


def sumOfDivisors(n):
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if i != n / i:
                s += n / i
    return s

abundantNumbers = [x for x in range(1, MAX + 1) if sumOfDivisors(x) > x]
abSums = Set()
for i in range(len(abundantNumbers)):
    for j in abundantNumbers[i:]:
        absum = abundantNumbers[i] + j
        if absum < MAX:
            abSums.add(absum)

print((MAX * MAX + MAX) / 2 - sum(abSums))
