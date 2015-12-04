def distinctPowers(a, b):
    return sorted(set([x ** y for x in range(2, a + 1)
                       for y in range(2, b + 1)]))

print len(distinctPowers(100, 100))
