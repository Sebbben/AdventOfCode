with open("8-test.txt", "r") as f:
    content = f.read()
    lineLen = len(content.splitlines()[0])
    tiles = "".join(content.splitlines())

antinodes = set()
locations = {}

def locConvert(loc):
    return loc%lineLen, loc//lineLen

for i, tile in enumerate(tiles):
    if tile == ".": continue
    if tile not in locations:
        locations[tile] = [i]
        continue
    

    for location in locations[tile]:
        currLineNum = i // lineLen
        locLineNum = location // lineLen
        dy = (currLineNum) - (locLineNum)
        dx = i-location

        antinodeLoc1 = i+dx
        antinodeLoc2 = location-dx

        if antinodeLoc1//lineLen-currLineNum == dy and antinodeLoc1 < len(tiles):
            antinodes.add(antinodeLoc1)

        if locLineNum-antinodeLoc2//lineLen == dy and antinodeLoc2 >= 0:
            antinodes.add(antinodeLoc2)
        
    locations[tile].append(i)

# for node in antinodes:
#     print(node, node%lineLen, node//lineLen)

print(len(antinodes))