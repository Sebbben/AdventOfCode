with open("8.txt") as f:
    cont = f.read().splitlines()

tot = 0

for line in cont:
    codeLen = len(line)

    newLen = codeLen + line.count("\\") + line.count("\"") + 4

    tot += newLen-codeLen

print(tot)