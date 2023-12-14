with open("3.txt") as f:
    cont = f.read().splitlines()

wire1 = cont[0].split(",")
wire2 = cont[1].split(",")

coords = {"x":0,"y":0}
wire1Path = []

for inst in wire1:
    wire1Path.append([])
    wire1Path[-1].append(coords.copy())
    if inst[0] == "U":
        coords["y"] += int(inst[1:])
    elif inst[0] == "D":
        coords["y"] -= int(inst[1:])
    elif inst[0] == "R":
        coords["x"] += int(inst[1:])
    elif inst[0] == "L":
        coords["x"] -= int(inst[1:])
    wire1Path[-1].append(coords.copy())
    wire1Path[-1].append(int(inst[1:]))

for i in wire1Path:
    print(i)

coords = {"x":0,"y":0}
wire2Path = []

for inst in wire2:
    wire2Path.append([])
    wire2Path[-1].append(coords.copy())
    if inst[0] == "U":
        coords["y"] += int(inst[1:])
    elif inst[0] == "D":
        coords["y"] -= int(inst[1:])
    elif inst[0] == "R":
        coords["x"] += int(inst[1:])
    elif inst[0] == "L":
        coords["x"] -= int(inst[1:])
    wire2Path[-1].append(coords.copy())

crossings = []

for p1 in wire1Path:
    for p2 in wire2Path:
        if (p1[0]["x"] == p1[1]["x"] and p2[0]["x"] == p2[1]["x"]) or (p1[0]["y"] == p1[1]["y"] and p2[0]["y"] == p2[1]["y"]):
            continue

        if p1[0]["x"] == p1[1]["x"]:
            if min(p2[0]["x"],p2[1]["x"]) < p1[0]["x"] < max(p2[0]["x"],p2[1]["x"]):
                if min(p1[0]["y"],p1[1]["y"]) < p2[0]["y"] < max(p1[0]["y"],p1[1]["y"]):
                    crossings.append({"x": p1[0]["x"], "y":p2[0]["y"]})
        else:
            if min(p2[0]["y"],p2[1]["y"]) < p1[0]["y"] < max(p2[0]["y"],p2[1]["y"]):
                if min(p1[0]["x"],p1[1]["x"]) < p2[0]["x"] < max(p1[0]["x"],p1[1]["x"]):
                    crossings.append({"y": p1[0]["y"], "x":p2[0]["x"]})

minLen = 10000000000000000000
for cross in crossings:
    minLen = min(abs(cross["x"]) + abs(cross["y"]), minLen)

print(minLen)