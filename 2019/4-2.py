r = range(264360,746325)

paswrds = 0

for num in r:
    snum = str(num)

    if all(int(snum[i]) <= int(snum[i+1]) for i in range(len(snum)-1)):
        if any(str(i)*2 in snum and not str(i)*3 in snum for i in range(10)):
            paswrds += 1

print(paswrds)
