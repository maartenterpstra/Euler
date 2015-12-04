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


def findMinCubePerm(cubeDict, numPerms=5):
    minVal = 999**numPerms
    for values in [q for q in cubeDict.values() if len(q) == numPerms]:
        if eachItemIsPermutationOfEachOther(values):
            minVal = min(minVal, min(values))
    return minVal

limit = 10000
cubes = {}
for cuboid in [x * x * x for x in xrange(limit)]:
    sortedCuboid = ''.join(sorted(list(str(cuboid))))

    if sortedCuboid not in cubes:
        cubes[sortedCuboid] = [cuboid]
    else:
        cubes[sortedCuboid].append(cuboid)

minCubePerm = findMinCubePerm(cubes)
print minCubePerm
