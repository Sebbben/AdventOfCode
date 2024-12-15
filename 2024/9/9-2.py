with open("9-test.txt", "r") as f:
    diskmap = f.read().strip()


files = list(map(int, diskmap[::2]))
freeSpaces = list(map(int, diskmap[1::2]))

tot = 0

taken = set()

outIndex = 0
fileId = 0
while fileId < len(files):
    tot += fileId * sum(range(fileId, fileId+files[fileId]+1))
    print(outIndex, fileId, files[fileId])
    outIndex += files[fileId]
    fillerFileId = len(files)-1
    
    while fillerFileId > fileId and freeSpaces[0] != 0:
        if files[fillerFileId] <= freeSpaces[0] and fillerFileId not in taken:
            print(outIndex, fillerFileId, files[fillerFileId], "-")
            tot += fillerFileId * sum(range(fillerFileId, fillerFileId+files[fillerFileId]+1))
            freeSpaces[0] -= files[fillerFileId]
            outIndex += files[fillerFileId]
            taken.add(fillerFileId)
        fillerFileId -= 1

    outIndex += freeSpaces.pop(0)
    fileId += 1
    while fileId in taken:
        fileId += 1
        fillerFileId += 1

print(tot)