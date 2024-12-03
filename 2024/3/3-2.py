import re
with open("3.txt", "r") as f:
    mem = f.read()


muls = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", mem)

do = True
tot = 0
for a,b,c,d in muls:
    if c: do = True
    if d: do = False
    if do and a and b: tot += int(a)*int(b)


print(tot)