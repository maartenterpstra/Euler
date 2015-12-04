from functools import reduce
indices = [1, 10, 100, 1000, 10000, 100000, 1000000]

st = ''.join([str(a) for a in range(1, 200000)])
print(reduce(lambda x, y: x * y, [int(st[a - 1]) for a in indices]))
