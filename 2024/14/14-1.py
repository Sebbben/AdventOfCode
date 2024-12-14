with open("14.txt", "r") as f:
    robots = f.readlines()


simTime = 100
mapX = 101
mapY = 103
# mapX = 11
# mapY = 7

tl, tr, bl, br = 0,0,0,0

for robot in robots:
    p,v = robot.split(" ")
    p = tuple(map(int, p.split("=")[1].split(",")))
    v = tuple(map(int, v.split("=")[1].split(",")))
    
    finalX = (p[0] + v[0]*simTime) % mapX
    finalY = (p[1] + v[1]*simTime) % mapY

    for i in range(simTime):
        print((p[0] + v[0]*i) % mapX, (p[1] + v[1]*i) % mapY)
    print(finalX, finalY)

    if finalX < mapX//2 and finalY < mapY // 2:
        tl += 1
    elif finalX > mapX//2 and finalY < mapY // 2:
        tr += 1
    elif finalX < mapX//2 and finalY > mapY // 2:
        bl += 1
    elif finalX > mapX//2 and finalY > mapY // 2:
        br += 1

print(tl,tr,bl,br)
print(tl*tr*bl*br)