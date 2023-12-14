with open("4.txt") as f:
    cont = f.read().split("\n\n")

bingoNumbers = [int(x) for x in cont[0].split(",")]

boards = cont[1:]

for i,board in enumerate(boards):
    board = board.replace("\n"," ").replace("  "," ")
    if board.startswith(" "):
        board = board[1:]
    boards[i] = [int(x) for x in board.split(" ")]

for num in bingoNumbers:
    boards = [b for b in boards if b != "Empty"]
    for i, board in enumerate(boards):
        board = [x if x != num else "X" for x in board]
        if [board[x:x+5] for x in range(0,len(board),5)].count(["X"]*5) == 1:
            print("Win!!")
            if len(boards) == 1:
                score = sum([x for x in board if x != "X"])*num
                print(f"{board} is the last one with score {score}")
                exit()
            board = "Empty"
        if [board[x:25:5] for x in range(5)].count(["X"]*5) == 1:
            print("Win!!#!!")
            if len(boards) == 1:
                score = sum([x for x in board if x != "X"])*num
                print(f"{board} is the last one with score {score}")
                exit()
            board = "Empty"

        boards[i] = board

print(boards)