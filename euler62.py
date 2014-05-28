def isPermutation(item, otherItem):
	val1 = ''.join(sorted(list(str(item))))
	val2 = ''.join(sorted(list(str(otherItem))))
	return val1 == val2

def eachItemIsPermutationOfEachOther(values):
	for i in range(len(values) - 1):
		for j in range(i + 1, len(values)):
			if not isPermutation(values[i], values[j]):
				return False
	return True

def findMinCubePerm(cubeDict, numPerms = 5):
	minVal = 999**numPerms
	for l in [q for q in cubeDict.values() if len(q) == numPerms]:
		values = [z for (y,z) in l]
		if eachItemIsPermutationOfEachOther(values):
			minVal = min(minVal, min(values))
	return minVal

limit = 10000
cubes = {}
for x in xrange( limit):
	cuboid = x*x*x
	sortedCuboid = ''.join(sorted(list(str(cuboid))))

	if not cubes.has_key(sortedCuboid):
		cubes[sortedCuboid] = [(x, cuboid)]
	else:
		cubes[sortedCuboid].append((x, cuboid))

minCubePerm = findMinCubePerm(cubes)
print minCubePerm