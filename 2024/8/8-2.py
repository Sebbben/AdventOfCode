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

        antinodeLoc = location-dx

        print(locConvert(i), locConvert(location))

        while currLineNum - ((antinodeLoc+1)//lineLen) == dy and antinodeLoc >= 0:
            antinodeLoc -= dx
            currLineNum -= dy

        
        currLineNum = (antinodeLoc-dx) // lineLen

        while (antinodeLoc+1)//lineLen - currLineNum == dy and antinodeLoc < len(tiles):
            print("gre", locConvert(antinodeLoc))
            antinodeLoc += dx
            currLineNum += dy
            antinodes.add(antinodeLoc)

        print(locConvert(antinodeLoc))
        print((antinodeLoc+1)//lineLen - currLineNum == dy , antinodeLoc < len(tiles))

    locations[tile].append(i)

# for node in antinodes:
#     print(node, node%lineLen, node//lineLen)

print(len(antinodes))