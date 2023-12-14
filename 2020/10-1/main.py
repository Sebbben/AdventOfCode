from input_loader import input_loader as il

inp = il.get_input_as_int_list("input.txt")
#inp = il.get_input_as_int_list("test.txt")


def main(inp):
    inp.append(0)
    inp.append(max(inp) + 3)
    inp = sorted(inp)
    ones = 0
    threes = 0
    for i in range(1, len(inp)):
        if inp[i]-inp[i-1] == 1:
            ones += 1
        elif inp[i]-inp[i-1] == 3:
            threes += 1
    print(ones, threes)
    return ones * threes


print(main(inp))
