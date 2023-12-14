with open("5.txt") as f:
    cont = f.read().splitlines()

niceWords = 0

for word in cont:

    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            break
    else:
        continue

    for i in range(len(word)-3):
        sub = word[i:i+2]
        if word.count(sub) == 2:
            break
    else:
        continue

    niceWords += 1

print(niceWords)
