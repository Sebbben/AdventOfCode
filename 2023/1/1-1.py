import re

with open("inp.txt", "r") as f:
    data = f.read().splitlines()
    
# data = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet""".splitlines()

tot = 0
 
for line in data:
    num = ""
    for char in line:
        if char.isnumeric():
            num += char
            break
    
    for char in line[::-1]:
        if char.isnumeric():
            num += char
            break
    
    tot += int(num)
    
print(tot)