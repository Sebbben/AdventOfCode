with open("inp.txt", "r") as f:
    data = f.read().splitlines()

tot = 0

for line in data:
    gameId, game = line.split(": ")
    gameId = gameId.split(" ")[1]
    
    game = game.replace("; ", ", ")
    games = game.split(", ")

    cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    
    for game in games:
        amount, color = game.split(" ")
        cubes[color] = max(int(amount), cubes[color])
    tot += cubes["red"]*cubes["green"]*cubes["blue"]
        
print(tot)