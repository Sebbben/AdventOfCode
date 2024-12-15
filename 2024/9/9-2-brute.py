with open("9-test.txt", "r") as f:
    diskmap = f.read().strip()


files = list(map(int, diskmap[::2]))
freeSpaces = list(map(int, diskmap[1::2]))

compacted = []

for fileId, size in enumerate(files):
    compacted.append((fileId, size))
    compacted.append((".", freeSpaces.pop(0)))

print(compacted)