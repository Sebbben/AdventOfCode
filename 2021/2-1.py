with open("2.txt") as f:
    cont = f.read().splitlines()

deapth = 0
forward = 0

for i in cont:
    num = int(i.split(" ")[1])
    if i.startswith("forward"):
        forward += num
    else:
        deapth += num if i.startswith("down") else -num

print(deapth,forward,deapth*forward)