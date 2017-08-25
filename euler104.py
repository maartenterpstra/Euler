import numpy as np
import itertools
Qm = np.matrix('1 1 ; 1 0', dtype='object')
Q = np.matrix('1 1 ; 1 0', dtype='object')
Qm2 = Qm * Qm
# all_pandigitals = set(map("".join, itertools.permutations('123456789')))


def isPandigital(n_str):
    splitted = set(n_str)
    if '0' in splitted:
        return False
    return len(splitted) == 9

k = 1
while True:
    Fn = Q[0, 1]
    Fnp1 = Q[0, 0]

    if isPandigital(str(Fn % 10 ** 9)) and isPandigital(str(Fn)[:9]):
        print(k)
        break
    if isPandigital(str(Fnp1 % 10 ** 9)) and isPandigital(str(Fnp1)[:9]):
        print(k+1)
        break
    k = k + 2
    Q = Q * Qm2
