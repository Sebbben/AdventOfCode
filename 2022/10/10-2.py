with open("10.txt") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

crt = ""

cycles = 0
reg = 1
for instr in data:
    instrCycles={"noop":1, "addx":2}[instr[0]]

    for i in range(instrCycles):
        crt += "#" if -1 <= reg - ((cycles+i)%40) <= 1 else " "
        # print(cycles+i, reg, crt)
    
    if instr[0] == "addx":
        reg += int(instr[1])

    cycles += instrCycles
    


for i in range(0,len(crt), 40):
    print(crt[i:i+40])