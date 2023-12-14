with open("4.txt") as f:
    cont = f.read().split("\n\n")

nums = cont[0].split(",")
nums = [int(i) for i in nums]
boards = cont[1:]

for i in range(len(boards)):
    boards[i] = boards[i].replace("\n"," ").replace("  ", " ")
    boards[i] = boards[i].split(" ")
    boards[i] = [int(j) for j in boards[i] if j != ""]

for num in nums:
    print(num)

    print(boards)
    for board in range(len(boards)):
        boards[board] = ["X" if i==num else i for i in boards[board]]

        for i in range(0,25,5):
            if boards[board][i:i+5].count("X") == 5:
                print(num*sum([n for n in boards[board] if n!="X"]))
                exit()
        for i in range(5):
            # print(boards[board])
            # print([boards[board][n] for n in range(i,25,5)], [boards[board][n] for n in range(i,25,5)].count("X"))
            # input()
            if [boards[board][n] for n in range(i,25,5)].count("X") == 5:
                print(num*sum([n for n in boards[board] if n!="X"]))
                exit()

for i in boards:
    print(i)