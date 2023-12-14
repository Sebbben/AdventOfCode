from input_loader import input_loader as il

inp = il.get_input_as_int_list("input.txt")
#inp = il.get_input_as_int_list("test.txt")


def getWrongNumber(inp, preamble_size):
    for i in range(preamble_size, len(inp)):
        preamble = inp[i-preamble_size:i]
        if all(inp[i]-num not in preamble for num in preamble):
            return inp[i]


def getContList(inp, num):
    top = 1
    bottom = 0
    while sum(inp[bottom:top]) != num:
        if sum(inp[bottom:top]) > num:
            bottom += 1
        else:
            top += 1
    return inp[bottom:top]


def main(inp):
    preamble_size = 25
    wrong_num = getWrongNumber(inp, preamble_size)
    contiguous_list = getContList(inp, wrong_num)
    return max(contiguous_list) + min(contiguous_list)


print(main(inp))
