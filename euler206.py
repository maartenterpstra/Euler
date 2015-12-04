import math
import re

# square root of 1020304050607080900
lowerBoundary = 1010101011
# square root of 1929394959697989990
upperBoundary = 1389026624
pattern = re.compile("1\d{1}2\d{1}3\d{1}4\d{1}5\d{1}6\d{1}7\d{1}8\d{1}9\d{1}0")

while upperBoundary > lowerBoundary:
    square = str(upperBoundary * upperBoundary)

    if pattern.match(square):
        print((square, upperBoundary))
        break
