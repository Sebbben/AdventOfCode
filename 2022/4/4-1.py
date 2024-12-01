with open("4.txt") as f:
    cont = [[list(map(int,line.split(",")[0].split("-"))), list(map(int,line.split(",")[1].split("-")))] for line in f.read().splitlines()]

tot = 0

for i in cont:
    if ((i[1][0] <= i[0][0] <= i[1][1]) and (i[1][0] <= i[0][1] <= i[1][1])) or ((i[0][0] <= i[1][0] <= i[0][1]) and (i[0][0] <= i[1][1] <= i[0][1])):
        tot += 1


print(tot)