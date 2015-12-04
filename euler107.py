edges = []
lines = [line.strip() for line in open('network.txt')]
for i in range(len(lines)):
    line = lines[i]
    elements = line.split(',')
    for j in range(len(elements)):
        if elements[j] != '-':
            edges.append((i, j, int(elements[j])))

# Perform Prim's algorithm
nodesInMST = [0]
edgesInMST = []
while sorted(nodesInMST) != list(range(len(lines))):
    minConnectsToTree = min([q for q in edges if q[0] in nodesInMST and q[
                            1] not in nodesInMST], key=lambda x: x[2])
    edgesInMST.append(minConnectsToTree)
    nodesInMST.append(minConnectsToTree[1])

# divide by two because it is a directed graph and edges are added twice
curWeight = sum(x[2] for x in edges) / 2
mstWeight = sum([x[2] for x in edgesInMST])
saving = curWeight - mstWeight
print(("{0} - {1} = {2}".format(curWeight, mstWeight, saving)))
