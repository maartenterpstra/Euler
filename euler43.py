from itertools import permutations
from functools import reduce

totalSum = 0
checkPrimes = [2, 3, 5, 7, 11, 13, 17]
for x in permutations("1234567890"):
    allCorrect = True
    for i in range(1, 8):
        if int(''.join(x[i:i+3])) % checkPrimes[i - 1] != 0:
            allCorrect = False
            break
    if allCorrect:
        print(int(''.join(x)))
        totalSum += int(''.join(x))

print(
    "Total sum of pandigitals with sub-string divisibility property: {0}".format(totalSum))
