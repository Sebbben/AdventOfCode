with open("7.txt") as f:
    cont = f.read().split(",")

cont = [int(i) for i in cont]

minimumFuel = 10000000

for i in range(min(cont),max(cont)):
    fuelUsed = sum([abs(i-x) for x in cont])
    minimumFuel = min(minimumFuel,fuelUsed)

    print(i,minimumFuel,fuelUsed)