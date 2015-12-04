def chakravala(n):
    b = 1
    a = 1
    minDiff = 1000000000000
    while abs(a * a - n) < minDiff:
        minDiff = abs(a * a - n)
        a += 1
    a -= 1
    k = a * a - n

    while True:
        ms = [m for m in range(1, 50) if (a + b * m) % k == 0]
        diff = 100000
        m = 1
        for q in ms:
            if abs(q * q - n) < diff:
                diff = abs(q * q - n)
                m = q
        newA = (a * m + n * b) / abs(k)
        b = (a + b * m) / abs(k)
        k = (m * m - n) / k
        a = newA
        if k == 1:
            return a
        if (abs(k) == 2 or abs(k) == 4) and (a % 2 == 0 or b % 2 == 0):
            return abs((a * a + n * b * b) / k)

limit = 1000
squares = [a * a for a in range(33)]
maxX = 0
maxD = 0
Ds = [x for x in range(2, limit + 1) if x not in squares]
for d in Ds:
    a = chakravala(d)
    if a > maxX:
        maxX = a
        maxD = d

print(maxX, maxD)
