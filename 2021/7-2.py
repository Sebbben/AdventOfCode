with open("7.txt") as f:
    cont = f.read().split(",")

cont = [int(i) for i in cont]

minimumFuel = sum([sum(range(abs(cont[0]-x)+1)) for x in cont])

for i in range(min(cont),max(cont)):
    fuelUsed = sum([sum(range(abs(i-x)+1)) for x in cont])
    minimumFuel = min(minimumFuel,fuelUsed)

    print(i,minimumFuel,fuelUsed)