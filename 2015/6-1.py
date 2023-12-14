with open("6.txt") as f:
    cont = f.read().splitlines()


def pp(l):
    for i in l:
        for j in i:
            if j:
                print("#", end="")
            else:
                print(" ", end="")
        print("")




lights = []
size = 1000

for i in range(size):
    lights.append([])
    for j in range(size):
        lights[i].append(False)

def on(n):
    return True


def off(n):
    return False


def toggle(n):
    return not n



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

pp(lights)

tot = 0
for i in lights:
    tot += i.count(True)

print(tot)

from PIL import Image  

width = 1000
height = 1000

img  = Image.new( mode = "RGB", size = (width, height), color = (0, 0, 0) )

for i in range(len(lights)):
    for j in range(len(lights[i])):
        img.putpixel((i,j), (255*lights[i][j],255*lights[i][j],255*lights[i][j]))


img.show()