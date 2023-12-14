with open("5.txt") as f:
    data = f.read().splitlines()

data = [int(x) for x in data]

steps = 0
index = 0

while index < len(data):
    data[index] += 1
    index += data[index]-1
    steps += 1

print(steps)