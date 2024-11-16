from collections import Counter
import numpy as np
import math

with open("9.txt") as f:
    data = [x.split(" ") for x in f.read().splitlines()]


headPos = np.array([0,0])
tailPos = np.array([0,0])

uniquePos = set()
uniquePos.add(tailPos.tobytes())

for instruction in data:
    if instruction[0] == "R":
        dr = np.array([1,0])
    elif instruction[0] == "L":
        dr = np.array([-1,0])
    elif instruction[0] == "U":
        dr = np.array([0,-1])
    elif instruction[0] == "D":
        dr = np.array([0,1])
    for i in range(int(instruction[1])):
        newheadPos = headPos + dr
        dist = newheadPos-tailPos
        if math.sqrt((dist[0]**2) + (dist[1]**2)) >= 2:
            tailPos = headPos
            uniquePos.add(tailPos.tobytes())

        headPos = newheadPos


print(len(uniquePos))