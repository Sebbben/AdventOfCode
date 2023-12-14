with open("7.txt") as f:
    data = f.read().splitlines()

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