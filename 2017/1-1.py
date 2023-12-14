
with open("1.txt") as f:
    data = list(f.read())

print(sum([int(data[i]) if data[i] == data[i+1] else 0 for i in range(-1,len(data)-1)]))