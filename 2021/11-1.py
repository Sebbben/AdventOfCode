with open("11-test.txt") as f:
    cont = [[int(x) for x in i]  for i in f.read().splitlines()]

class Octopus:
    def __init__(self, energy, grid):
        self.energy = energy
        self.grid = grid
        self.pos = []

        for i in range(len(grid)):
            if self in self.grid[i]:
                ind = self.grid[i].index(self)
                self.pos = [i,ind]
                break

    def incrementEnergy(self):
        self.energy += 1


    def blink(self):
        if self.energy >= 10:
            self.energy = 0
 

grid = []

for row in cont:
    grid.append([Octopus(x,grid) for x in row])

steps = 1

for _ in range(steps):
    for row in grid:
        for octo in row:
            octo.incrementEnergy()
    
    for row in grid:
        for octo in row:
            octo.blink()
