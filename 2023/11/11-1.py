with open("inp.txt", "r") as f:
    data = f.read().splitlines()

# data = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....""".splitlines()

print(len(data))
i = len(data) - 1

while i > 0:
    if not "#" in data[i]:
        data.insert(i, data[i])
    i -= 1

data = ["".join([data[y][x] for y in range(len(data))]) for x in range(len(data[0]))]

i = len(data) - 1
while i > 0:
    if not "#" in data[i]:
        data.insert(i, data[i])
    i -= 1

data = ["".join([data[y][x] for y in range(len(data))]) for x in range(len(data[0]))]

coords = []

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            coords.append((x,y))

tot = 0
for i, gal1 in enumerate(coords):
    for j, gal2 in enumerate(coords[i+1:]):
        j = j + i + 1
        print(i,j, abs(gal2[0]-gal1[0]) + abs(gal2[1]-gal1[1]))
        tot += abs(gal2[0]-gal1[0]) + abs(gal2[1]-gal1[1])

print(tot)