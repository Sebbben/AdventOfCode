with open("inp.txt", "r") as f:
    data = f.read().splitlines()

# data = """..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...""".splitlines()

# data = """.....
# .S-7.
# .|.|.
# .L-J.
# .....""".splitlines()

conversions = {
    "|": 0b1100,
    "-": 0b0011,
    "L": 0b1010,
    "J": 0b1001,
    "7": 0b0101,
    "F": 0b0110,
    ".": 0b0000,
    "S": 0b1111,
}

y = 0
while "S" not in data[y]:
    y += 1

queue = [((data[y].index("S"),y),0)]
queueItems = set(((data[y].index("S"),y),))
visited = set()

while queue:
    print(queue)
    coords, dist = queue.pop(0)
    queueItems.remove(coords)
    visited.add(coords)
    x,y = coords
    if x > 0 and conversions[data[y][x]] & 0b0001 and conversions[data[y][x-1]] & 0b0010: # Connect west
        coords = (x-1,y)
        if not coords in queueItems:
            if coords not in visited:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:
            print(dist+1, "W")
            break
    
    if x < len(data[0])-1 and conversions[data[y][x]] & 0b0010 and conversions[data[y][x+1]] & 0b0001: # Connecting east
        coords = (x+1,y)
        if not coords in queueItems:
            if coords not in visited:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:
            print(dist+1,"E")
            break
    
    
    if y > 0 and conversions[data[y][x]] & 0b1000 and conversions[data[y-1][x]] & 0b0100: # Connect north
        coords = (x,y-1)
        if not coords in queueItems:
            if coords not in visited:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:
            print(dist+1,"N")
            break
    
    if y < len(data)-1 and conversions[data[y][x]] & 0b0100 and conversions[data[y+1][x]] & 0b1000: # Connecting south
        coords = (x,y+1)
        if not coords in queueItems:
            if coords not in visited:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:
            print(dist+1,"S")
            break
    














# maze = [[conversions[x] for x in y] for y in data]

# components = {f"{x}:{y}":f"{x}:{y}" for x in range(len(maze[0])) for y in range(len(maze))}

# for y, row in enumerate(maze):
#     for x, entry in enumerate(row):
#         if y > 0 and 0b1100 & entry[0] & maze[y-1][x][1]: # connect north
#             components[f"{x}:{y}"]
#         0b1100 & entry[0] & maze[y+1][x][1] # connect south
#         0b1100 & entry[0] & maze[y][x-1][1] # connect east
#         0b1100 & entry[0] & maze[y][x+1][1] # connect west
        
        
            