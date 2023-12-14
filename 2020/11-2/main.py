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
                    suround = []
                    #up
                    for row in range(i-1, 0, -1):
                        if inp[row][j] == "#" or inp[row][j] == "L":
                            suround.append(inp[row][j])
                            break
                    #down
                    for row in range(i+1, len(inp)):
                        if inp[row][j] == "#" or inp[row][j] == "L":
                            suround.append(inp[row][j])
                            break
                    #left
                    for col in range(j-1, 0, -1):
                        if inp[i][col] == "#" or inp[i][col] == "L":
                            suround.append(inp[i][col])
                            break
                    #right
                    for col in range(j+1, len(inp[i])):
                        if inp[i][col] == "#" or inp[i][col] == "L":
                            suround.append(inp[i][col])
                            break
                    #up left
                    for col in range(1, min(i,j)):
                        if inp[i-col][j-col] == "#" or inp[i-col][j-col] == "L":
                            suround.append(inp[i-col][j-col])
                            break
                    #up right
                    for col in range(1, min(i,len(inp[i])-j)):
                        if inp[i-col][j+col] == "#" or inp[i-col][j+col] == "L":
                            suround.append(inp[i-col][j+col])
                            break
                    #down left
                    for col in range(1, min(len(inp)-i,j)):
                        if inp[i+col][j-col] == "#" or inp[i+col][j-col] == "L":
                            suround.append(inp[i+col][j-col])
                            break
                    #down right
                    for col in range(1, min(len(inp)-i,len(inp[i])-j)):
                        if inp[i+col][j+col] == "#" or inp[i+col][j+col] == "L":
                            suround.append(inp[i+col][j+col])
                            break
                    
                    
                    

                    if suround.count("#") == 0:
                        newArr[i].append("#")
                    else:
                        newArr[i].append("L")
                elif inp[i][j] == "#":
                    suround = []
                    #up
                    for row in range(i-1, 0, -1):
                        if inp[row][j] == "#" or inp[row][j] == "L":
                            suround.append(inp[row][j])
                            break
                    #down
                    for row in range(i+1, len(inp)):
                        if inp[row][j] == "#" or inp[row][j] == "L":
                            suround.append(inp[row][j])
                            break
                    #left
                    for col in range(j-1, 0, -1):
                        if inp[i][col] == "#" or inp[i][col] == "L":
                            suround.append(inp[i][col])
                            break
                    #right
                    for col in range(j+1, len(inp[i])):
                        if inp[i][col] == "#" or inp[i][col] == "L":
                            suround.append(inp[i][col])
                            break
                    #up left
                    for col in range(1, min(i,j)):
                        if inp[i-col][j-col] == "#" or inp[i-col][j-col] == "L":
                            suround.append(inp[i-col][j-col])
                            break
                    #up right
                    for col in range(1, min(i,len(inp[i])-j)):
                        if inp[i-col][j+col] == "#" or inp[i-col][j+col] == "L":
                            suround.append(inp[i-col][j+col])
                            break
                    #down left
                    for col in range(1, min(len(inp)-i,j)):
                        if inp[i+col][j-col] == "#" or inp[i+col][j-col] == "L":
                            suround.append(inp[i+col][j-col])
                            break
                    #down right
                    for col in range(1, min(len(inp)-i,len(inp[i])-j)):
                        if inp[i+col][j+col] == "#" or inp[i+col][j+col] == "L":
                            suround.append(inp[i+col][j+col])
                            break
                    if suround.count("#") >= 5:
                        newArr[i].append("L")
                    else:
                        newArr[i].append("#")
                else:
                    newArr[i].append(".")

        for i in newArr:
            print(i)

        if newArr == inp:
            break
        else:
            inp = newArr

    inp = [item for sublist in newArr for item in sublist]
    print(inp.count("#"))


print(main(inp))
