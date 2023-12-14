from collections import Counter

with open("10.txt") as f:
    cont = f.read().splitlines()

counter = Counter()

for line in cont:
    opened = []
    for chr in line:
        if chr in ("(","[","{","<"):
            opened.append(chr)
        else:
            if chr == ")" and opened[-1]=="(":
                opened.pop()
            elif chr == "]" and opened[-1]=="[":
                opened.pop()
            elif chr == "}" and opened[-1]=="{":
                opened.pop()
            elif chr == ">" and opened[-1]=="<":
                opened.pop()
            else:
                print("err",chr)
                counter.update(chr)
                break


counter = dict(counter)
print(counter[")"]*3 + counter["]"]*57 + counter["}"]*1197 + counter[">"]*25137)

