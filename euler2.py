def fibGen(a=-1, b=1, upto=4000000):
    while a + b < upto:
        a, b = b, a + b
        yield b

print(sum(i for i in fibGen() if i % 2))
