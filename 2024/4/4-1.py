with open("4.txt", "r") as f:
    lines = f.read().splitlines()

def countXmas(x,y) -> int:
    tests = (
        ((0,0), (0,-1), (0,-2), (0,-3)),
        ((0,0), (1,-1), (2,-2), (3,-3)),
        ((0,0), (1,0), (2,0), (3,0)),
        ((0,0), (1,1), (2,2), (3,3)),
        ((0,0), (0,1), (0,2), (0,3)),
        ((0,0), (-1,1), (-2,2), (-3,3)),
        ((0,0), (-1,0), (-2,0), (-3,0)),
        ((0,0), (-1,-1), (-2,-2), (-3,-3))
    )

    tot = 0

    for test in tests:
        text = ""
        for dx, dy in test:
            if not (0<= x+dx < len(lines[y])): break
            if not (0<= y+dy < len(lines)): break
            text += lines[y+dy][x+dx]
        if text == "XMAS":
            tot += 1
    
    return tot

tot = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "X":
            tot += countXmas(x,y)

print(tot)