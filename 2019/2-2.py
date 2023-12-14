with open("2.txt") as f:
    cont = [int(i) for i in f.read().split(",")]

noun = 0
verb = 0
target = 19690720

mem = [0]

while mem[0] != target:
    mem = cont.copy()
    mem[1] = noun
    mem[2] = verb

    for i in range(0,len(mem), 4):
        op = mem[i:i+4]
        if op[0] == 1:
            mem[op[3]] = mem[op[1]] + mem[op[2]]
        elif op[0] == 2:
            mem[op[3]] = mem[op[1]] * mem[op[2]]
        elif op[0] == 99:
            break
    
    print(f"noun = {noun} and verb = {verb} was tried")
    noun += 1
    if noun == 100:
        noun = 0
        verb += 1
    if verb == noun == 99:
        break

print(100*(noun-1) + verb)