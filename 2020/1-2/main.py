from input_loader import input_loader as il
input = il.get_input_as_int_list("input.txt")


def main(input):
    for i in input:
        for j in input:
            target = 2020 - i - j
            if target in input:
                return target*i*j


print(main(input))
