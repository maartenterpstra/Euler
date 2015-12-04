from decimal import Decimal
from fractions import Fraction


def fraction(self, terms=None):
    "Convert to a Fraction."

    if terms is None or terms >= len(self):
        terms = len(self) - 1

    frac = Fraction(1, self[terms])
    for t in reversed(self[1:terms]):
        frac = 1 / (frac + t)

    frac += self[0]
    return frac

if __name__ == "__main__":
    elist = [2]
    maxLen = 100
    for i in range(1, maxLen // 3 + 2):
        elist.append(1)
        elist.append(i * 2)
        elist.append(1)

    elist = elist[:maxLen]
    frac = fraction(elist)

    numerator = str(frac).split('/')[0]
    numbersInNumerator = [int(i) for i in list(numerator)]

    print sum(numbersInNumerator)
