with open("3.txt") as f:
    cont = f.read()

x, y = 0, 0
positions = {}

for i in cont:
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == "<":
        x -= 1
    else:
        x += 1

    if f"{x},{y}" in positions.keys():
        positions[f"{x},{y}"] += 1
    else:
        positions[f"{x},{y}"] = 1

tot = 0
for i in positions.keys():
    if positions[i] >= 1:
        tot += 1

print(tot)
