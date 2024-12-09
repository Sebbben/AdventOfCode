with open("6.txt", "r") as f:
    col = f.readlines()

dirs = [-len(col[0]), 1, len(col[0]), -1]

def isLoop(objPos):
    ccol = col
    x = ccol.index("^")
    ccol = ccol[:objPos] + "#" + ccol[objPos+1:]


    uniquePos = set()
    currDirIndex = 0
    currDir = dirs[currDirIndex]
    while True:
        if (x, currDirIndex) in uniquePos: return True
        uniquePos.add((x,currDirIndex))

        if abs(currDir) == 1 and x // dirs[2] != (x+currDir) // dirs[2]: break
        if abs(currDir) != 1 and not (0<= (x+currDir) <= len(ccol)): break
        if ccol[x+currDir] == "#":
            currDirIndex = (currDirIndex + 1) % len(dirs)
            currDir = dirs[currDirIndex]

        x += currDir
    
    return False


col = "".join(col)
x = col.index("^")

uniquePos = {}
uniqueObs = set()
currDirIndex = 0
currDir = dirs[currDirIndex]
while True:
    if not x in uniquePos: uniquePos[x] = []
    uniquePos[x].append(currDirIndex)

    if isLoop(x+currDir):
        uniqueObs.add(x+currDir)

    if abs(currDir) == 1 and x // dirs[2] != (x+currDir) // dirs[2]: break
    if abs(currDir) != 1 and not (0<= (x+currDir) <= len(col)): break
    if col[x+currDir] == "#":
        currDirIndex = (currDirIndex + 1) % len(dirs)
        currDir = dirs[currDirIndex]

    x += currDir




print(len(uniqueObs))

# for i in uniqueObs:
#     print(i, i%dirs[2], i//dirs[2])
