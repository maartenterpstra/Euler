def most_common(lst):
    return max(set(lst), key=lst.count)

squares = [a*a for a in xrange(1, 1000)]
limit = 1000
print most_common(filter(lambda x: x <= 1000, (sum((x, y, int((x*x + y*y) ** 0.5))) for x in xrange(1, limit) for y in xrange(x, limit) if x*x + y*y in squares)))