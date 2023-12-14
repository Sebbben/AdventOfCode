with open("7.txt") as f:
    cmds = f.read().splitlines()

wires = {}
vars = {}

def notOpp(n):
    n = list(str(bin(n))[2:])
    for i in range(len(n)):
        
        if n[i] == "1":
            n[i] = "0"
        else:
            n[i] = "1" 
    n = "".join(n)
    n = "1" * (16-len(n)) + n
    return int(n, 2)

for cmd in cmds:
    [cmd,v] = cmd.split(" -> ")
    cmd = cmd.split(" ")


    if len(cmd) == 1 and cmd[0].isnumeric():
        vars[v] = cmd[0]
    else:
        wires[v] = cmd

# print(wires)
while len(wires.keys()) != 0:
    print(len(wires.keys()))
    try:
        for wire in wires.keys():
            for v in vars.keys():
                if v in wires[wire]:
                    currentWire = wires[wire]
                    currentWire[currentWire.index(v)] = vars[v]


                    if currentWire.count("AND") and currentWire[0].isnumeric() and currentWire[2].isnumeric():
                        vars[wire] = int(currentWire[0]) & int(currentWire[2])
                        del wires[wire]
                        break
                    elif currentWire.count("OR") and currentWire[0].isnumeric() and currentWire[2].isnumeric():
                        vars[wire] = int(currentWire[0]) | int(currentWire[2])
                        del wires[wire]
                        break
                    elif currentWire.count("NOT") and currentWire[1].isnumeric():
                        vars[wire] = notOpp(int(currentWire[1]))
                        del wires[wire]
                        break
                    elif currentWire.count("LSHIFT") and currentWire[0].isnumeric():
                        vars[wire] = int(currentWire[0]) << int(currentWire[2])
                        del wires[wire]
                        break
                    elif currentWire.count("RSHIFT") and currentWire[0].isnumeric():
                        vars[wire] = int(currentWire[0]) >> int(currentWire[2])
                        del wires[wire]
                        break


    except Exception as e:
        pass    

print(vars["a"])