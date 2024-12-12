with open("5.txt", "r") as f:
    rules, updates = map(lambda x: x.splitlines(), f.read().split("\n\n"))

needs = {}

for rule in rules:
    first, last = rule.split("|")
    first, last = int(first), int(last)
    if last not in needs:
        needs[last] = []
    needs[last].append(first)

tot = 0

for update in updates:
    update = list(map(int, update.split(",")))

    print("Update:", update)

    breakingNums = set()
    validUpdate = True
    for num in update:
        if num in breakingNums:
            validUpdate = False
            break
            
        if num in needs:
            breakingNums.update(needs[num])
        print(breakingNums)
        
    if validUpdate:
        print(update)
        tot += update[len(update)//2]

print(tot)