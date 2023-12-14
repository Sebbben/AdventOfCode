with open("3.txt") as f:
    cont = f.read()

x1, y1 = 0, 0
x2, y2 = 0, 0
santasSurn = True

positions = {}

for i in cont:
    if santasSurn:
        if i == "^":
            y1 += 1
        elif i == "v":
            y1 -= 1
        elif i == "<":
            x1 -= 1
        else:
            x1 += 1

        if f"{x1},{y1}" in positions.keys():
            positions[f"{x1},{y1}"] += 1
        else:
            positions[f"{x1},{y1}"] = 1
    else:
        if i == "^":
            y2 += 1
        elif i == "v":
            y2 -= 1
        elif i == "<":
            x2 -= 1
        else:
            x2 += 1

        if f"{x2},{y2}" in positions.keys():
            positions[f"{x2},{y2}"] += 1
        else:
            positions[f"{x2},{y2}"] = 1
    santasSurn = not santasSurn

tot = 0
for i in positions.keys():
    if positions[i] >= 1:
        tot += 1

print(tot)
