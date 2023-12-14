with open("inp.txt", "r") as f:
    data = [list(line) for line in f.read().splitlines()]

# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()

# data = [list(line) for line in data]

def getSurounding(matrix, pos):
    maxX = len(matrix[0])
    maxY = len(matrix)
    
    neighbors = {}
    
    for x in range(-1,2):
        if not ( 0 <= (pos[0] + x) < maxX ): continue
        for y in range(-1,2):
            if not ( 0 <= (pos[1] + y) < maxY ): continue
            # print(x,y)
            neighbors[f"{pos[0]+x},{pos[1]+y}"] = matrix[pos[1]+y][pos[0]+x]
            
    return neighbors
           
def getNum(matrix, pos):
    x = pos[0]
    
    while x >= 0 and matrix[pos[1]][x].isnumeric():
        x-=1
    
    x += 1
    numStr = ""
    coords = set()
    
    while x<len(matrix[pos[1]]) and matrix[pos[1]][x].isnumeric():
        numStr += matrix[pos[1]][x]
        coords.add((x,pos[1]))
        x+=1
        
    return int(numStr), coords
         
checkedCoords = set()           
tot = 0

for y, yList in enumerate(data):
    for x, val in enumerate(yList):
        if val == "*":
            surounding = getSurounding(data, (x,y))
            uniqueParts = set()
            for pos in surounding:
                posList = list(map(int,pos.split(",")))
                if not (tuple(posList) in checkedCoords) and surounding[pos].isnumeric():
                    num, coords = getNum(data, posList)
                    uniqueParts.add(num)
                    checkedCoords.update(coords)
            if len(uniqueParts) == 2:
                parts = 1
                for part in uniqueParts: parts*=part
                
                tot += parts                    
                    
print(tot)