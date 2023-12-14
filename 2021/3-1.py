with open("3.txt") as f:
    cont = f.read().splitlines()

gamma = ""

for i in range(len(cont[0])):
    pos = [j[i] for j in cont]
    gamma += str(int(pos.count("0") < pos.count("1")))

epsilon = "".join(["0" if i=="1" else "1" for i in gamma])

print(int(gamma,2)*int(epsilon,2))