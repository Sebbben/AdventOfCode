from input_loader import input_loader as il

inp = il.get_input_as_string("input.txt")
#inp = il.get_input_as_string("test.txt")


def main(inp):
    inp = inp.splitlines()
    time = int(inp[0])
    busses = [int(i) for i in inp[1].split(",") if i != "x"]
    buss_times = [(time % i)-i for i in busses]
    return busses[buss_times.index(max(buss_times))] * abs(max(buss_times))


print(main(inp))
