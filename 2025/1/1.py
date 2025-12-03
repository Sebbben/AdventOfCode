with open("input.txt") as f:
    content = f.readlines()

tot = 0

dial = 50
for line in content:
    if line[0] == "L":
        dial = (dial + int(line[1:])) % 100
    else:
        dial = (dial - int(line[1:])) % 100
    
    if dial == 0:
        tot += 1
        
print(tot)