from collections import Counter

with open("5.txt") as f:
    cont = f.read().splitlines()

points = []
for line in cont:
    start, end = line.split(" -> ")
    x1,y1 = start.split(",")
    x2,y2 = end.split(",")
    if x1 == x2 or y1 == y2:
        x1,x2 = sorted([int(x1),int(x2)])
        y1,y2 = sorted([int(y1),int(y2)])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                points.append(f"{x},{y}")


ventdict = Counter(points)
            
tot = 0
for i in ventdict.keys():
    if ventdict.get(i) >= 2:
        print(ventdict[i])
        tot += 1

print(tot)