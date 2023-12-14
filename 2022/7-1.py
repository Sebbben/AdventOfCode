with open("7.txt") as f:
    cont = f.read().splitlines()

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def getParent(self):
        return self.parent

    def mkdir(self, name):
        self.children.append(Dir(name, self))

    def mkfile(self,name,size):
        self.children.append(AFile(self, name, size))

    def getSize(self):
        return sum([x.getSize() for x in self.children])

    def getChild(self, name):
        return [x for x in self.children if x.name == name][0]


class AFile:
    def __init__(self, parent, name, size):
        self.name = name
        self.parent = parent
        self.size = size

    def getSize(self):
        return self.size

root = Dir("/", None)
walker = root

for line in cont:
    if line.startswith("$"):
        if line.startswith("$ ls"):
            pass
        elif line.startswith("$ cd"):
            _,__, where = line.split(" ")
            if where == "/":
                walker = root
            elif where == "..":
                walker = walker.getParent()
            else:
                walker = walker.getChild(where)

    else:
        if line.startswith("dir"):
            walker.mkdir(line.split(" ")[1])
        else:
            size, name = line.split(" ")
            walker.mkfile(name,int(size))

maxSize = 100_000
foldersUnderSum = 0

def getFolderSizes(folder):
    global foldersUnderSum
    s = folder.getSize()
    if s < maxSize: # <= ?
        foldersUnderSum += s
    for i in folder.children:
        if isinstance(i,Dir):
            getFolderSizes(i)
    
getFolderSizes(root)
print(foldersUnderSum)