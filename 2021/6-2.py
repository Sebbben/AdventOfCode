from collections import Counter,deque
with open("6.txt") as f:
    cont = f.read().split(",")

# cont = "3,4,3,1,2".split(",")

fishes = [int(i) for i in cont]

fishes = dict(Counter(cont))

for i in range(9):
    if str(i) not in fishes.keys():
        fishes[str(i)] = 0
        

print(fishes)

for _ in range(256):
    zeroes = fishes["0"]
    fishes["0"] = fishes["1"]
    fishes["1"] = fishes["2"]
    fishes["2"] = fishes["3"]
    fishes["3"] = fishes["4"]
    fishes["4"] = fishes["5"]
    fishes["5"] = fishes["6"]
    fishes["6"] = fishes["7"]
    fishes["7"] = fishes["8"]
    fishes["6"] += zeroes
    fishes["8"] = zeroes
    print(fishes)

fishes = Counter(fishes)
print(sum(fishes.values()))