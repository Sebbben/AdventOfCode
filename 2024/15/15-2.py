with open("15.txt", "r") as f:
    warehouse, dirs = f.read().split("\n\n")

wareLines = warehouse.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.").splitlines()

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
    

    if instr in ("<", ">"):
        
        while warehouse[x] not in ("#", "."):
            x += currDir
            
        if warehouse[x] == "#":
            continue
        while x != robot:
            warehouse[x] = warehouse[x-currDir]
            x -= currDir
        
    else:
        blocked = False
        toCheck = [robot]
        toUpdate = []
        toClear = []
        while toCheck:
            currCheck = toCheck.pop(0) + currDir        
            toClear.append(currCheck-currDir)
            if warehouse[currCheck] == ".": 
                continue
            if warehouse[currCheck] == "#": 
                blocked = True
                break
                
            if warehouse[currCheck] == "[":
                toCheck.append(currCheck)
                toCheck.append(currCheck+1)
                toUpdate.append((currCheck+currDir, warehouse[currCheck]))
                toUpdate.append((currCheck+currDir+1, warehouse[currCheck+1]))

            else:
                toCheck.append(currCheck)
                toCheck.append(currCheck-1)
                toUpdate.append((currCheck+currDir, warehouse[currCheck]))
                toUpdate.append((currCheck+currDir-1, warehouse[currCheck-1]))
                
                
        if blocked: continue
        
        # print(toUpdate)
        for pos in toClear:
            warehouse[pos] = "."
        if warehouse[robot+currDir] == "[":            
            warehouse[robot+currDir] = "@"
            warehouse[robot+currDir+1] = "."
        elif warehouse[robot+currDir] == "]":            
            warehouse[robot+currDir] = "@"
            warehouse[robot+currDir-1] = "."
        elif warehouse[robot+currDir] == ".":
            warehouse[robot+currDir] = "@"
        
        for pos, newVal in toUpdate:
            warehouse[pos] = newVal


    warehouse[robot] = "."
    robot += currDir
    
    # print(instr)
    # for i in range(0,len(warehouse), dirsMap["v"]):
    #     print("".join(warehouse[i:i+dirsMap["v"]]))
    # input()

    
    

tot = 0

for x, obj in enumerate(warehouse):
    if obj != "[": continue

    tot += x//dirsMap["v"]*100 + (x%dirsMap["v"])

print(tot)