coins = [200, 100, 50, 20, 10, 5, 2, 1]
coinLen = len(coins)


def possibilities(num, maxcoin=0):

    s = 0
    if maxcoin == coinLen - 1:
        return 1
    for i in range(maxcoin, coinLen):
        if num - coins[i] == 0:
            s = s + 1
        if num - coins[i] > 0:
            s = s + possibilities(num - coins[i], i)
    return s

print(possibilities(200))
