import re

data = None

with open("input.txt") as f:
    data = re.findall(r"(\d+)-(\d+)", f.read())

tot = 0

for pair in data:
    for i in range(int(pair[0]), int(pair[1])+1):
        strInt = str(i)
        for j in range(1, len(strInt)//2+1):
            if strInt[:j]*((len(strInt)//(j))) == strInt:
                tot += i
                break

print(tot)