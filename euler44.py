from itertools import combinations
pentagonals = frozenset([int((0.5 * n) * ((3 * n - 1))) for n in range(1, 10000)])


def isPentagonal(n):
    return n in pentagonals

lowDiff = int(1e10)
for (a, b) in combinations(pentagonals, 2):
    diff = abs(a - b)
    if isPentagonal(a + b) and isPentagonal(diff):
        if diff < lowDiff:
            lowDiff = diff

print(lowDiff)
