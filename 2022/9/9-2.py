with open("9.txt") as f:
    data = [x.split(" ") for x in f.read().splitlines()]




dirMap = {
    "R": [1,0],
    "L": [-1,0],
    "U": [0,1],
    "D": [0,-1],
}

def sqrDist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

knots = [[0 for _ in range (2)] for __ in range(10)]
locations = set()

for i, instruction in enumerate(data):
    print(i,instruction)
    direction = dirMap[instruction[0]]
    amount = int(instruction[1])
    for _ in range(amount):
        knots[0][0] += direction[0]
        knots[0][1] += direction[1]

        for i, knot in enumerate(knots[1:]):
            if sqrDist(knot, knots[i]) >= 2**2:
                if knot[0] == knots[i][0]: # Same column
                    if knot[1] > knots[i][1]: # If current above last, move down one
                        knot[1] -= 1
                    else: # If current below last, move up one
                        knot[1] += 1
                elif knot[1] == knots[i][1]: # Same row
                    if knot[0] > knots[i][0]: # If current to the right of last, move left
                        knot[0] -= 1
                    else: # If current to left of last, move to the right
                        knot[0] += 1
                elif knot[0] > knots[i][0] and knot[1] > knots[i][1]: # Current is above and to the right of last
                    knot[0] -= 1
                    knot[1] -= 1
                elif knot[0] < knots[i][0] and knot[1] > knots[i][1]: # Current is below and to the right of last
                    knot[0] += 1
                    knot[1] -= 1
                elif knot[0] > knots[i][0] and knot[1] < knots[i][1]: # Current is above and to the left of last
                    knot[0] -= 1
                    knot[1] += 1
                elif knot[0] < knots[i][0] and knot[1] < knots[i][1]: # Current is below and to the left of last
                    knot[0] += 1
                    knot[1] += 1

        
        print(knots)
        locations.add(tuple(knots[-1]))


size = [600,400]
for j in range(size[1]):
    for i in range(size[0]):
        if (i-size[0]//2, -(j-size[1]//2)) == (0,0):
            print("s", end="")
        elif ((i-size[0]//2), -(j-size[1]//2)) == tuple(knots[-1]):
            print("O", end="")
        elif ((i-size[0]//2),-(j-size[1]//2)) in locations:
            print("#", end="")
        else:
            print(".", end="")

    print("", end="\n")
print(len(locations))