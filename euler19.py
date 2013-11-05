from datetime import date

numMonths = 12
i = 0
for year in range(1901, 2001):
	#plus one for an inclusive range, since the range function is exclusive the upper limit
	for month in range(1, numMonths + 1):
		if date(year, month, 1).weekday() == 6:
			i += 1

print i