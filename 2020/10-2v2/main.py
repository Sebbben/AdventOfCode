from input_loader import input_loader as il

inp = il.get_input_as_int_list("input.txt")
#inp = il.get_input_as_int_list("test.txt")
#inp = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def getNextAdapters(arr, rating):
    return [x for x in arr if 1 <= x-rating <= 3]


def getAllOptions(inp):
    all_options = []
    arr = [[inp[0]]]
    while len(arr) != 0:
        newArr = []
        for i in arr:
            next_dapters = getNextAdapters(inp, i[-1])
            if len(next_dapters) == 0:
                all_options.append(i)
                continue
            for j in next_dapters:
                newArr.append(i + [j])
        arr = newArr
    return all_options


def main(inp):
    inp.append(0)
    inp.append(max(inp) + 3)
    inp = sorted(inp)

    diff_inp = [inp[i+1]-inp[i] for i in range(len(inp)-1)]

    one_groups = []
    new_group = []
    for i in range(len(diff_inp)):
        if diff_inp[i] == 1:
            new_group.append(inp[i])
        else:
            if len(new_group) >= 2:
                new_group.append(inp[i])
                one_groups.append(new_group)
            new_group = []

    for i in one_groups:
        start = inp.index(i[0])
        end = inp.index(i[-1])
        inp[start: end+1] = ["*"]

    tot = 1

    for i in one_groups:
        tot *= len(getAllOptions(i))

    return tot


print(main(inp))
