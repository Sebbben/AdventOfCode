with open("8.txt") as f:
    cont = f.read().splitlines()

tot = 0

for line in cont:
    codeLen = len(line)
    memLen = len(line[1:-1])

    i = 0
    while i < len(line):
        if line[i:i+2] == "\\"+"x":
            memLen-=3
            i+=3
        elif line[i] == "\\":
            memLen-=1
            i+=1
        i+=1
    tot += (codeLen-memLen)

print(tot)