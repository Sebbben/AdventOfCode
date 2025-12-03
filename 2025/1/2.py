with open("input.txt") as f:
    content = f.readlines()

tot = 0

dial = 50
for line in content:
    if line[0] == "L":
        for _ in range(int(line[1:])):
            dial += 1
            dial %= 100
            tot += dial == 0
    else:
        for _ in range(int(line[1:])):
            dial -= 1
            dial %= 100
            tot += dial == 0
    
        
print(tot)