upper = 100
numberRange = list(range(1, upper + 1))
sos = sum([x * x for x in numberRange])
sumList = sum(numberRange)
sos2 = sumList * sumList
print(sos2 - sos)
