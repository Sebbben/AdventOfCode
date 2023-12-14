r = range(264360,746325)

paswrds = 0

for num in r:
    snum = str(num)

    if all(int(snum[i]) <= int(snum[i+1]) for i in range(len(snum)-1)):
        if any(snum[i] == snum[i+1] for i in range(len(snum)-1)):
            paswrds += 1

print(paswrds)
