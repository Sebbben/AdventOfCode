with open("1.txt") as f:
    cont = f.read()

floor = 1

for i in range(len(cont)):
    if cont[i] == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        print(i)
        break
