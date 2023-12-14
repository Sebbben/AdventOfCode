with open("8.txt") as f:
    cont = f.read().splitlines()

counter = 0
for i in cont:
    i = i.split(" | ")[1]
    lengths = [len(x) for x in i.split(" ")]
    counter += lengths.count(2)
    counter += lengths.count(4)
    counter += lengths.count(3)
    counter += lengths.count(7)

print(counter)