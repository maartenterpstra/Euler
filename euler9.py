# through trial-and-error it seems that 426 is the lowest maximum value
# that will solve this problem
maxVal = 426
print next(x * y * z for x in range(maxVal) for y in range(x + 1, maxVal) for z in range(y + 1, maxVal) if x + y + z == 1000 and x * x + y * y == z * z)
