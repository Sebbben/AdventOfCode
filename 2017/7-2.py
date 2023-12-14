with open("7.txt") as f:
    data = f.read().splitlines()


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def getChildren(self): return self.children
    def getName(self): return self.name
    def getWeight(self): return self.weight
    def getTotalWeight(self):
        if self.children == None:
            return self.weight
        tot = 0
        for child in self.children:
            tot += child.getTotalWeight()

idk = {}

for line in data:
    l = line.split(" -> ")

    key = l[0].split(" ")[0]

    if len(l) == 1:
        idk[key] = None
        continue

    vals = l[1].split(", ")
    idk[key] = vals

hasChild = True
prog = 0
for i in idk:
    prog = i
    break
while hasChild:
    hasChild = False
    for key in idk:
        if idk[key] != None:
            if prog in idk[key]:
                prog = key
                hasChild = True
                break

print(prog)
