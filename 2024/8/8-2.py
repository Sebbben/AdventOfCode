with open("8.txt", "r") as f:
    grid = f.read().splitlines()

locations = {}
antinodes = set()

for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if tile == ".": continue
        if tile not in locations:
            locations[tile] = [(x,y)]
            continue
        
        for x2,y2 in locations[tile]:
            dx = x2-x
            dy = y2-y

            while 0 <= x2 < len(row) and 0 <= y2 < len(grid):
                x2 -= dx
                y2 -= dy

            x2 += dx
            y2 += dy
            
            while 0 <= x2 < len(row) and 0 <= y2 < len(grid):
                antinodes.add((x2,y2))
                x2 += dx
                y2 += dy


        locations[tile].append((x,y))



print(len(antinodes))