from collections import Counter

with open("2.txt") as f:
    cont = f.read().splitlines()

score = 0

outcome = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

freq = Counter(cont)


for line in freq:
    score += outcome[line]*freq.get(line)

print(score)
