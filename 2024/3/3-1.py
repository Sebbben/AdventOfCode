import re
with open("3.txt", "r") as f:
    mem = f.read()


muls = re.findall(r"mul\((\d+),(\d+)\)", mem)

print(sum((int(a)*int(b) for a, b in muls)))
