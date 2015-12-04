def most_common(lst):
    return max(set(lst), key=lst.count)

squares = [a * a for a in range(1, 1000)]
limit = 1000
print(most_common([x for x in (sum((x,
                                    y,
                                    int((x * x + y * y) ** 0.5))) for x in range(1,
                                                                                 limit) for y in range(x,
                                                                                                       limit) if x * x + y * y in squares) if x <= 1000]))
