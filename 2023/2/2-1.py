with open("inp.txt", "r") as f:
    data = f.read().splitlines()

tot = 0

maxAmounts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for line in data:
    gameId, game = line.split(": ")
    gameId = gameId.split(" ")[1]
    
    game = game.replace("; ", ", ")
    games = game.split(", ")

    if all((maxAmounts[color] >= int(amount) for color, amount in list(map(lambda x: x.split(" ")[::-1], games)))):
        tot += int(gameId)
        
print(tot)