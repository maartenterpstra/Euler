diagLength = 1001


# s = 1
# for x in range(3, diagLength + 1, 2):
# 	squared = x*x
# 	rightTop    = squared
# 	leftTop     = squared - x   + 1
# 	rightBottom = squared - 2*x + 2
# 	leftBottom  = squared - 3*x + 3
# 	s = s + rightBottom + leftBottom + rightTop + leftTop

s = sum(4*x*x - 6*x + 6 for x in xrange(3, diagLength + 1, 2)) + 1
print s