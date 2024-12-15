with open("9.txt", "r") as f:
    diskmap = f.read().strip()


files = list(map(int, diskmap[::2]))
freeSpaces = list(map(int, diskmap[1::2]))

tot = 0

outIndex = 0
fileId = 0
while fileId < len(files):
    size = files[fileId]
    for _ in range(size):
        tot += outIndex*fileId
        files[fileId] -= 1
        outIndex += 1
    
    for _ in range(freeSpaces.pop(0)):
        if files[-1] == 0: break
        tot += (len(files)-1)*outIndex
        outIndex += 1
        files[-1] -= 1
        if files[-1] == 0:
            files.pop()

    fileId += 1



print(tot)