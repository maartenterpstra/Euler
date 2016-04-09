print(sum((1 if n ^ 2 * n ^ 3 * n == 0 else 0 for n in range(1, 2 ** 30 + 1))))
