import itertools


def isPalindrome(s):
    return s == s[::-1]

numberRange = list(range(100, 1000))
print(max([q * r for (q, r) in itertools.product(numberRange,
                                                 numberRange) if isPalindrome(str(q * r))]))
