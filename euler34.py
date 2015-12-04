def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

# precompute all factorial for every digit
fac = [factorial(x) for x in range(10)]

# is the sum of the factorial of the digits equal to itself?


def isFactoriolDigitSum(n):
    return sum(map(lambda x: fac[x], [int(i) for i in str(n)])) == n

print sum([x for x in xrange(3, 10 ** 5) if isFactoriolDigitSum(x)])
