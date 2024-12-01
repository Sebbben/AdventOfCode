with open("8.txt") as f:
    trees = [list(map(int,list(x))) for x in f.read().splitlines()]

numberOfTreesVisable = 0

for y in range(1,len(trees)-1):
    for x in range(1, len(trees[y])-1):
        if all([right < trees[y][x] for right in trees[y][:x]]):
            numberOfTreesVisable += 1
            continue
        elif all([left < trees[y][x] for left in trees[y][x+1:]]):
            numberOfTreesVisable += 1
            continue
        elif all([trees[up][x] < trees[y][x] for up in range(y)]):
            numberOfTreesVisable += 1
            continue
        elif all([trees[down][x] < trees[y][x] for down in range(y+1,len(trees))]):
            numberOfTreesVisable += 1
            continue

numberOfTreesVisable += len(trees)*2 + len(trees[0])*2 - 4
        

print(numberOfTreesVisable)