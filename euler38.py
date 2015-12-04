def isPandigital(n):
    # Basically it computes the histogram and asserts that every number occurs
    # once
    if n < 123456789 or n > 987654321:
        return False

    l = [0] * 9
    for x in str(n):
        l[int(x) - 1] += 1

    return all(item == 1 for item in l)

l = set()
for x in range(1, 10):
    for t in range(1, 10000):
        multRange = [z + 1 for z in range(x)]
        newNum = int(''.join([str(t * u) for u in multRange]))
        if (isPandigital(newNum)):
            # print(x, newNum)
            l.add((newNum, x, t))

(num, numMult, base) = max(l)
print("Largest pandigital number is {0} ({1} * [1..{2}])".format(num, base, numMult))
