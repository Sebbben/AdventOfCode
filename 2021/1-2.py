with open("1.txt") as f:
    cont = f.read().splitlines()

cont = [int(i) for i in cont]

print([sum(cont[i: i+3]) < sum(cont[i+1:i+4])
      for i in range(len(cont)-1)].count(True))
