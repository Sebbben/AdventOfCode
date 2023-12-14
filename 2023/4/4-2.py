with open("inp.txt", "r") as f:
    data = f.read().splitlines()

import itertools

tot = 0
amount = [0]
for ind, line in enumerate(data):
    line = line.replace("  ", " ").split(": ")[1]
    winners, numbers = line.split(" | ")
    winners = set(winners.split(" "))
    numbers = set(numbers.split(" "))

    matches = len(winners & numbers)
    cardCount = amount.pop(0)+1 if len(amount) != 0 else 1
    amount = itertools.zip_longest([cardCount]*matches, amount, fillvalue=0)
    amount = list(map(lambda a: a[0]+a[1], amount))
    tot += cardCount

print(tot)
