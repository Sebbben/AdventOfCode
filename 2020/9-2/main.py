from input_loader import input_loader as il

inp = il.get_input_as_int_list("input.txt")
#inp = il.get_input_as_int_list("test.txt")


def main(inp):
    preamble_size = 25

    for i in range(preamble_size, len(inp)):
        preamble = inp[i-preamble_size:i]
        if all(inp[i]-num not in preamble for num in preamble):
            return inp[i]


print(main(inp))
