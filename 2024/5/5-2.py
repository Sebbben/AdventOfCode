with open("5.txt", "r") as f:
    rules, updates = map(lambda x: x.splitlines(), f.read().split("\n\n"))

blockings = {}
comeLater = {}
for rule in rules:
    first, last = rule.split("|")
    first, last = int(first), int(last)
    if last not in blockings:
        blockings[last] = []
    if first not in comeLater:
        comeLater[first] = []
    blockings[last].append(first)
    comeLater[first].append(last)


tot = 0

def getCorrect(update):
    newUpdate = []
    for num in update:
        i = 0
        for i in range(len(newUpdate)-1, -1, -1):
            if num in comeLater and newUpdate[i] in comeLater[num]:
                i += 1
                break
        newUpdate.insert(i,num)
    
    return newUpdate



def getBreakingNums(update):
    broken = []
    breakingNums = set()
    for num in update:
        if num in breakingNums: broken.append(num)
        if num in blockings:
            breakingNums.update(blockings[num])
    
    return broken



for update in updates:
    update = list(map(int, update.split(",")))

    print("Update:", update)

    if getBreakingNums(update):
        correct = getCorrect(update)
        print(correct)
        tot += correct[len(correct)//2]

print(tot)