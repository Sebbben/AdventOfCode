with open("4.txt") as f:
    data = f.read().splitlines()

numberOfValid = 0

for passphrase in data:
    pp = passphrase.split(" ")
    if all([pp.count(i) == 1 for i in pp]):
        numberOfValid += 1

print(numberOfValid)
