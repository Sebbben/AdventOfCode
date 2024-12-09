from itertools import product

with open("7.txt", "r") as f:
    tests = f.read().splitlines()


tot = 0
for test in tests:
    tRes, vals = test.split(": ")
    vals = vals.split(" ")

    perms = product(["+","*"], repeat=len(vals)-1)
    for perm in perms:

        res = int(vals[0])
        for i, opr in enumerate(perm):
            if opr == "+":
                res += int(vals[i+1])
            else:
                res *= int(vals[i+1])

        if int(res) == int(tRes):
            tot += int(res)
            break

print(tot)