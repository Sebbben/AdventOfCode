# with open("inp.txt", "r") as f:
#     data = f.read().splitlines()

data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

# data = """..#
# ...
# #..""".splitlines()

print(len(data))
i = len(data) - 1
lineRef = "."*len(data[0])

yExps = [y for y in range(len(data)) if not("#" in data[y])]
data = ["".join([data[y][x] for y in range(len(data))]) for x in range(len(data[0]))]
xExps = [x for x in range(len(data)) if not("#" in data[x])]
data = ["".join([data[y][x] for y in range(len(data))]) for x in range(len(data[0]))]

coords = []

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            coords.append([x,y])

expAmount = 10


tot = 0
for i, gal1 in enumerate(coords):
    for j, gal2 in enumerate(coords[i+1:]):
        j = j + i + 1
        
        toAdd = 0
        
        for yEx in yExps:
            if gal1[1] < yEx < gal2[1] or gal1[1] > yEx > gal2[1]:
                print(gal1, gal2, yEx)
                toAdd += expAmount
                
        
        for xEx in xExps:
            if gal1[0] < xEx < gal2[0] or gal1[0] > xEx > gal2[0]:
                toAdd += expAmount
                
        # print(i,j, abs(gal2[0]-gal1[0]) + abs(gal2[1]-gal1[1]))
        tot += (max(gal2[0],gal1[0])-min(gal2[0],gal1[0]) + max(gal2[1],gal1[1])-min(gal2[1],gal1[1])) + toAdd

print(tot)