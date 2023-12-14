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

# data = """..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# ..........""".splitlines()

# data = """.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...""".splitlines()

# data = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L""".splitlines()

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

S = (data[y].index("S"),y)
queue = [(S,0)]
queueItems = set((S,))
pipes = set()

while queue:
    # print(queue)
    coords, dist = queue.pop(0)
    queueItems.remove(coords)
    pipes.add(coords)
    x,y = coords
    if x > 0 and conversions[data[y][x]] & 0b0001 and conversions[data[y][x-1]] & 0b0010: # Connect west
        coords = (x-1,y)
        if not coords in queueItems:
            if coords not in pipes:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:            
            pipes.add(coords)
            break
    
    if x < len(data[0])-1 and conversions[data[y][x]] & 0b0010 and conversions[data[y][x+1]] & 0b0001: # Connecting east
        coords = (x+1,y)
        if not coords in queueItems:
            if coords not in pipes:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:
            pipes.add(coords)
            break
    
    
    if y > 0 and conversions[data[y][x]] & 0b1000 and conversions[data[y-1][x]] & 0b0100: # Connect north
        coords = (x,y-1)
        if not coords in queueItems:
            if coords not in pipes:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:
            pipes.add(coords)
            break
    
    if y < len(data)-1 and conversions[data[y][x]] & 0b0100 and conversions[data[y+1][x]] & 0b1000: # Connecting south
        coords = (x,y+1)
        if not coords in queueItems:
            if coords not in pipes:
                queue.append((coords,dist+1))
                queueItems.add(coords)
        else:
            pipes.add(coords)
            break
        
        
n = ~conversions[data[S[1]-1][S[0]]]&0b0100 # Get wether the node to the north has a connection south
s = ~conversions[data[S[1]+1][S[0]]]&0b1000 # Get wether the node to the north has a connection south
e = ~conversions[data[S[1]][S[0]+1]]&0b0001 # Get wether the node to the north has a connection south
w = ~conversions[data[S[1]][S[0]-1]]&0b0010 # Get wether the node to the north has a connection south
 
 
startShouldBe = n^s^e^w


for fromCon, toCon in conversions.items():
    if toCon == startShouldBe:
        start = fromCon
        break

data[S[1]] = data[S[1]].replace("S", start)    
    
parent = {}
roots = {}
visited = set()

for y, row in enumerate(data):
    for x, entry in enumerate(row):
        coords = (x,y)
        if coords in visited or coords in pipes: continue
        
        print("New component at",coords)
        
        queue = [coords]
        parent[coords] = coords
        roots[coords] = set((coords,))
        ## BFS
        while queue:
            # print(queue)
            node = queue.pop()
            nX, nY = node
            visited.add(node)
            for dy in range(-1,2):
                if not (0 <= nY+dy <= len(data)-1): continue
                for dx in range(-1,2):
                    if not (0 <= nX+dx <= len(data[0])-1): continue
                    if dx == 0 and dy == 0: continue
                    coord = (nX+dx, nY+dy)
                    # print(dx,dy,coord)
                    
                    if coord not in visited and coord not in pipes:
                        queue.append(coord)
                        par = coords
                        while par != parent[par]:
                            par = parent[par]    
                                                
                        parent[coord] = par
                        roots[par].add(coord)
                            

tot = 0
for par, num in roots.items():
    count = 0
    print(par, num)
    dirs = 0b0000
    for y in range(par[1],-1,-1):
        if (par[0],y) in pipes:
            dirs ^= conversions[data[y][par[0]]]&0b0011
            print(data[y][par[0]], bin(conversions[data[y][par[0]]] & 0b0011), "-> ",bin(dirs))
            
    if dirs&0b0011:
        print("added")
        tot += len(num)
print(tot)

# onInside = []

# for pipePiece, coord in nextToStraight:
#     # print(pipePiece, coord)
#     if data[pipePiece[1]][pipePiece[0]] == "|":
#         if coord[0]<pipePiece[0]:
#             direction=(0,1)
#         else:
#             direction=(0,-1)
#     else:
#         if coord[1]<pipePiece[1]:
#             direction=(-1,0)
#         else:
#             direction=(1,0)
    
#     x,y = pipePiece
#     x += direction[0]
#     y += direction[1]
    
#     rights = 1
#     # print(coord)
#     while x!=pipePiece[0] or y != pipePiece[1]:
#         # print(data[y][x],x,y)
#         if data[y][x] == "7":
#             if direction == (1,0):
#                 rights += 1
#                 direction = (0,1)
#             else:
#                 rights -= 1
#                 direction = (-1,0)
#         elif data[y][x] == "L":
#             if direction == (-1, 0):
#                 rights += 1
#                 direction = (0,-1)
#             else:
#                 rights -= 1
#                 direction = (1,0)
#         elif data[y][x] == "J":
#             if direction == (0,1):
#                 rights += 1
#                 direction = (-1,0)
#             else:
#                 rights -= 1
#                 direction = (0,-1)
#         elif data[y][x] == "F":
#             if direction == (0,-1):
#                 rights += 1
#                 direction = (1,0)
#             else:
#                 rights -= 1
#                 direction = (0,1)
#         elif data[y][x] == "S":
#             if direction == (0,1):
#                 if data[y][x-1] in ["F","L", "-"]:
#                     rights += 1
#                     direction = (-1,0)
#                 else:
#                     rights -= 1
#                     direction = (1,0)
#             elif direction == (-1,0):
#                 if data[y-1][x] in ["F","7", "|"]:
#                     rights += 1
#                     direction = (0,-1)
#                 else:
#                     rights -= 1
#                     direction = (0,1)
#             elif direction == (0,-1):
#                 if data[y][x+1] in ["J","7", "-"]:
#                     rights += 1
#                     direction = (0,1)
#                 else:
#                     rights -= 1
#                     direction = (0,-1)
#             elif direction == (1,0):
#                 if data[y+1][x] in ["L","J", "|"]:
#                     rights += 1
#                     direction = (0,1)
#                 else:
#                     rights -= 1
#                     direction = (0,-1)
                
                    
                
#         x += direction[0]
#         y += direction[1]

#     if rights == 5:
#         onInside.append(parent[coord])
    
# tot = 0

# for coord, par in parent.items():
#     if par in onInside:
#         tot += 1

# print(tot)
