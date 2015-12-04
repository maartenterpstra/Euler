def factorial(n, res=1):
    if n <= 1:
        return res
    else:
        return factorial(n - 1, res * n)

print((sum(int(x) for x in list(str(factorial(100))))))
