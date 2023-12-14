from input_loader import input_loader as il

inp = il.get_input_as_int_list("input.txt")
#inp = il.get_input_as_int_list("test.txt")
#inp = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def getNextAdapters(arr, rating):
    return [x for x in arr if 1 <= x-rating <= 3]


def main(inp):
    inp.append(0)
    inp.append(max(inp) + 3)
    inp = sorted(inp)
    all_options = []
    arr = [[0]]
    while len(arr) != 0:
        print(len(arr[0]))
        newArr = []
        for i in arr:
            next_dapters = getNextAdapters(inp, i[-1])
            if len(next_dapters) == 0:
                all_options.append(i)  
                continue
            for j in next_dapters:
                newArr.append(i + [j])
        arr = newArr
    for i in all_options:
        print(i)
    return len(all_options)


print(main(inp))
