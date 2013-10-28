upper = 100
numberRange = range(1, upper + 1)
sos = sum(map(lambda x: x*x, numberRange))
sumList = sum(numberRange)
sos2 = sumList * sumList
print sos2 - sos