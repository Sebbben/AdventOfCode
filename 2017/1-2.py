
with open("1.txt") as f:
    data = list(f.read())

data = [int(x) for x in data]

tot = 0

offset = len(data)//2

for i in range(len(data)):
    print(data[i], data[(i+offset)%len(data)])
    if data[i] == data[(i+offset)%len(data)]:
        tot += data[i]


print(tot)