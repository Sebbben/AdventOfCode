from collections import Counter
with open("6.txt") as f:
    cont = f.read()

for i in range(len(cont)-4):
    check = Counter(cont[i:i+14])
    if check.most_common(1)[0][1] == 1:
        print(i+14)
        break
