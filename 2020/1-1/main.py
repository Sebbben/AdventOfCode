from input_loader import input_loader as il
input = il.get_input_as_int_list("input.txt")


def main(input):
    for i in input:
        if i >= 2020:
            continue
        target = 2020 - i
        if target in input:
            return i*target


print(main(input))
