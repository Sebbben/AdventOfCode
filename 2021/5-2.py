from collections import Counter

with open("5.txt") as f:
    cont = f.read().splitlines()

points = []
for line in cont:
    start, end = line.split(" -> ")
    x1,y1 = start.split(",")
    x2,y2 = end.split(",")

    x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)

    if x1 == x2 or y1 == y2:
        x1,x2 = sorted([x1,x2])
        y1,y2 = sorted([y1,y2])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                points.append(f"{x},{y}")
    else:
        if x1>x2:
            xValues = list(reversed(list(range(x2,x1+1))))
        else:
            xValues = list(range(x1,x2+1))
        if y1>y2:
            yValues = list(reversed(list(range(y2,y1+1))))
        else:
            yValues = list(range(y1,y2+1))

        for i in range(len(xValues)):
            points.append(f"{xValues[i]},{yValues[i]}")


ventdict = Counter(points)
            
tot = 0
for i in ventdict.keys():
    if ventdict.get(i) >= 2:
        tot += 1

print(tot)