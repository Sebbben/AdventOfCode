with open("11.txt", "r") as f:
    stones = list(map(int, f.read().strip().split(" ")))

memo = {}

for _ in range(75):
    newStones = []
    for stone in stones:
        if stone in memo:
            newStones.extend(memo[stone])
            continue

        if stone == 0:
            memo[stone] = (1,)
            newStones.append(1)
        elif len(str(stone))%2==0:
            strStone = str(stone)
            newStones.append(int(strStone[:len(strStone)//2]))
            newStones.append(int(strStone[len(strStone)//2:]))
            memo[stone] = tuple(newStones[-2:])
            
        else:
            newStones.append(stone*2024)
            memo[stone] = (newStones[-1],)
    stones = newStones
    
print(len(stones))