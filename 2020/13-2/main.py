from input_loader import input_loader as il

inp = il.get_input_as_string("input.txt")
#inp = il.get_input_as_string("test.txt")

def main(inp):
    inp = inp.splitlines()
    time = int(inp[0])
    busses = inp[1].split(",")
    for i in range(len(busses)):
        if busses[i] != "x":
            busses[i] = int(busses[i])
    inc = max([i for i in busses if i != "x"])
    print(inc)
    exit()
    i = inc + 100000000000000
    i -= busses.index(inc)
    while True:
        print(i)
        for buss in range(len(busses)):
            if busses[buss] != "x":
                if (i+buss)%busses[buss]!=0:
                    break
        else:
            break
        i += inc
        
    print(i,"hallo")


print(main(inp))
