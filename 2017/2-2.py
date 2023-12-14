with open("2.txt") as f:
    data = f.read().splitlines()

data = [[int(x) for x in row.split(",")] for row in data]

sum = 0

for row in data:
    for i in range(len(row)):
        for j in range(len(row)):
            if i==j: continue
            if row[i]%row[j] == 0:
                print(row[i],row[j])
                sum += row[i]//row[j]


print("Sum: ", sum)