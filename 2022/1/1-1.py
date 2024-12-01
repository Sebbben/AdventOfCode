with open("1.txt") as f:
    cont = f.read().split("\n\n")


print(max([sum(list(map(int,x.splitlines()))) for x in cont]))

data = []


for i in cont:
    data.append(sum(list(map(int, i.splitlines()))))


print(max(data))