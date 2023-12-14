with open("2.txt") as f:
    data = f.read().splitlines()

data = [[int(x) for x in row.split(",")] for row in data]

sum = 0

for row in data:
    print(max(row)-min(row))
    sum += max(row)-min(row)


print("Sum: ", sum)