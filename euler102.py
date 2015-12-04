class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "({0}, {1}, {2})".format(a, b, c)

    def sign(self, p1, p2, p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    def contains(self, p):
        b1 = self.sign(p, self.a, self.b) < 0
        b2 = self.sign(p, self.b, self.c) < 0
        b3 = self.sign(p, self.c, self.a) < 0

        return b1 == b2 and b2 == b3


origin = Point(0, 0)
containsOrigin = 0

lines = [line.strip() for line in open('triangles.txt')]
for line in lines:
    lineSplit = line.split(',')
    p1 = Point(int(lineSplit[0]), int(lineSplit[1]))
    p2 = Point(int(lineSplit[2]), int(lineSplit[3]))
    p3 = Point(int(lineSplit[4]), int(lineSplit[5]))

    triangle = Triangle(p1, p2, p3)
    if triangle.contains(origin):
        containsOrigin += 1

print(containsOrigin)
