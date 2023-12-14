with open("1.txt") as f:
    cont = f.read().splitlines()

print([int(cont[i]) < int(cont[i+1])
      for i in range(len(cont)-1)].count(True))
