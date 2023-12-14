with open("5.txt") as f:
    cont = f.read().splitlines()

niceWords = 0

for word in cont:
    if sum([word.count(v) for v in "aeiou"]) < 3:
        continue

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            break
    else:
        continue
    for i in ["ab", "cd", "pq", "xy"]:
        if i in word:
            break
    else:
        niceWords += 1

print(niceWords)
