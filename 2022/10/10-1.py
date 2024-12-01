with open("10.txt") as f:
    data = [x.split(" ") for x in f.read().splitlines()]


cycles = 0
reg = 1
tot = 0
nextCheck = 20
for instr in data:
    instrCycles={"noop":1, "addx":2}[instr[0]]
    if cycles < nextCheck and cycles+instrCycles >= nextCheck:
        print(reg*nextCheck, reg, nextCheck)
        tot += reg*nextCheck
        nextCheck += 40
    if instr[0] == "addx":
        print(instr)
        reg += int(instr[1])
    if nextCheck > 240: break

    cycles += instrCycles
    

print(tot)