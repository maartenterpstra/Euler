import itertools
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            NotImplemented

    def distance(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return math.hypot(dx, dy)


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSides(self):
        return [p1.distance(p2) for (p1, p2) in itertools.combinations(
            [self.a, self.b, self.c], 2)]


def testSides(triangle):
    sides = triangle.getSides()
    sidesSquared = sorted([x * x for x in sides])
    return abs(sidesSquared[0] + sidesSquared[1] - sidesSquared[2]) < 0.0001


def numOfRightTriangles(triangleList, limit):
    count = 0
    for triangle in triangleList:
        if testSides(triangle):
            count += 1
            if triangle.b.x == limit:
                if triangle.c.x == triangle.c.y == limit:
                    return count

    return count


def InLine(x, y, z):
    if x.x == y.x == z.x:
        return True
    if x.y == y.y == z.y:
        return True
    return False

limit = 50
points = [Point(x, y) for x in range(limit + 1) for y in range(limit + 1)]
print("Generated Points")
origin = Point(0, 0)
possibleTriangles = (Triangle(x, y, z) for (x, y, z) in itertools.combinations(
    points, 3) if x == origin and not InLine(x, y, z))
print("Generated Triangles")

print((numOfRightTriangles(possibleTriangles, limit)))
