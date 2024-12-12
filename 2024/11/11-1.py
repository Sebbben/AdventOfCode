with open("11.txt", "r") as f:
    stones = list(map(int, f.read().strip().split(" ")))

for _ in range(25):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone))%2==0:
            strStone = str(stone)
            newStones.append(int(strStone[:len(strStone)//2]))
            newStones.append(int(strStone[len(strStone)//2:]))
        else:
            newStones.append(stone*2024)
    stones = newStones
    
print(len(stones))