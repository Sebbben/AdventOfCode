with open("2.txt") as f:
    cont = [[int(j) for j in i.split("x")] for i in f.read().splitlines()]

tot = 0

for gift in cont:
    tot += 2*sum(sorted(gift)[0:2])  # the band that goes arround the package
    tot += gift[0]*gift[1]*gift[2]  # for the ribbon on top

print(tot)
