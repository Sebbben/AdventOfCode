import itertools

with open("inp.txt", "r") as f:
    directions, nodes = f.read().split("\n\n")
    nodes = {node[:3]:(node[7:10],node[12:-1]) for node in nodes.splitlines()}
    directions = list(map(int, list(directions.replace("L","0").replace("R", "1"))))

currentNode = "AAA"
steps = 0
d = itertools.cycle(directions)

while currentNode != "ZZZ":
    steps += 1
    currentNode = nodes[currentNode][next(d)]
    
print(steps)