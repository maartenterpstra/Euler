length = 50


def findWays(remainingLength, tileLen, cache):
    numSol = 0

    if (cache[remainingLength] != 0):
        return cache[remainingLength]
    if tileLen > remainingLength:
        return numSol
    for remaining in range(remainingLength - tileLen + 1):
        numSol += 1
        numSol += findWays(remainingLength - remaining -
                           tileLen, tileLen, cache)

    cache[remainingLength] = numSol
    return numSol

solutions = 0
nMin = 2
nMax = 4
for i in range(nMin, nMax + 1):
    cache = [0] * (length + 1)
    solutions += findWays(length, i, cache)

print(solutions)
