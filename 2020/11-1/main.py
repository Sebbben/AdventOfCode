from input_loader import input_loader as il

inp = il.get_input_as_list("input.txt")
#inp = il.get_input_as_list("test.txt")


def main(inp=[""]):
    for i in range(len(inp)):
        inp[i] = ["."]+[i for i in inp[i]]+["."]
    inp.append(["."]*len(inp[0]))
    inp = [["."]*len(inp[0])] + inp

    while True:
        newArr = [["."]*len(inp[0])]

        for i in range(1, len(inp)):
            newArr.append([])
            newArr[i].append(".")
            for j in range(1, len(inp[i])):
                if inp[i][j] == "L":
                    top = inp[i-1][j-1:j+2]
                    middle = inp[i][j-1:j+2]
                    bottom = inp[i+1][j-1:j+2]
                    suround = top + middle + bottom
                    if suround.count("#") == 0:
                        newArr[i].append("#")
                    else:
                        newArr[i].append("L")
                elif inp[i][j] == "#":
                    top = inp[i-1][j-1:j+2]
                    middle = inp[i][j-1:j+2]
                    bottom = inp[i+1][j-1:j+2]
                    suround = top + middle + bottom
                    if suround.count("#")-1 >= 4:
                        newArr[i].append("L")
                    else:
                        newArr[i].append("#")
                else:
                    newArr[i].append(".")

        """for i in newArr:
            print(i)
"""

        if newArr == inp:
            break
        else:
            inp = newArr

    inp = [item for sublist in newArr for item in sublist]
    print(inp.count("#"))


print(main(inp))
