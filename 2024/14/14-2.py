with open("14.txt", "r") as f:
    robots = f.readlines()


simTime = 0
mapX = 101
mapY = 103

while True:
    grid = []
    row = []
    for __ in range(mapX):
        row.append(".")
    for _ in range(mapY):
        grid.append(row.copy())

    for robot in robots:
        p,v = robot.split(" ")
        p = tuple(map(int, p.split("=")[1].split(",")))
        v = tuple(map(int, v.split("=")[1].split(",")))
        
        finalX = (p[0] + v[0]*simTime) % mapX
        finalY = (p[1] + v[1]*simTime) % mapY
        grid[finalY][finalX] = "#"
        
    strGrid = ["".join(row) for row in grid]
    if any(("#####" in row for row in strGrid)):
        for row in strGrid:
            print(row)
        print(simTime)
        if input() == "-":
            simTime -= 2
    simTime += 1
    