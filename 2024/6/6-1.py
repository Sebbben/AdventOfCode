with open("6.txt", "r") as f:
    col = f.readlines()

dirs = [-len(col[0]), 1, len(col[0]), -1]

col = "".join(col)
x = col.index("^")


uniquePos = set()
currDirIndex = 0
currDir = dirs[currDirIndex]
while True:
    uniquePos.add(x)

    if abs(currDir) == 1 and x // dirs[2] != (x+currDir) // dirs[2]: break
    if abs(currDir) != 1 and not (0<= (x+currDir) <= len(col)): break
    if col[x+currDir] == "#":
        currDirIndex = (currDirIndex + 1) % len(dirs)
        currDir = dirs[currDirIndex]

    x += currDir

print(len(uniquePos))
