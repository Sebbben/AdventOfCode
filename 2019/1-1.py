with open("1.txt") as f:
    cont = f.read().splitlines()

tot = 0
for i in cont:
    tot += (int(i) // 3)-2

print(tot)