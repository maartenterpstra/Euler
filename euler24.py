from itertools import permutations


def nthPermutation(num, n):
    return int(''.join(list(permutations(list(num)))[n - 1]))

print nthPermutation("0123456789", 1000000)
