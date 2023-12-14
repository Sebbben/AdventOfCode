with open("6.txt") as f:
    cont = f.read().splitlines()


lights = []
size = 1000

for i in range(size):
    lights.append([])
    for j in range(size):
        lights[i].append(0)

def on(n):
    return n+1


def off(n):
    return max(0,n-1)


def toggle(n):
    return n+2



for line in cont:
    inst = line.split(" ")
    pos1 = inst[-3].split(",")
    pos2 = inst[-1].split(",")
    
    pos1 = [int(i) for i in pos1]
    pos2 = [int(i) for i in pos2]

    if inst[0] == "toggle":
        method = toggle
    elif inst[1] == "on":
        method = on
    else:
        method = off

    # print(method.__name__)

    for i in range(pos1[0],pos2[0]+1):
        for j in range(pos1[1],pos2[1]+1):
                lights[i][j] = method(lights[i][j])


tot = 0
for i in lights:
    for j in i:
        tot += j

print(tot)