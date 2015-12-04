def d(x):
    s = 1
    for i in range(2, int(x**0.5) + 1):
        if (x % i == 0):
            s += i
            s += x / i
    return s


def check(x):
    i = d(x)
    return i != x and d(i) == x

print((sum(x for x in range(1, 10000) if check(x))))
