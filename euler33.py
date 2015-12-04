from fractions import Fraction
from decimal import Decimal
fracs = []
limit = 100
for i in range(10, limit):
    i_set = set(str(i))
    for j in range(i + 1, limit):
        j_set = set(str(j))
        # Skip trivial examples (20 / 40, etc)
        if i % 10 == 0 and j % 10 == 0:
            continue
        # Common elements means that the intersection of the sets is non-empty
        # Exploit that
        inter = i_set.intersection(j_set)
        if len(inter) > 0:
            # Sets dont do indexing. These sets contain only one element so
            # popping yields that element
            common = str(inter.pop())
            # Prevent replacing entire numbers (i.e. 11 becomes '')
            new_i = int(str(i).replace(common, "", 1))
            new_j = int(str(j).replace(common, "", 1))

            # floats work for upto 100 but maybe not after that. Still fast enough though
            # check for new j is needed as, for example, 12/20 -> 2 / 0
            if new_j > 0 and Decimal(
                    i) / Decimal(j) == Decimal(new_i) / Decimal(new_j):
                fracs.append(Fraction(i, j))

# Result is denominator of reduced fraction. The Fraction class does
# reduction automatically
print reduce(lambda x, y: x * y, fracs).denominator
