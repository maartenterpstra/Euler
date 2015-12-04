f = open('p042_words.txt', 'r')
words = f.read().replace('"', '').split(',')

# a triangular number s = n(n+1) / 2
# rigorous algebra shows that n = (sqrt(1 + 8s) - 1) / 2
# so to test that, compute it and see if it is an int


def isTriangular(s):
    test = ((1 + 8 * s) ** 0.5 - 1) / 2.0
    return int(test) == test

print(sum([isTriangular(s)
           for s in [sum([ord(x) - ord('A') + 1 for x in list(w)]) for w in words]]))
