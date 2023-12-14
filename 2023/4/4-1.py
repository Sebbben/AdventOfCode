with open("inp.txt", "r") as f:
    data = f.read().splitlines()

tot = 0

for line in data:
    line = line.replace("  ", " ").split(": ")[1]
    winners, numbers = line.split(" | ")
    winners = set(winners.split(" "))
    numbers = set(numbers.split(" "))

    matches = len(winners & numbers)
    if matches > 0:
        tot += 2**(matches-1)

print(tot)