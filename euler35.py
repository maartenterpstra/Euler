from math import ceil, log10


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def circlesArePrime(num):
    if num < 10:
        return True

    l = [num]
    circle = num

    while True:
        # Suppose 197 is tested, then 7000 is added and whole divided by 10,
        # yielding 719
        circle = int(circle + (circle % 10) *
                     pow(10, ceil(log10(circle)))) / 10

        if circle == num:
            return True

        if not isPrime(circle):
            return False

limit = int(1e6)
print(len([z for z in (x for x in range(2, limit + 1)
                       if isPrime(x)) if circlesArePrime(z)]))
