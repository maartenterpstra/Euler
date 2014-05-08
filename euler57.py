from decimal import Decimal
from fractions import Fraction


class CFraction(list):
    """
    A continued fraction, represented as a list of integer terms.
    """

    def __init__(self, value, maxterms=15):
        if isinstance(value, (int, float, Decimal)):
            value = Decimal(value)
            remainder = int(value)
            self.append(remainder)

            while len(self) < maxterms:
                value -= remainder
                value = Decimal(1) / value
                remainder = int(value)
                self.append(remainder)
        elif isinstance(value, (list, tuple)):
            self.extend(value)
        else:
            raise ValueError("CFraction requires number or list")

    def fraction(self, terms=None):
        "Convert to a Fraction."

        if terms is None or terms >= len(self):
            terms = len(self) - 1

        frac = Fraction(1, self[terms])
        for t in reversed(self[1:terms]):
            frac = 1 / (frac + t)

        frac += self[0]
        return frac

    def __float__(self):
        return float(self.fraction())

    def __str__(self):
        return "[%s]" % ", ".join([str(x) for x in self])

if __name__ == "__main__":
	sqrtList = [1]
	maxLen = 1000
	sqrtList.extend([2 for i in range(1, maxLen + 1)])

	count = 0
	cf  = CFraction(sqrtList)
	for t in xrange(1, len(cf)):
		frac = cf.fraction(t)
		split = str(frac).split('/')
		if len(split[0]) > len(split[1]):
			count += 1

	print count