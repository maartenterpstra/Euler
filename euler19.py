from datetime import date

numMonths = 12


#Could also be a oneliner as here, but the other version is more readable
#print len([d for d in (date(year, month, 1) for year in range(1901, 2001) for month in range(1, numMonths + 1)) if d.weekday() == 6])


i = 0
for year in range(1901, 2001):
	#plus one for an inclusive range, since the range function is exclusive the upper limit
	for month in range(1, numMonths + 1):
		if date(year, month, 1).weekday() == 6:
			i += 1

print i