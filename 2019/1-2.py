with open("1.txt") as f:
    cont = f.read().splitlines()

tot = 0
for i in cont:
    mass = int(i)
    while mass > 0:
        tot += max(((mass // 3)-2),0)
        mass = (mass // 3)-2

print(tot)