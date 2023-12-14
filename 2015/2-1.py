with open("2.txt") as f:
    cont = [i.split("x") for i in f.read().splitlines()]

tot = 0

for gift in cont:
    a = int(gift[0])*int(gift[1])
    b = int(gift[1])*int(gift[2])
    c = int(gift[0])*int(gift[2])
    tot += min([a, b, c])
    tot += (2*a + 2*b + 2*c)

print(tot)
