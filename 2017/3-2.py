import numpy as np

target = 265149

direction = "Right"
spiral = np.ones((1,1))
pos = [0,0]

while spiral[pos[0]][pos[1]] < target:
    if direction == "Right":
        pos[1] += 1
    elif direction == "Left":
        pos[1] -= 1
    elif direction == "Up":
        pos[0] -= 1
    elif direction == "Down":
        pos[0] += 1
    
    

    

print(spiral[pos[0],pos[1]])