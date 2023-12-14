import re
with open("5.txt") as f:
    stacks, instructions = f.read().split("\n\n")

stacksList = [
    [],
    [],
    [],
    
    [],
    [],
    [],

    [],
    [],
    [],
]

for i in stacks.splitlines()[:-1]:
    
    row = [i[x+1:x+2] for x in range(0,len(i)-2,4)]
    for j in range(len(row)):
        if row[j] != " ":
            stacksList[j].append(row[j])

for i in range(len(stacksList)):
    stacksList[i].reverse()

for cmd in instructions.splitlines():
    cmd = list(map(int, re.findall("\d+", cmd)))
    print(cmd)
    for i in range(cmd[0]):
        stacksList[cmd[2]-1].append(stacksList[cmd[1]-1].pop())

print("".join([x[-1] for x in stacksList]))