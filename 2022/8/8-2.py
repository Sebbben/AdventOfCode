with open("8.txt") as f:
    trees = [list(map(int,list(x))) for x in f.read().splitlines()]

bestScore = 0

for y in range(1,len(trees)-1):
    for x in range(1, len(trees[y])-1):
        score = 1
        # print("Current test: ",x,y,trees[y][x])

        for left in range(x):
            if trees[y][x-(left+1)] >= trees[y][x]:
                score *= left+1
                break
        else:
            score *= left+1


        for right in range(len(trees[y]) - x - 1):
            if trees[y][x+(right+1)] >= trees[y][x]:
                score *= right+1
                break
        else:
            score *= right+1

        for up in range(y):
            if trees[y-(up+1)][x] >= trees[y][x]:
                score *= up+1
                break
        else:
            score *= up+1

        for down in range(len(trees) - y - 1):
            if trees[y+(down+1)][x] >= trees[y][x]:
                score *= down+1
                break
        else:
            score *= down+1

        bestScore = max(score, bestScore)

print(bestScore)