with open("9.txt", "r") as f:
    diskmap = f.read().strip()


files = list(map(int, diskmap[::2]))
freeSpaces = list(map(int, diskmap[1::2]))

compacted = ""
totLenFiles = sum(files)

fillerFileID = len(files) - 1 

fillers = "".join([str(i)*files[i] for i in range(len(files)-1,-1,-1)])

fileID = 0
for fileID, amount in enumerate(files):
    compacted += str(fileID)*int(files[fileID])
    fileID += 1

    compacted += fillers[:freeSpaces[0]]

    fillers = fillers[freeSpaces[0]:]
    
    freeSpaces.pop(0)

    if not freeSpaces or len(compacted) >= totLenFiles: break

compacted = compacted[:totLenFiles]

tot = 0
for i, v in enumerate(compacted):
    tot += i*int(v)

print(tot)