with open("2.txt") as f:
    cont = [int(i) for i in f.read().split(",")]

print(cont)

cont[1] = 12
cont[2] = 2

for i in range(0,len(cont), 4):
    op = cont[i:i+4]
    if op[0] == 1:
        cont[op[3]] = cont[op[1]] + cont[op[2]]
    elif op[0] == 2:
        cont[op[3]] = cont[op[1]] * cont[op[2]]
    elif op[0] == 99:
        break

print(cont[0])