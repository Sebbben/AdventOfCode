with open("6.txt") as f:
    data = f.read().splitlines()

data = [int(i) for i in data]

seenConfigs = []
cycles = 0

while str(data) not in seenConfigs:
    cycles += 1
    seenConfigs.append(str(data))

    print(data)
    m = max(data)
    begin = data.index(m)
    end = data.index(m)+m
    data[data.index(m)] = 0
    for i in range(begin+1, end+1):
        data[i%len(data)] += 1

    


print(cycles)