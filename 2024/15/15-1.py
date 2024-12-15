with open("15-test.txt", "r") as f:
    warehouse, dirs = f.read().split("\n\n")

wareLines = warehouse.splitlines()

dirsMap = {
    "<": -1,
    ">": 1,
    "v": len(wareLines[0]),
    "^": -len(wareLines[0])
}

warehouse = list("".join(wareLines))
robot = warehouse.index("@")

for instr in dirs:
    currDir = dirsMap[instr]
    x = robot+currDir
    
    while warehouse[x] not in ["#", "."]:
        x += currDir
    
    if warehouse[x] == "#":
        continue
    
    warehouse[x] = "O"
    warehouse[robot] = "."
    robot += currDir
    warehouse[robot] = "@"

tot = 0

for x, obj in enumerate(warehouse):
    if obj != "O": continue

    tot += x//dirsMap["v"]*100 + (x%dirsMap["v"])

print(tot)