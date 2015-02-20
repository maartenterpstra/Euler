# (Public) Returns F(n).
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]

# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

i = 0
f = fibonacci(i)
while len(str(f)) < 1000:
    i = i + 1
    f = fibonacci(i)

print i