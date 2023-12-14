from math import *

inp = 265149

nearestSquare = ceil(sqrt(inp))

print(nearestSquare)

print(nearestSquare**2-inp)
print(nearestSquare-(nearestSquare**2-inp)-1)