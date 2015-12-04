def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (abs(a) / gcd(a, b)) * abs(b)

lm = 1
for x in range(2, 21):
    lm = lcm(x, lm)

print lm
