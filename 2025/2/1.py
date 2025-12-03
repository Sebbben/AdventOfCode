import re

data = None

with open("input.txt") as f:
    data = re.findall(r"(\d+)-(\d+)", f.read())

tot = 0

for pair in data:
    for i in range(int(pair[0]), int(pair[1])):
        strInt = str(i)
        if strInt[:len(strInt)//2] == strInt[len(strInt)//2:]:
            tot += i

print(tot)