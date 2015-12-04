def isFifthPowerOfDigits(n, power=5):
    return sum([x ** power for x in [int(i) for i in str(n)]]) == n

print(sum([i for i in range(2, 2 * 10 ** 5) if isFifthPowerOfDigits(i)]))
