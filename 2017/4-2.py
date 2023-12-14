from collections import Counter

with open("4.txt") as f:
    data = f.read().splitlines()

numberOfValid = 0

for line in data:
    isValid = True
    words = line.split(" ")
    for i,word in enumerate(words):
        letters = Counter(word)
        for j,word2 in enumerate(words):
            if i == j: continue
            if Counter(word2) == letters: isValid = False

        print(isValid)

    if isValid:
        numberOfValid += 1


print(numberOfValid)