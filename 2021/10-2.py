with open("10.txt") as f:
    cont = f.read().splitlines()

scores = []

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
                break
    else:
        opened = list(reversed(opened))
        s = 0
        for i in opened:
            s *= 5
            if i == "(":
                s+=1
            elif i == "[":
                s+=2
            elif i == "{":
                s+=3
            elif i == "<":
                s+=4
        scores.append(s)

print(list(sorted(scores))[len(scores)//2])