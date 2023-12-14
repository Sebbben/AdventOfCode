# import itertools

# with open("inp.txt", "r") as f:
#     directions, nodes = f.read().split("\n\n")
#     nodes = {node[:3]:(node[7:10],node[12:-1]) for node in nodes.splitlines()}
#     directions = list(map(int, list(directions.replace("L","0").replace("R", "1"))))

# followingNodes = [node for node in nodes if node[-1]=="A"]

# print(followingNodes)

# steps = 0
# d = itertools.cycle(directions)

# while not all((node[-1]=="Z" for node in followingNodes)):
#     steps += 1
#     nextStep = next(d)
#     followingNodes = [nodes[node][nextStep] for node in followingNodes]
    
# print(steps)




import itertools

with open("inp.txt", "r") as f:
    directions, nodes = f.read().split("\n\n")
    nodes = {node[:3]:(node[7:10],node[12:-1]) for node in nodes.splitlines()}
    directions = list(map(int, list(directions.replace("L","0").replace("R", "1"))))

followingNodes = [node for node in nodes if node[-1]=="A"]

startingOrder = followingNodes.copy()
nodesLoopOffset = {node: [-1,-1] for node in followingNodes}


steps = 0
d = itertools.cycle(directions)

while followingNodes:
    toRemove = []
    for i, node in enumerate(followingNodes): 
        startingNode = startingOrder[i]
        if node[-1] == "Z": 
            if nodesLoopOffset[startingNode][0] == -1:
                nodesLoopOffset[startingNode][0] = steps
            elif nodesLoopOffset[startingNode][1] == -1:
                nodesLoopOffset[startingNode][1] = steps - nodesLoopOffset[startingNode][0]
                toRemove.append((node, startingNode))
    
    for node, startingNode in toRemove:
        startingOrder.remove(startingNode)
        followingNodes.remove(node)

            

    steps += 1
    nextStep = next(d)
    followingNodes = [nodes[node][nextStep] for node in followingNodes]
    
from functools import reduce
from math import gcd
    
# print(nodesLoopOffset)
print(reduce((lambda x, y: int(x * y / gcd(x, y))), [nums[0] for nums in nodesLoopOffset.values()]))
