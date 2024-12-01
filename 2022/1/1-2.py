with open("1.txt") as f:
    cont = f.read().split("\n\n")


data = []

for i in cont:
    data.append(sum(list(map(int, i.splitlines()))))

tot = 0

for i in range(3):
    tot += max(data)
    data.remove(max(data))

print(tot)